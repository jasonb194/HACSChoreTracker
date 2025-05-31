# HACS Daily Chores

This Home Assistant addon allows users to track their daily chores efficiently. With this addon, you can manage your chores, mark them as complete, and keep track of your progress.

## Installation

1. Ensure you have Home Assistant installed and running.
2. Install HACS (Home Assistant Community Store) if you haven't already.
3. Download the `hacs-daily-chores` repository and place it in the `custom_components` directory of your Home Assistant configuration.
4. Restart Home Assistant to load the new component.

## Usage

After installation, you can add the Daily Chores sensor to your Home Assistant configuration. This will allow you to monitor and manage your daily chores directly from the Home Assistant interface.

### Configuration Example

```yaml
sensor:
  - platform: daily_chores
    name: My Daily Chores
```

## Features

- Track daily chores and their completion status.
- Custom services to add or complete chores.
- Easy integration with Home Assistant.

## Troubleshooting

If you encounter any issues, please check the logs for errors related to the Daily Chores component. Ensure that the component is correctly installed and that Home Assistant is up to date.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.