from typing import List


class InvoiceLine(object):
    def __init__(self, net_value: int, description: str):
        self.description = description
        self.net_value = net_value

    def validate(self):
        pass


class Invoice:
    def __init__(self, number: str, lines: List[InvoiceLine]):
        self.number = number
        self.lines = lines
        self._total_net_value = None

    def validate(self):
        pass

    @property
    def total_net_value(self):
        return self._total_net_value

    @total_net_value.setter
    def total_net_value(self, value):
        pass