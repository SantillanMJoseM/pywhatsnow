import os
import platform

try:
    import winerror
except ImportError or ModuleNotFoundError:
    pass

osname = platform.system()


def shutdown(time: int = 20) -> None:
    """Programa un apagado después del tiempo especificado"""

    if "window" in osname.lower():
        cont = f"shutdown -s -t {time}"
        error_code = os.system(cont)
        if error_code in [winerror.ERROR_SHUTDOWN_IN_PROGRESS, 1115]:
            print("Ya se ha programado un proceso de cierre!")
        else:
            print(f"Su sistema se apagará en {time} segundos!")

    elif "linux" in osname.lower():
        cont = f"shutdown -h {time}"
        os.system(cont)
        print(f"Su sistema se apagará en {time} minutos!")

    elif "darwin" in osname.lower():
        cont = f"shutdown -h -t {time}"
        os.system(cont)
        print(f"Su sistema se apagará en {time} minutos!")

    else:
        raise Warning(
            f"Disponible solo en Windows, Mac y Linux, no se puede ejecutar en {osname}"
        )


def cancel_shutdown() -> None:
    """Cancela el apagado programado"""

    if "window" in osname.lower():
        error_code = os.system("shutdown /a")
        if error_code == winerror.ERROR_NO_SHUTDOWN_IN_PROGRESS:
            print(
                "¡El proceso de cancelación de apagado ha sido cancelado! [NO hay apagado programado]"
            )
        else:
            print("El apagado ha sido cancelado!")

    elif "linux" in osname.lower():
        os.system("shutdown -c")
        print("El apagado ha sido cancelado!")

    elif "darwin" in osname.lower():
        os.system("killall shutdown")
        print("El apagado ha sido cancelado!")

    else:
        raise Warning(
            f"Disponible solo en Windows, Mac y Linux, no se puede ejecutar en {osname}"
        )
