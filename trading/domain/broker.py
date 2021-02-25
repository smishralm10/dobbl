class Broker:
    def __init__(self, name: str, client_id: str, api_key: str):
        self._name = name
        self._client_id = client_id
        self._api_key = api_key
    
    def __repr__(self):
        return f'<Broker {self.name}>'
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def client_id(self) -> str:
        return self._client_id
    