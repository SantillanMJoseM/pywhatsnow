class CountryCodeException(Exception):
    """
    El código de país no está presente en el número de teléfono
    """
    pass


class CallTimeException(Exception):
    """
    El tiempo de espera es demasiado corto para que se abra WhatsApp Web
    """
    pass


class InternetException(Exception):
    """
    La máquina host no está conectada a Internet o la velocidad de conexión es lenta
    """
    pass


class UnsupportedEmailProvider(Exception):
    """
    El proveedor de correo electrónico utilizado para enviar el correo electrónico no es compatible
    """
    pass


class UnableToAccessApi(Exception):
    """
    No se puede acceder a la API de pywhatsnow
    """
    pass
