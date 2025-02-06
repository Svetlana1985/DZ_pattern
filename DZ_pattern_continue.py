from abc import ABC, abstractmethod
from os import remove
from typing import List
import pyaudio
import pyttsx3
import os
#
# class IAlert(ABC):
#     @abstractmethod
#     def send_alert(self, message: str) -> None:
#         pass
#
# class Phone:
#     def send_sms(self, text: str) -> None:
#         print(f'Phone: Sending SMS - {text}')
#
# class Email:
#     def send_email(self, subject: str, body: str) -> None:
#         print(f'Email: Sending email - {subject}\n {body}')
#
# class Notification:
#     def broadcast(self, message: str):
#         print(f'Notification: Listen - {message}')
#
# class PhoneAdapter(IAlert):
#     def __init__(self, phone: Phone):
#         self.phone = phone
#
#     def send_alert(self, message: str) -> None:
#         self.phone.send_sms(message)
#
# class EmailAdapter(IAlert):
#     def __init__(self, email: Email):
#         self.email = email
#
#     def send_alert(self, message: str) -> None:
#         self.email.send_email('Notification: ', message)
#
# class NotificationAdapter(IAlert):
#     def __init__(self, notification: Notification):
#         self.notification = notification
#         self.tts_engine = pyttsx3.init()
#         self.tts_engine.setProperty('rate', 150)
#         self.tts_engine.setProperty('volume', 0.7)
#
#     def send_alert(self, message: str) -> None:
#         self.notification.broadcast(message)
#         try:
#             self.tts_engine.say(message)
#             self.tts_engine.runAndWait()
#         except Exception as e:
#             print(f"Error during text-to-speech: {e}")
#
# def send_alerts_to_devices(devices: List[IAlert], message: str) -> None:
#     for device in devices:
#         device.send_alert(message)
#
# if __name__ == '__main__':
#     phone = Phone()
#     email = Email()
#     notification = Notification()
#     phone_adapter = PhoneAdapter(phone)
#     email_adapter = EmailAdapter(email)
#     notification_adapter = NotificationAdapter(notification)
#     alert_devices: List[IAlert] = [phone_adapter, email_adapter, notification_adapter]
#     alert_message = 'Attention! Snowstorms are expected!'
#     send_alerts_to_devices(alert_devices, alert_message)

# Задаиние №2
class MenuItem(ABC):
    @abstractmethod
    def display(self) -> None:
        pass
    def get_price(self) -> float:
        pass

class Dish(MenuItem):
    def __init__(self, dish_name: str, description: str, price: float):
        self.dish_name = dish_name
        self.description = description
        self.price = price

    def display(self) -> None:
        print(f'{self.dish_name}: {self.description} (Price {self.price}₽)')

    def get_price(self) -> float:
        return self.price

class Menu(MenuItem):
    def __init__(self, name: str):
        self.name = name
        self.items: List[MenuItem] = []

    def add(self, item: MenuItem) -> None:
        if not item in self.items:
            self.items.append(item)

    def remove(self, item: MenuItem) -> None:
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError('This item is not in the List!')

    def display(self) -> None:
        print (f'\n {self.name}')
        for item in self.items:
            item.display()

    def get_price(self) -> float:
        total_price = 0.0
        for item in self.items:
            total_price +=item.get_price()
        return total_price

def print_menu(menu: MenuItem) -> None:
    menu.display()
    print(f'\n Total price: {menu.get_price()}₽')

if __name__ == '__main__':
    first_dish_1 = Dish('Borsch', 'Vegetable soup with beef served with sour cream',
                        550.0)
    first_dish_2 = Dish('Fish soup', 'Omul ear with herbs and pepper',
                        780.0)
    second_dish_1 = Dish('Potato casserole', 'Mashed potatoes with pork and cream sauce',
                         340.0)
    second_dish_2 = Dish('Cabbage rolls', 'Meat in cabbage leaves baked in a spicy sauce',
                         450.0)
    desert_1 = Dish('Chak-Chak', 'Cookies in honey', 255.0)
    desert_2 = Dish('Romovaja baba', 'Muffin with liquor syrup in the sugar glaze',
                    285.0)
    drink_1 = Dish('Black tea', 'Indian leaf tea 600ml',
                   250.0)
    drink_2 = Dish('Coffe', 'Black Arabian coffee with milk 280ml',
                   75.0)
    desert_3 = Dish('Ice Cream', 'A ball of ice cream with syrup', 65.0)
    first_dish = Menu('First Dish')
    first_dish.add(first_dish_1)
    first_dish.add(first_dish_2)

    second_dish = Menu('Second Dish')
    second_dish.add(second_dish_1)
    second_dish.add(second_dish_2)

    deserts = Menu('Deserts')
    deserts.add(desert_1)
    deserts.add(desert_2)
    deserts.add(desert_3)

    drinks = Menu('Drinks')
    drinks.add(drink_1)
    drinks.add(drink_2)

    full_menu = Menu('Menu Bistro')
    full_menu.add(first_dish)
    full_menu.add(second_dish)
    full_menu.add(deserts)
    full_menu.add(drinks)

    print_menu(full_menu)
    drinks.remove(drink_1)
    print_menu(full_menu)
    drinks.remove(Dish("Some Item", "Some description", 100.0))

