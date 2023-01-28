import os
from time import sleep
import pyautogui

class Command:
    def __init__(self):
        self.data = {"name": "connect", 'aliases':['connect to pie', 'connect to pi', 'connect to server', 'connect to second server']}
    
    def run(self, alias, args=None):
        if alias==0 or alias==1:
            os.system("cmd.exe /c start cmd.exe /k ssh pi@192.168.1.29")
            sleep(1)
            pyautogui.typewrite('root')
            pyautogui.press('enter')
            return "Connecting to pi"
        elif alias==2:
            os.system("cmd.exe /c start cmd.exe /k ssh root@158.69.161.71")
            sleep(1)
            pyautogui.typewrite('n1rilxyi71bpzvi7rgjinm')
            pyautogui.press('enter')
            return "Connecting to server"
        elif alias==3:
            os.system("cmd.exe /c start cmd.exe /k ssh root@15.235.6.255")
            sleep(1)
            pyautogui.typewrite('449x1qyyhnp8krdcpymlxy')
            pyautogui.press('enter')
            return "Connecting to second server"
