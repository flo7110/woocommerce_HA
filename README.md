# WooCommerce Integration for Home Assistant

## Description

This integration allows Home Assistant to interact with your WooCommerce store. It uses the WooCommerce API to fetch orders and other relevant data from your store.

## Features

- **Fetch orders**: Retrieve orders from WooCommerce.
- **Configure API keys**: Set up your WooCommerce API keys and URL directly from the Home Assistant UI.

## Installation

1. **Download and Install**: Go to HACS > Integration. Click on the 3 dots in the corner and add a custom repository. Add this URL https://github.com/flo7110/woocommerce_HA and select "Integration"
2. Restart Home Assistant: After installation, restart Home Assistant to load the new integration.

## Configuration
Add Integration: Go to Configuration > Integrations in Home Assistant and click on Add Integration.

Configure WooCommerce:

Consumer Key: Your WooCommerce Consumer Key.
Consumer Secret: Your WooCommerce Consumer Secret.
WooCommerce URL: The URL of your WooCommerce store.
Configuration Flow
The configuration flow allows you to enter the following details:

Consumer Key: The API key used to access your WooCommerce store.
Consumer Secret: The secret key used along with the Consumer Key.
WooCommerce URL: The base URL of your WooCommerce store.
The configuration form now includes descriptive labels for each field:

Consumer Key: "Consumer Key"
Consumer Secret: "Consumer Secret"
WooCommerce URL: "WooCommerce URL"