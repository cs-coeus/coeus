from typing import Generic, TypeVar

I = TypeVar('I')
O = TypeVar('O')


class DataRepository(Generic[I, O]):

    @staticmethod
    def getData(input: I) -> O:
        pass
