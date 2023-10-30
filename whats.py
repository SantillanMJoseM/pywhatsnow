import time
import webbrowser as web
from datetime import datetime
from typing import Optional
from urllib.parse import quote
from re import fullmatch
import pyperclip
import paperclip

import os
import keyboard
import pyautogui as pg

from pywhatsnow.core import core, exceptions, log

pg.FAILSAFE = False

core.check_connection()


def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Enviar mensaje de WhatsApp al instante"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Falta el código de país en el número de teléfono!")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(4)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time - 4)
    pg.press("enter")
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    log.log_db(_time=time.localtime(), receiver=phone_no, path=' ', caption=' ', message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg(
    phone_no: str,
    message: str,
    time_hour: int,
    time_min: int,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Enviar un mensaje de WhatsApp a una hora determinada"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Falta el código de país en el número de teléfono!")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Formato de hora no válido!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "El tiempo de llamada debe ser mayor que el tiempo de espera, ya que WhatsApp Web tarda algo de tiempo en cargarse!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"En {sleep_time} Segundos se abrirá WhatsApp y después de {wait_time} Segundos se entregará el mensaje!"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=phone_no, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group(
    group_id: str,
    message: str,
    time_hour: int,
    time_min: int,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Enviar mensaje de WhatsApp a un grupo a una hora determinada"""

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Formato de hora no válido!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "El tiempo de llamada debe ser mayor que el tiempo de espera, ya que WhatsApp Web tarda algo de tiempo en cargarse!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"En {sleep_time} Segundos se abrirá WhatsApp y después de {wait_time} Segundos se entregará el mensaje!"
    )
    time.sleep(sleep_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatmsg_to_group_instantly(
    group_id: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
    sleep_time: int = 0
) -> None:
    """Enviar mensaje de WhatsApp a un grupo al instante"""

    current_time = time.localtime()

    time.sleep(sleep_time)
    core.send_message(message=message, receiver=group_id, wait_time=wait_time)
    log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhats_image(
    receiver: str,
    img_path: str,
    caption: str = "",
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Enviar imagen a un contacto o grupo de WhatsApp a una hora determinada"""

    if (not receiver.isalnum()) and (not core.check_number(number=receiver)):
        raise exceptions.CountryCodeException("Falta el código de país en el número de teléfono!")

    current_time = time.localtime()
    core.send_image(
        path=img_path, caption=caption, receiver=receiver, wait_time=wait_time
    )
    log.log_image(_time=current_time, path=img_path, receiver=receiver, caption=caption)
    log.log_db(_time=time.localtime(), receiver=receiver, path=img_path, caption=caption, message=' ')
    if tab_close:
        core.close_tab(wait_time=close_time)


def sendwhatdoc_immediately(
    phone_no: str,
    image: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Enviar mensaje de WhatsApp al instante"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Falta el código de país en el número de teléfono!")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(4)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time - 4)
    core.move_document_int(image)
    pg.moveTo(228, 206)
    pg.mouseDown()
    pg.click(228, 206)
    pg.mouseUp()
    time.sleep(2)
    pg.dragTo(1645,456,duration=1.5)
    time.sleep(1)
    pg.press("enter")
    pg.press("enter")
    core.move_document_fin(image)
    if tab_close:
        core.close_tab(wait_time=close_time)  


def open_web() -> bool:
    """Abre WhatsApp Web"""

    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True
