from dataclasses import dataclass

@dataclass(frozen=True)
class Broker:
    id: int
    name: str
    client_id: str

@dataclass(frozen=True)
class Strategy:
    id: int
    name: str

class Order:
    def __init__(
        self, broker: Broker, instrument: str, strategy: Strategy, transaction: str, qty: int, price: int
        ):
        self.broker = broker
        self.intsrument = instrument
        self.strategy = strategy
        self.transaction = transaction
        self.qty = qty
        self.price = price


