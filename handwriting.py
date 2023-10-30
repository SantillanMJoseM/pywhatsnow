import requests

from pywhatsnow.core import exceptions


def text_to_handwriting(
    string: str, save_to: str = "pywhatsnow.png", rgb: tuple = (0, 0, 0)
) -> None:
    """Convierta la cadena dada en caracteres escritos a mano"""

    data = requests.get(
        f"https://pywhatkit.herokuapp.com/handwriting?text={string}&rgb={rgb[0]},{rgb[1]},{rgb[2]}"
    )
    status_code = (
        data.status_code
    )  # source = https://www.geeksforgeeks.org/http-status-codes-successful-responses/
    if status_code == 200:
        with open(save_to, "wb") as file:
            file.write(data.content)
            file.close()
    elif 400 <= status_code <= 599:
        raise exceptions.UnableToAccessApi("No se puede acceder a la API de Pywhatsnow en este momento")
