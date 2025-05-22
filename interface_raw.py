from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class EmailNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"Sending email notification: {message}")


class SMSNotificationSender(NotificationSender):
    def send_notification(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")


obj = EmailNotificationSender()
obj.send_notification("Hello, this is a test email notification.")

sms_obj = SMSNotificationSender()
sms_obj.send_notification("Hello, this is a test SMS notification.")