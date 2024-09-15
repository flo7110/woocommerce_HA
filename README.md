# WooCommerce Integration for Home Assistant

This integration allows you to monitor your WooCommerce store directly in Home Assistant.

## Installation

1. Add this repository to [HACS](https://hacs.xyz/) as a custom repository.
2. Search for "WooCommerce Integration" and install it.
3. Add the following to your `configuration.yaml` file:

```yaml
woocommerce_integration:
  consumer_key: "your_consumer_key"
  consumer_secret: "your_consumer_secret"
  url: "https://your-woocommerce-store.com"
```
4. Restart Home Assistant
