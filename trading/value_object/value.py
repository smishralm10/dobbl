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