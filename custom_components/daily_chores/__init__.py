from homeassistant.core import HomeAssistant, ServiceCall
from .sensor import DailyChoresSensor
from datetime import datetime

SENSOR = None

async def async_setup(hass: HomeAssistant, config: dict):
    global SENSOR
    SENSOR = DailyChoresSensor("Daily Chores")
    hass.states.async_set("sensor.daily_chores", SENSOR.state)

    async def handle_add_chore(call: ServiceCall):
        name = call.data["name"]
        assigned_to = call.data["assigned_to"]
        interval_days = call.data["interval_days"]
        initial_due_date = call.data.get("initial_due_date")
        if initial_due_date:
            initial_due_date = datetime.strptime(initial_due_date, "%Y-%m-%d").date()
        SENSOR.add_chore(name, assigned_to, interval_days, initial_due_date)
        hass.states.async_set("sensor.daily_chores", SENSOR.state)

    hass.services.async_register(
        "daily_chores", "add_chore", handle_add_chore
    )

    async def handle_complete_chore(call: ServiceCall):
        name = call.data["name"]
        completed_date = call.data.get("completed_date")
        if completed_date:
            completed_date = datetime.strptime(completed_date, "%Y-%m-%d").date()
        SENSOR.complete_chore(name, completed_date)
        hass.states.async_set("sensor.daily_chores", SENSOR.state)

    hass.services.async_register(
        "daily_chores", "complete_chore", handle_complete_chore
    )

    return True