from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    """Configurer l'intégration via YAML (optionnel)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Configurer l'intégration via l'UI."""
    # Assure-toi que les données de configuration sont bien extraites
    consumer_key = entry.data.get("consumer_key")
    consumer_secret = entry.data.get("consumer_secret")
    url = entry.data.get("url")

    # Vérifie que les clés existent bien avant d'utiliser les valeurs
    if not consumer_key or not consumer_secret or not url:
        return False

    # Stocker les données dans hass.data pour les autres parties de l'intégration
    hass.data[DOMAIN] = {
        "consumer_key": consumer_key,
        "consumer_secret": consumer_secret,
        "url": url,
    }

    # Charger la plateforme des capteurs (sensor.py)
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "sensor"))
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Désinstaller l'intégration."""
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    hass.data.pop(DOMAIN)
    return True
