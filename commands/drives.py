import ctypes
import itertools
import os
import string
import platform



class Command:
    def __init__(self):
        self.data = {"name": "Check that all the drives are there", 'aliases':['check drives', 'check drive .+', 'what drives are available']}
    
    def run(self, alias, args=None):
        if alias==0:
            message = ""
            failed = False
            try: os.listdir('C:\\')
            except Exception: message += "The C drive is not available. "; failed = True

            try: os.listdir('E:\\')
            except Exception: message += "The E drive is not available. "; failed = True

            try: os.listdir('F:\\')
            except Exception: message += "The F drive is not available. "; failed = True

            try: os.listdir('G:\\')
            except Exception: message += "The G drive is not available. "; failed = True

            if failed:
                return message 
            else:
                return "All storage drives are available."
        elif alias==1:
            if args==None: return "Please specify a drive to check."
            try: os.listdir(args + ":\\")
            except Exception: return "The " + args + " drive is not available."
            return "The " + args + " drive is available."
        elif alias==2:
            message = ""
            for drive in string.ascii_uppercase:
                try: os.listdir(drive + ":\\")
                except Exception: 2+2
                else: message += "The " + drive + " drive is available. "
            return message


            