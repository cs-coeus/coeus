from typing import Generic, TypeVar

I = TypeVar('I')
O = TypeVar('O')


class ModelInterface(Generic[I, O]):

    @staticmethod
    def predict(input: I) -> O:
        pass
