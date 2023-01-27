import os
import ctypes

class Command:
    def __init__(self):
        self.data = {"name": "shutdown", 'aliases':['shutdown', 'restart', 'lock', 'switch user']}
    
    def run(self, alias, args=None):
        if alias == 0:
            os.system("shutdown /s /t 0")
        elif alias == 1:
            os.system("shutdown /r /t 0")
        elif alias == 2:
            ctypes.windll.user32.LockWorkStation()
        elif alias == 3:
            os.system("shutdown /l")