# HACS Daily Chores

A Home Assistant custom integration to help you track, schedule, and complete daily chores for your household. Add, view, and mark chores as complete—all from the Home Assistant UI.

---

## Features

- Track chores with a name, assignee, and recurrence interval.
- Set an initial due date for each chore.
- Only the next instance of each chore is displayed.
- Mark chores as complete; the next due date is automatically recalculated.
- Exposes custom services for adding and completing chores.
- Integrates with Lovelace dashboards (including custom card support).

---

## Installation

### Manual

1. Ensure you have Home Assistant and [HACS](https://hacs.xyz/) installed.
2. Download or clone this repository into your Home Assistant `custom_components` directory:
   ```
   custom_components/daily_chores/
   ```
3. Restart Home Assistant.

### HACS Custom Repository

1. In Home Assistant, go to **HACS → Integrations → Custom repositories**.
2. Add your GitHub repo URL (e.g., `https://github.com/jasonb194/hacs-daily-chores`) as an **Integration**.
3. Install "Daily Chores" from HACS.
4. Restart Home Assistant.

---

## Usage

### Services

This integration provides two services:

#### 1. `daily_chores.add_chore`

Add a new chore.

**Service Data Example:**
```yaml
name: Take out trash
assigned_to: Alex
interval_days: 7
initial_due_date: 2025-06-01  # Optional, defaults to today
```

#### 2. `daily_chores.complete_chore`

Mark a chore as complete.

**Service Data Example:**
```yaml
name: Take out trash
completed_date: 2025-06-02  # Optional, defaults to today
```

You can call these services from **Developer Tools → Services**, automations, or scripts.

---

### Viewing Chores

- The integration creates a sensor: `sensor.daily_chores`.
- You can add this sensor to an Entities card in your Lovelace dashboard to view the next due chore.

**Example Entities Card:**
```yaml
type: entities
entities:
  - sensor.daily_chores
```

---

### Custom Lovelace Card (Optional)

You can use the included custom card for a better UI experience.

1. Copy `www/daily-chores-card.js` to your `/config/www/` directory.
2. In Home Assistant, go to **Settings → Dashboards → Resources** and add:
   ```
   /local/daily-chores-card.js
   ```
   as a JavaScript module.
3. Add the card to your dashboard:
   ```yaml
   type: custom:daily-chores-card
   title: Daily Chores
   ```

This card allows you to add chores and mark them as complete directly from the dashboard.

---

## Troubleshooting

- Check **Settings → System → Logs** for errors related to `daily_chores`.
- Ensure the integration is in the correct directory and Home Assistant has been restarted.
- If the custom card does not appear, verify the resource path and browser cache.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing

Pull requests and suggestions are welcome! Please open an issue or PR on GitHub.