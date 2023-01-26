class Command:
    def __init__(self):
        self.data = {"name": "test", 'aliases':['testing', 'test .+']}
    
    def run(self, alias, args=None):
        print("Test complete")