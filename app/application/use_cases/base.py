from typing import Protocol


class BaseInteractor[Request, Response](Protocol):
    def __call__(self, request: Request) -> Response:
        raise NotImplementedError()