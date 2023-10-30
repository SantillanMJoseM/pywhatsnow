import os
import pathlib
import time
from platform import system
from urllib.parse import quote
from webbrowser import open
import shutil
from pywhatsnow.core import const as cs

import requests
from pyautogui import click, hotkey, locateOnScreen, moveTo, press, size, typewrite

from pywhatsnow.core.exceptions import InternetException

WIDTH, HEIGHT = size()


def check_number(number: str) -> bool:
    """Comprueba el número para ver si contiene el código de país."""

    return "+" in number or "_" in number


def close_tab(wait_time: int = 2) -> None:
    """Cierra la pestaña del navegador actualmente abierta"""

    time.sleep(wait_time)
    if system().lower() in ("windows", "linux"):
        hotkey("ctrl", "w")
    elif system().lower() == "darwin":
        hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} No soportado!")
    press("enter")


def check_connection() -> None:
    """Verifique la conexión a Internet de la máquina host"""

    try:
        requests.get("https://google.com")
    except requests.RequestException:
        raise InternetException(
            "Error al conectarse a Internet. Asegúrate de estar conectado a Internet!"
        )


def _web(receiver: str, message: str) -> None:
    """Abre WhatsApp Web según el receptor"""
    if check_number(number=receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)


def send_message(message: str, receiver: str, wait_time: int) -> None:
    """Analiza y envía el mensaje"""

    _web(receiver=receiver, message=message)
    time.sleep(7)
    click(WIDTH / 2, HEIGHT / 2)
    time.sleep(wait_time - 7)
    if not check_number(number=receiver):
        for char in message:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    press("enter")
    time.sleep(7)
    press("enter")


def copy_image(path: str) -> None:
    """Copie la imagen al portapapeles según la plataforma"""

    if system().lower() == "linux":
        if pathlib.Path(path).suffix in (".PNG", ".png"):
            os.system(f"copyq copy image/png - < {path}")
        elif pathlib.Path(path).suffix in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            os.system(f"copyq copy image/jpeg - < {path}")
        else:
            raise Exception(
                f"El formato de archivo {pathlib.Path(path).suffix} no es compatible!"
            )
    elif system().lower() == "windows":
        from io import BytesIO

        import win32clipboard
        from PIL import Image

        image = Image.open(path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
    elif system().lower() == "darwin":
        if pathlib.Path(path).suffix in (".jpg", ".jpeg", ".JPG", ".JPEG"):
            os.system(
                f"osascript -e 'configura el portapapeles en (leer (archivo POSIX \"{path}\") como imagen JPEG)'"
            )
        else:
            raise Exception(
                f"El formato de archivo {pathlib.Path(path).suffix} no es compatible!"
            )
    else:
        raise Exception(f"Sistema no compatible: {system().lower()}")


def send_image(path: str, caption: str, receiver: str, wait_time: int) -> None:
    """Envía la imagen a un contacto o grupo según el receptor"""

    _web(message=caption, receiver=receiver)

    time.sleep(7)
    click(WIDTH / 2, HEIGHT / 2)
    time.sleep(wait_time - 7)
    copy_image(path=path)
    if not check_number(number=receiver):
        for char in caption:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    else:
        typewrite(" ")
    if system().lower() == "darwin":
        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")
    time.sleep(1)
    press("enter")
    time.sleep(1)
    press("enter")

def check_status ():
    """Revision de estado de numero telefonico valio o invalido whatsapp"""
   
def find_link():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\link.png")
    try:
        moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
        click()
    except Exception:
        location = locateOnScreen(f"{dir_path}\\data\\link2.png")
        moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
        print(location)
        click()   

def find_document():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    location = locateOnScreen(f"{dir_path}\\data\\document.png")
    print(location)
    moveTo(location[0] + location[2]/2, location[1] + location[3]/2)
    click()

def move_document_int(image):
    pathori = cs.pathori + '/' + image
    pathint = cs.pathint + '/' + image
    try:
        shutil.move(pathori, pathint)
    except:
        pass

def move_document_fin(image):
    pathint = cs.pathint + '/' + image
    pathfin = cs.pathfin + '/' + image

    try:
        shutil.move(pathint, pathfin)
    except:
        pass