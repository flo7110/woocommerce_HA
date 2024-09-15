import requests
from requests.auth import HTTPBasicAuth
from homeassistant.helpers.entity import Entity

from .const import DOMAIN

# Définition du capteur WooCommerce
class WooCommerceOrderSensor(Entity):
    def __init__(self, config_entry):
        """Initialisation du capteur."""
        self._name = "WooCommerce Orders"
        self._state = None
        self._config = config_entry.data

    @property
    def name(self):
        """Retourne le nom du capteur."""
        return self._name

    @property
    def state(self):
        """Retourne l'état actuel du capteur."""
        return self._state

    def update(self):
        """Mise à jour des informations du capteur."""
        consumer_key = self._config["consumer_key"]
        consumer_secret = self._config["consumer_secret"]
        url = self._config["url"]

        try:
            # Appel API WooCommerce pour récupérer les commandes
            response = requests.get(
                f"{url}/wp-json/wc/v3/orders",
                auth=HTTPBasicAuth(consumer_key, consumer_secret)
            )
            response.raise_for_status()
            orders = response.json()
            self._state = len(orders)  # Nombre de commandes trouvées
        except requests.exceptions.RequestException as e:
            self._state = "Error"
            print(f"Erreur lors de la récupération des commandes : {e}")

# Fonction pour configurer et enregistrer le capteur
async def async_setup_entry(hass, config_entry, async_add_entities):
    """Configurer les capteurs WooCommerce."""
    async_add_entities([WooCommerceOrderSensor(config_entry)])
