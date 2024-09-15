from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: ConfigType):
    """Configurer l'intégration via YAML (optionnel)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Configurer l'intégration via l'UI."""
    hass.data[DOMAIN] = entry.data

    # Charger la plateforme des capteurs
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Désinstaller l'intégration."""
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    hass.data.pop(DOMAIN)
    return True
