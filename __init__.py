# Version 1.0
# Status: (Release)
# Documentation: ....


__VERSION__ = "Version 1.3 (Stable)"

from platform import system

from pywhatsnow.ascii_art import image_to_ascii_art
from pywhatsnow.handwriting import text_to_handwriting
from pywhatsnow.mail import send_hmail, send_mail
from pywhatsnow.misc import info, playonyt, search, show_history, web_screenshot
from pywhatsnow.sc import cancel_shutdown, shutdown
from pywhatsnow.whats import (
    open_web,
    sendwhatmsg,
    sendwhatmsg_instantly,
    sendwhatmsg_to_group,
    sendwhatmsg_to_group_instantly,
    sendwhats_image,
    sendwhatdoc_immediately,
)

if system().lower() in ("darwin", "windows"):
    from pywhatsnow.misc import take_screenshot

if system().lower() == "windows":
    from pywhatsnow.remotekit import start_server
