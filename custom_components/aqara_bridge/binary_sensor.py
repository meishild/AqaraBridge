"""Support for Xiaomi Aqara binary sensors."""
import logging
import time

try:
    # hass 2024.11
    from homeassistant.config import DATA_CUSTOMIZE
except (ModuleNotFoundError, ImportError):
    from homeassistant.helpers.entity import DATA_CUSTOMIZE
from homeassistant.helpers.event import async_call_later
from homeassistant.components.binary_sensor import BinarySensorEntity

from .core.aiot_manager import (
    AiotManager,
    AiotEntityBase,
)
from .core.const import (
    CONF_OCCUPANCY_TIMEOUT,
    DOMAIN,
    HASS_DATA_AIOT_MANAGER
)

TYPE = "binary_sensor"

DATA_KEY = f"{TYPE}.{DOMAIN}"

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    manager: AiotManager = hass.data[DOMAIN][HASS_DATA_AIOT_MANAGER]
    cls_entities = {
        "motion": AiotMotionBinarySensor,
        "exist": AiotExistBinarySensor,
        "contact": AiotDoorBinarySensor,
        "default": AiotBinarySensorEntity
    }
    await manager.async_add_entities(
        config_entry, TYPE, cls_entities, async_add_entities
    )


class AiotBinarySensorEntity(AiotEntityBase, BinarySensorEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotEntityBase.__init__(self, hass, device, res_params, TYPE, channel, **kwargs)
        self._attr_state_class = kwargs.get("state_class")
        self._extra_state_attributes.extend(["trigger_time", "trigger_dt"])

    def convert_res_to_attr(self, res_name, res_value):
        if res_name == "firmware_version":
            return res_value
        if res_name == "zigbee_lqi":
            return int(res_value)
        if res_name == "voltage":
            return format(float(res_value) / 1000, '.3f')
        if res_name in ["moisture", "smoke"]:
            return int(res_value) != 0
        return super().convert_res_to_attr(res_name, res_value)

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        if self.device_class in ["moisture", "smoke"] and self._attr_is_on is None:
            return False
        return self._attr_is_on
        
class AiotMotionBinarySensor(AiotBinarySensorEntity, BinarySensorEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotBinarySensorEntity.__init__(self, hass, device, res_params, channel, **kwargs)
        # 关闭间隔
        self._attr_detect_time = 150
        # 最后移动时间
        self._last_on = 0
        self._last_off = 0
        self._timeout_pos = 0
        self._unsub_set_no_motion = None
        self._attr_is_on = False
        self._extra_state_attributes.extend(["detect_time"])
    
    @property
    def detect_time(self):
        return self._attr_detect_time
    
    async def _start_no_motion_timer(self, delay: float):
        if self._unsub_set_no_motion:
            self._unsub_set_no_motion()

        self._unsub_set_no_motion = async_call_later(
            self.hass, abs(delay), self._set_no_motion)

    async def _set_no_motion(self, *args):
        self._last_off = time.time()
        self._timeout_pos = 0
        self._unsub_set_no_motion = None
        self._attr_is_on = False
        self.schedule_update_ha_state()

        # repeat event from Aqara integration
        self.hass.bus.fire('xiaomi_aqara.motion', {
            'entity_id': self.entity_id
        })

    def convert_res_to_attr(self, res_name, res_value):
        log_info = "[conver_attr, {}, {}]".format(self.device.did, self._attr_name)
        if res_name in ["firmware_version", "zigbee_lqi", "voltage"]:
            return super().convert_res_to_attr(res_name, res_value)

        # 间隔时间刷新
        if res_name in ["detect_time"]:
            return int(res_value)

        # 移动只会有on被触发
        if self._last_on == 0 and self.trigger_time is not None:
            self._last_on = self.trigger_time

        res_value = int(res_value)
        time_now = time.time()

        if time_now - self._last_on < 1:
            _LOGGER.warn("{}false, time_now:{} < last_on:{}".format(log_info ,time_now, self._last_on))
            return
        self._attr_is_on = bool(res_value)

        # 检查是否超过最长delay时间，超过未无人状态
        if time_now - self.trigger_time > self.detect_time:
            self._attr_is_on = False
            _LOGGER.info("{}false, time_now:{} - trigger_time:{} > detect_time:{}".format(log_info ,time_now, self.trigger_time, self.detect_time))
            return False

        # handle available change
        self.schedule_update_ha_state()

        if self._unsub_set_no_motion:
            self._unsub_set_no_motion()

        custom = self.hass.data[DATA_CUSTOMIZE].get(self.entity_id)

        # if customize of any entity will be changed from GUI - default value
        # for all motion sensors will be erased
        timeout = custom.get(CONF_OCCUPANCY_TIMEOUT, self.detect_time)
        if timeout:
            if isinstance(timeout, list):
                pos = min(self._timeout_pos, len(timeout) - 1)
                delay = timeout[pos]
                self._timeout_pos += 1
            else:
                delay = timeout

            if delay < 0 and time_now + delay < self._last_off:
                delay *= 2
            self.hass.add_job(self._start_no_motion_timer, delay)
        _LOGGER.info("{}conver_value:{}".format(log_info ,bool(res_value)))
        return bool(res_value)


class AiotExistBinarySensor(AiotBinarySensorEntity, BinarySensorEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotBinarySensorEntity.__init__(self, hass, device, res_params, channel, **kwargs)
        self._extra_state_attributes.extend(["monitor_type", "direction_status", "content_direction", "content_leftright"])
        self._attr_monitor_type = None
        self._attr_direction_status = None
    
    @property
    def monitor_type(self):
        return self._attr_monitor_type
    
    @property
    def direction_status(self):
        return self._attr_direction_status

    @property
    def content_direction(self):
        return "monitor_type:0:无向检测,direction_status:0:进入,1:离开,6:接近,7:远离"

    @property
    def content_leftright(self):
        return "monitor_type:1:左右检测,direction_status:2:左进 3:右出 4:右进 5:左出 6:接近 7:远离"

    def convert_res_to_attr(self, res_name, res_value):
        if res_name in ["firmware_version", "zigbee_lqi", "voltage"]:
            return super().convert_res_to_attr(res_name, res_value)
        if res_name in ["direction_status", "monitor_type"]:
            return res_value

        self._attr_is_on = int(res_value) == 1
        self.schedule_update_ha_state()
        return int(res_value) == 1


class AiotDoorBinarySensor(AiotBinarySensorEntity, BinarySensorEntity):
    def convert_res_to_attr(self, res_name, res_value):
        if res_name in ["firmware_version", "zigbee_lqi", "voltage"]:
            return super().convert_res_to_attr(res_name, res_value)

        self._attr_is_on = int(res_value) == 1
        self.schedule_update_ha_state()
        return int(res_value) == 1
