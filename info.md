# HACS Daily Chores Addon

## Overview
The HACS Daily Chores addon allows users to track and manage their daily chores efficiently within Home Assistant. This addon provides a sensor to monitor the status of chores and custom services to add or complete chores.

## Features
- Track daily chores with a dedicated sensor.
- Add new chores and mark them as completed using custom services.
- Integration with Home Assistant for seamless automation.

## Configuration
To configure the Daily Chores addon, add the following to your `configuration.yaml`:

```yaml
sensor:
  - platform: daily_chores
```

## Troubleshooting
If you encounter issues with the Daily Chores addon:
- Ensure that the addon is properly installed and configured in Home Assistant.
- Check the Home Assistant logs for any error messages related to the Daily Chores component.
- Verify that the custom services are correctly defined in `services.yaml`.

For further assistance, please refer to the README.md file or the Home Assistant community forums.