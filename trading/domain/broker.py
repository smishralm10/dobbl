class Broker:
    def __init__(self, name: str, client_id: str, api_key: str):
        self.name = name
        self._client_id = client_id
        self._api_key = api_key
    
    def __repr__(self):
        return f'<Broker {self.name}>'
    
    