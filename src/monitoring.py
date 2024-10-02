from src.bus import *
from src.city import *
from src.depot import *
from src.route import *


class Monitoring:
    class Commands:
        def search(self, *args, **kwargs) -> str:
            city: City = kwargs['city']
            
            return 'temp'
            
    def __init__(self) -> None:
        self.cmd_symbol = '$: '
        self.response = str()
        self.city = City('Tashkent')
    
    def prompt_args(self) -> list[str]:
        return input(self.cmd_symbol).split(' ')
    
    
    def eval_command(self, *args, **kwargs) -> str:
        return eval(args[0])(*args[1:], **kwargs)
    
    def run(self) -> None:
        while True:
            args = self.prompt_args()
            
            self.response += ''
            