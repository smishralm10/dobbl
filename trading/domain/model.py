from dataclasses import dataclass

class Order:
    def __init__(
        self, broker: Broker, instrument: str, strategy: Strategy, transaction: str, qty: int, price: int
        ):
        self.broker = broker
        self.intsrument = instrument
        self.strategy = strategy
        self.transaction = transaction
        self._qty = qty
        self._price = price


