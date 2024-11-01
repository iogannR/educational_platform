from typing import Protocol


class BasePasswordHashAdapter(Protocol):
    
    @classmethod
    def hash_password(password: str) -> str:
        raise NotImplementedError()
    
    @classmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        raise NotImplementedError()