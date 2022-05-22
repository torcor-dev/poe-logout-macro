from pynput.mouse import Listener
from libqtile.command.client import InteractiveCommandClient
import subprocess
import time

POE_WIN_NAME = "Path of Exile"

def on_click(x, y, button, pressed):
    c = InteractiveCommandClient()
    focused_win = c.group.info()['focus']

    if focused_win != POE_WIN_NAME:
        return

    if button.name == 'button8' and pressed:
        logout()
        print('logout')

def logout():
    enable = "sudo iptables -I INPUT -p tcp --sport 6112 --tcp-flags PSH,ACK PSH,ACK -j REJECT --reject-with tcp-reset;"

    disable = "sudo iptables -D INPUT -p tcp --sport 6112 --tcp-flags PSH,ACK PSH,ACK -j REJECT --reject-with tcp-reset;"
    subprocess.Popen(enable, shell=True)
    time.sleep(1)
    subprocess.Popen(disable, shell=True)

    

with Listener(on_click=on_click) as listener:
    listener.join()
