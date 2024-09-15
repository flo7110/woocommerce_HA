import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

class WooCommerceConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for WooCommerce Integration."""
    
    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return WooCommerceOptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Crée l'entrée avec les données fournies
            return self.async_create_entry(title="WooCommerce", data=user_input)

        # Définir le schéma pour la saisie de l'utilisateur
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("consumer_key", default="", description="Consumer Key for WooCommerce API"): str,
                vol.Required("consumer_secret", default="", description="Consumer Secret for WooCommerce API"): str,
                vol.Required("url", default="", description="URL of your WooCommerce store"): str,
            })
        )

class WooCommerceOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow."""
    
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required("consumer_key", default=self.config_entry.data.get("consumer_key"), description={"name": "Consumer Key"}): str,
                vol.Required("consumer_secret", default=self.config_entry.data.get("consumer_secret"), description={"name": "Consumer Secret"}): str,
                vol.Required("url", default=self.config_entry.data.get("url"), description={"name": "WooCommerce URL"}): str,
            })
        )
