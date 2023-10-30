import os
import time
import webbrowser as web
from platform import system
from typing import Optional

import requests
import wikipedia

from pywhatsnow.core import exceptions

if system().lower() in ("windows", "darwin"):
    from PIL import ImageGrab

    def take_screenshot(
        file_name: str = "pywhatsnow_screenshot", delay: int = 2, show: bool = True
    ) -> None:
        """Tomar captura de pantalla de la pantalla"""

        time.sleep(delay)
        screen = ImageGrab.grab()
        if show:
            screen.show(title=file_name)
        screen.save(f"{file_name}.png")


def web_screenshot(
    link: str,
    filename: str = "Screenshot.jpg",
    path: str = os.getcwd(),
    width: int = 1920,
    height: int = 1080,
) -> None:
    """Tomar captura de pantalla de la pantalla"""

    url = f"https://render-tron.appspot.com/screenshot/{link}/?width={width}&height={height}"
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(path, filename), "wb") as file:
            for chunk in response:
                file.write(chunk)


def show_history() -> None:
    """Imprime el archivo de registro generado por la biblioteca"""

    try:
        with open("PyWhatsNow_DB.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("El archivo de registro no existe!")
    else:
        if len(content) == 0:
            print("No hay registros en el archivo!")
        else:
            print(content)


def info(topic: str, lines: int = 3, return_value: bool = False) -> Optional[str]:
    """Da información sobre el tema."""

    data = wikipedia.summary(topic, sentences=lines)
    print(data)
    if return_value:
        return data


def playonyt(topic: str, use_api: bool = False, open_video: bool = True) -> str:
    """Reproducir un vídeo de YouTube"""

    if use_api:
        response = requests.get(
            f"https://pywhatsnow.herokuapp.com/playonyt?topic={topic}"
        )
        status_code = response.status_code
        if status_code == 200:
            if open_video:
                web.open(response.content.decode("ascii"))
            return response.content.decode("ascii")
        elif 400 <= status_code <= 599:
            raise exceptions.UnableToAccessApi(
                "No se puede acceder a la API de pywhatsnow en este momento"
            )
    else:
        url = f"https://www.youtube.com/results?q={topic}"
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == "WEB_PAGE_TYPE_WATCH":
                break
        if lst[count - 5] == "/results":
            raise Exception("No se encontró ningún vídeo para este tema!")

        if open_video:
            web.open(f"https://www.youtube.com{lst[count - 5]}")
        return f"https://www.youtube.com{lst[count - 5]}"


def search(topic: str) -> None:
    """Búsquedas sobre el tema en Google"""

    link = f"https://www.google.com/search?q={topic}"
    web.open(link)
