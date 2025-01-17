import logging

import voluptuous as vol
from homeassistant.config_entries import (
    ConfigFlow,
    OptionsFlow,
    ConfigEntry
)
from homeassistant.core import callback

from . import init_hass_data, data_masking, gen_auth_entry
from .core.const import *

_LOGGER = logging.getLogger(__name__)

DEVICE_GET_TOKEN_CONFIG = vol.Schema({vol.Required(CONF_FIELD_AUTH_CODE): str})


class AqaraBridgeFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle an Aqara Bridge config flow."""

    VERSION = 1

    def __init__(self):
        """Initialize."""
        self.account = None
        self.country_code = None
        self.account_type = None
        self.app_id = None
        self.app_key = None
        self.key_id = None
        self._session = None
        self._device_manager = None

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry):
        """ get option flow """
        return OptionsFlowHandler(config_entry.entry_id)

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        init_hass_data(self.hass)
        self._device_manager = self.hass.data[DOMAIN][HASS_DATA_AIOT_MANAGER]
        auth_entry_id = self.hass.data[DOMAIN][HASS_DATA_AUTH_ENTRY_ID]
        self._session = self.hass.data[DOMAIN][HASS_DATA_AIOTCLOUD]
        return await self.async_step_get_auth_code()

    async def async_step_get_auth_code(self, user_input=None):
        """Configure an aqara device through the Aqara Cloud."""
        errors = {}
        if user_input:
            self.account = user_input.get(CONF_FIELD_ACCOUNT)
            self.country_code = user_input.get(CONF_FIELD_COUNTRY_CODE)
            self.app_id = user_input.get(CONF_FIELD_APP_ID)
            self.app_key = user_input.get(CONF_FIELD_APP_KEY)
            self.key_id = user_input.get(CONF_FIELD_KEY_ID)
            self.account_type = 0
            self._session.set_country(self.country_code)
            self._session.set_app_id(self.app_id)
            self._session.set_app_key(self.app_key)
            self._session.set_key_id(self.key_id)

            refresh_token = user_input.get(CONF_FIELD_REFRESH_TOKEN)
            if refresh_token and refresh_token != "":
                resp = await self._session.async_refresh_token(refresh_token)
                if resp["code"] == 0:
                    auth_entry = gen_auth_entry(
                        self.app_id, self.app_key, self.key_id,
                        self.account, self.account_type, self.country_code,
                        resp["result"],
                    )
                    self.hass.async_add_job(
                        self.hass.config_entries.flow.async_init(
                            DOMAIN, context={"source": "get_token"}, data=auth_entry
                        )
                    )
                    return self.async_abort(reason="complete")
                else:
                    errors['base'] = 'refresh_token_error'
            else:
                resp = await self._session.async_get_auth_code(self.account, 0)
                if resp["code"] == 0:
                    return await self.async_step_get_token()
                else:
                    errors['base'] = 'auth_code_error'
        def_account = user_input.get(
            CONF_FIELD_ACCOUNT) if user_input and user_input.get(CONF_FIELD_ACCOUNT) else ""
        def_country_code = user_input.get(CONF_FIELD_COUNTRY_CODE) if user_input and user_input.get(
            CONF_FIELD_COUNTRY_CODE) else SERVER_COUNTRY_CODES_DEFAULT
        def_app_id = user_input.get(CONF_FIELD_APP_ID) if user_input and user_input.get(
            CONF_FIELD_APP_ID) else DEFAULT_CLOUD_APP_ID
        def_app_key = user_input.get(CONF_FIELD_APP_KEY) if user_input and user_input.get(
            CONF_FIELD_APP_KEY) else DEFAULT_CLOUD_APP_KEY
        def_key_id = user_input.get(CONF_FIELD_KEY_ID) if user_input and user_input.get(
            CONF_FIELD_KEY_ID) else DEFAULT_CLOUD_KEY_ID

        config_scheme = vol.Schema({
            vol.Required(CONF_FIELD_ACCOUNT, default=def_account): str,
            vol.Required(CONF_FIELD_COUNTRY_CODE, default=def_country_code): vol.In(SERVER_COUNTRY_CODES),
            vol.Required(CONF_FIELD_APP_ID, default=def_app_id): str,
            vol.Required(CONF_FIELD_APP_KEY, default=def_app_key): str,
            vol.Required(CONF_FIELD_KEY_ID, default=def_key_id): str,
            vol.Optional(CONF_FIELD_REFRESH_TOKEN): str,
        })
        return self.async_show_form(
            step_id="get_auth_code",
            data_schema=config_scheme,
            errors=errors,
        )

    async def async_step_get_token(self, user_input=None):
        errors = {}
        if user_input:
            if CONF_FIELD_AUTH_CODE in user_input:
                auth_code = user_input.get(CONF_FIELD_AUTH_CODE)
                resp = await self._session.async_get_token(auth_code, self.account, 0)

                if resp["code"] == 0:
                    auth_entry = gen_auth_entry(
                        self.app_id, self.app_key, self.key_id,
                        self.account, self.account_type, self.country_code,
                        resp["result"],
                    )
                    self.hass.async_add_job(
                        self.hass.config_entries.flow.async_init(
                            DOMAIN, context={"source": "get_token"}, data=auth_entry
                        )
                    )
                else:
                    errors["base"] = "get_auth_code_error"
            elif CONF_ENTRY_AUTH_ACCOUNT in user_input:
                return self.async_create_entry(
                    title=data_masking(user_input[CONF_ENTRY_AUTH_ACCOUNT], 4),
                    data=user_input,
                )

            return self.async_abort(reason="complete")

        return self.async_show_form(
            step_id="get_token", data_schema=DEVICE_GET_TOKEN_CONFIG, errors=errors
        )


class OptionsFlowHandler(OptionsFlow):
    def __init__(self, entry_id):
        """Initialize options flow."""
        self.entry_id = entry_id
        self.account = None
        self.country_code = None
        self.account_type = 0
        self._session = None

    async def async_step_init(self, user_input=None):
        """Configure an aqara device through the Aqara Cloud."""
        errors = {}

        config_entry = self.hass.config_entries.async_get_entry(self.entry_id)
        if isinstance(user_input, dict):
            # 用户输入
            self.account = user_input.get(CONF_FIELD_ACCOUNT)
            self.country_code = user_input.get(CONF_FIELD_COUNTRY_CODE)
            if self._session is None:
                self._session = self.hass.data[DOMAIN][HASS_DATA_AIOTCLOUD]
            self._session.set_country(self.country_code)
            self._session.set_app_id(user_input.get(CONF_FIELD_APP_ID))
            self._session.set_app_key(user_input.get(CONF_FIELD_APP_KEY))
            self._session.set_key_id(user_input.get(CONF_FIELD_KEY_ID))

            refresh_token = user_input.get(CONF_FIELD_REFRESH_TOKEN)
            if refresh_token and refresh_token != "":
                # 更新了token值
                resp = await self._session.async_refresh_token(refresh_token)
                if resp["code"] == 0:
                    auth_entry = gen_auth_entry(
                        self._session.get_app_id(), self._session.get_app_key(), self._session.get_key_id(),
                        self.account, self.account_type, self.country_code,
                        resp["result"],
                    )
                    self.hass.config_entries.async_update_entry(
                        config_entry, data=auth_entry)
                    return self.async_abort(reason="complete")
                else:
                    errors['base'] = 'refresh_token_error'
            else:
                resp = await self._session.async_get_auth_code(self.account, 0)
                if resp["code"] == 0:
                    return await self.async_step_option_get_token()
                else:
                    errors['base'] = 'auth_code_error'
        else:
            prev_input = {
                **config_entry.data,
                **config_entry.options,
            }
            config_scheme = vol.Schema(
                {
                    vol.Required(CONF_FIELD_ACCOUNT,
                                 default=prev_input.get(CONF_ENTRY_AUTH_ACCOUNT, vol.UNDEFINED)): str,
                    vol.Required(CONF_FIELD_COUNTRY_CODE,
                                 default=prev_input.get(SERVER_COUNTRY_CODES_DEFAULT, vol.UNDEFINED)): vol.In(SERVER_COUNTRY_CODES),
                    vol.Optional(CONF_FIELD_APP_ID,
                                 default=prev_input.get(CONF_ENTRY_APP_ID, vol.UNDEFINED)): str,
                    vol.Optional(CONF_FIELD_APP_KEY,
                                 default=prev_input.get(CONF_ENTRY_APP_KEY, vol.UNDEFINED)): str,
                    vol.Optional(CONF_FIELD_KEY_ID,
                                 default=prev_input.get(CONF_ENTRY_KEY_ID, vol.UNDEFINED)): str,
                    vol.Optional(CONF_FIELD_REFRESH_TOKEN): str,
                }
            )
            return self.async_show_form(step_id="init", data_schema=config_scheme, errors=errors)

    async def async_step_option_get_token(self, user_input=None):
        errors = {}
        config_entry = self.hass.config_entries.async_get_entry(self.entry_id)
        if user_input and CONF_FIELD_AUTH_CODE in user_input:
            auth_code = user_input.get(CONF_FIELD_AUTH_CODE)
            resp = await self._session.async_get_token(auth_code, self.account, 0)
            if resp["code"] == 0:
                auth_entry = gen_auth_entry(
                    self._session.get_app_id(), self._session.get_app_key(), self._session.get_key_id(),
                    self.account, self.account_type, self.country_code,
                    resp["result"],
                )
                self.hass.config_entries.async_update_entry(
                    config_entry, data=auth_entry)
                return self.async_abort(reason="complete")
            else:
                errors["base"] = "auth_code_error"
        return self.async_show_form(
            step_id="option_get_token", data_schema=DEVICE_GET_TOKEN_CONFIG, errors=errors
        )
