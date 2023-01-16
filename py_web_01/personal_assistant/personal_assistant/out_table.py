from tabulate import tabulate
from abc import ABC, abstractmethod


class CLIBotInterface(ABC):
    @abstractmethod
    def show_all_info(self):
        pass


class BotInfo(CLIBotInterface):
    table_format = 'pipe'
    table_showindex = 'always'

    def __init__(self, data, headers):
        self.data = data
        self.headers = headers

    def show_all_info(self):
        print(tabulate(self.data, headers=self.headers, tablefmt=self.table_format, showindex=self.table_showindex))
