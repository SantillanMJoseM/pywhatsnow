import os
import time
import pyodbc
from datetime import datetime

from pywhatsnow.core.core import check_number
from pywhatsnow.core.core import check_status


def format_message(message: str) -> str:
    """Formatea el mensaje para eliminar espacios redundantes y caracteres de nueva línea"""
    msg_l = message.split(" ")
    new = []
    for x in msg_l:
        if "\n" in x:
            x = x.replace("\n", "")
            new.append(x) if not len(x) == 0 else None

        elif len(x) != 0:
            new.append(x)

    return " ".join(new)


def log_message(_time: time.struct_time, receiver: str, message: str) -> None:
    """Registra la información del mensaje después de enviarlo"""

    if not os.path.exists("PyWhatsNow_DB.txt"):
        file = open("PyWhatsNow_DB.txt", "w+")
        file.close()


    with open("PyWhatsNow_DB.txt", "a", encoding="utf-8") as file:
        if check_number(receiver):
            file.write(
                f"Fecha: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nHora: {_time.tm_hour}:{_time.tm_min}\n"
                f"Telefono: {receiver}\nMensaje: {message}"
            )
        else:
            file.write(
                f"Fecha: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nHora: {_time.tm_hour}:{_time.tm_min}\n"
                f"Group ID: {receiver}\nMensaje: {message}"
            )
        file.write("\n--------------------\n")
        file.close()


def log_image(_time: time.struct_time, path: str, receiver: str, caption: str) -> None:
    """Registra la información de la imagen después de enviarla"""

    if not os.path.exists("PyWhatsNow_DB.txt"):
        file = open("PyWhatsNow_DB.txt", "w+")
        file.close()

    caption = format_message(caption)

    with open("PyWhatsNow_DB.txt", "a", encoding="utf-8") as file:
        if check_number(number=receiver):
            file.write(
                f"Fecha: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nHora: {_time.tm_hour}:{_time.tm_min}\n"
                f"Telefono: {receiver}\nImage: {path}\nPie: {caption}"
            )

        else:
            file.write(
                f"Fecha: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nHora: {_time.tm_hour}:{_time.tm_min}\n"
                f"Group ID: {receiver}\nImage: {path}\nPie: {caption}"
            )
        file.write("\n--------------------\n")
        file.close()

def log_db(_time: time.struct_time, receiver: str, path: str, caption: str, message: str) -> None:
    """Genera log DB"""
    from pywhatsnow.core import const
    #--- Generar Coneccion a base de datos--#
    #--- Se difine coneccion en archivo fijo dentro del core ---#
    try: 
        conexion=pyodbc.connect('DRIVER={SQL SERVER}; SERVER='+const.server+';DATABASE='+const.bd+';UID='+const.user+';PWD='+const.contra)
    except:
        pass
    
    status = 1 #check_status() 
    cursor = conexion.cursor()
    cursorinsert = conexion.cursor()
    
    consulta = "insert into TestWhatsApp(Fecha, Telefono, Imagen, Caption, Mensaje, status) values (?,?,?,?,?,?)"
    #cursorinsert.execute(consulta,datetime.today(),{receiver},{path},{caption},{message})
    cursorinsert.execute(consulta,datetime.today(),str({receiver}),str(path),str(caption),str(message), status)
    cursorinsert.commit()
    cursorinsert.close()
    cursor.close
    conexion.close
