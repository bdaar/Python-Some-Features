from notifypy import Notify

notif = Notify()
notif.urgency = "critical"
notif.application_name = "App Name"
notif.title = "Notify Title"
notif.message = "Message"
notif.icon = "Icon Path"
notif.send()