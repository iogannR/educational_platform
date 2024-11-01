from typing import Protocol


class BaseJWTTokenAdapter(Protocol):
    
    @classmethod
    def encode_jwt(cls, payload: dict, key: str, algoritm: str) -> str:
        raise NotImplementedError()
    
    @classmethod
    def decode_jwt(cls, token: str, key: str, algoritms: list[str]) -> dict:
        raise NotImplementedError()