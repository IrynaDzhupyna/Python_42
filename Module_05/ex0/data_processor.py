from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self):
        self.storage: list[str] = []
        self.output_rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # checks input data
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        # process the input data
        pass

    def output(self) -> tuple[int, str]:
        # outputs ingested data
        #   extracts the oldest pieces of data along with their rank
        oldest_data = (self.storage, self.output_rank.pop(0))
        self.output_data += 1
        return oldest_data



# each spesialized class will need to override these methods
#   overriders of validate haive the same signature as in DataProcessor
#   overiders of ingest have their own specific signatures to match the types they expect
#       if user doesn't validate the data before calling ingest, and data is invalid - raise exception
class NumericProcessor(DataProcessor):
    """
        converts data into str and stores it internally,
        waiting to be extracted using the output method"""
    def __init__(self, data: int | float | list: Any):
        self.data = data

    def validate(self, data: Any) -> bool:
        # int, float and list of both types also mixed
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False


    def ingest(self, data: int|float|list[int|float]) ->  None:
        # converts the data into string
        if not self.validate(data):
            raise TypeError ("Expected int, float of list of these types")
        
        if isinstance(data, (int|float):
            self.storage.append(str(data))

        elif isinstance(data, list):
            for element in data:
                self.storage.append(str(element))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False


    def ingest(self, data: str | list[str,str]) -> list[str, str] | None:

        if not validate(data):
            raise TypeError("Expected str or list of strings")


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and all(isinstance(k, str)
            and isinstance(v, str) for k, v in data.item():
                return True
        if isinstance(data, list) and isinstance(data, dict)
            and isinstance(k, str) and isinstance(v, str) for k, v in data.item():
                return True
        return False

def main() -> None:
    num = NumericProcessor(5,

if __name__ == "__main__":
    main()
