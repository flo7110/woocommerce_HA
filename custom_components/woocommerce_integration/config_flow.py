import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

class WooCommerceConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for WooCommerce."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Manage the configuration options for the integration."""
        errors = {}

        if user_input is not None:
            # Validation des informations saisies
            return self.async_create_entry(title="WooCommerce", data=user_input)

        # Ajouter des placeholders pour chaque champ
        data_schema = vol.Schema({
            vol.Required("url", default=""): str,
            vol.Required("consumer_key", default=""): str,
            vol.Required("consumer_secret", default=""): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
            description_placeholders={
                "url": "Entrez l'URL de votre site WooCommerce (ex. https://votresite.com)",
                "consumer_key": "Entrez votre Consumer Key WooCommerce",
                "consumer_secret": "Entrez votre Consumer Secret WooCommerce"
            }
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return WooCommerceOptionsFlowHandler(config_entry)


class WooCommerceOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle an options flow for WooCommerce."""

    def __init__(self, config_entry):
        """Initialize WooCommerce options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options for the custom integration."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema({
            vol.Optional("option1", default=self.config_entry.options.get("option1", False)): bool,
            vol.Optional("option2", default=self.config_entry.options.get("option2", False)): bool,
        })

        return self.async_show_form(
            step_id="init",
            data_schema=data_schema
        )
