import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 25 and plugged!=True:
    from pynotifier import Notification
    Notification(
        title="ALERT! BATTERY LOW!",
        description=str(percent) + "% BATTERY REMAIN!!",
        duration=10,
    ).send()

