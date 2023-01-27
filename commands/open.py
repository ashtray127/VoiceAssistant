import os

class Command:
    def __init__(self):
        self.data = {"name":"Open programs", "aliases":["open coding folder", 'open virtualbox', 'open opera']}
    
    def run(self, alias, args=None):
        if alias == "open coding folder":
            os.startfile("C:\\Users\\User\\Documents\\Coding")
        elif alias == "open virtualbox":
            os.startfile("C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe")
        elif alias == "open opera":
            os.startfile("C:\\Users\\User\\AppData\\Local\\Programs\\Opera\\launcher.exe")