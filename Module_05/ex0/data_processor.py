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
        oldest_data = (self.output_rank, self.strage.pop(0))
        self.output_rank += 1
        return oldest_data


class NumericProcessor(DataProcessor):
    """
        converts data into str and stores it internally,
        waiting to be extracted using the output method

        resives data via ingest
        """

    def validate(self, data: Any) -> bool:
        # int, float and list of both types also mixed
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False


    def ingest(self, data: int|float|list[int|float]) ->  None:
        # converts int/float/list[int|float] into string
        if not self.validate(data):
            raise TypeError ("Expected int, float of list of these types")
        
        if isinstance(data, (int, float)):
            self.storage.append(str(data))

        elif isinstance(data, list):
            for element in data:
                self.storage.append(str(element))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        # str or list[str]
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False


    def ingest(self, data: str | list[str]) -> None:
        # stores str or list(str)
        if not self.validate(data):
            raise TypeError("Expected str or list of strings")

        if isinstance(data, str):
            self.storage.append(data)

        elif isinstance(data, list):
            for element in data:
                self.storage.append(element)


class LogProcessor(DataProcessor):
    """ dict[str, str], list[dict[str,str] """

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str) for k, v in data.item())
        if isinstance(data, list):
            return all(self.validate(element) for element in data)
        return False


    def ingest(self, data: dict[str, str]|list(dict[str, str]))-> None:
        # to str
        if not self.validate(data):
            raise TypeError("Expected dict of str key-value pairs, or list of that type")
        
        if isinstance(data, dict):
            self.stored.append(str(data))

        elif isinstance(data, list):
            new = ''.join([str(element) for element in data])



def main() -> None:
    num = NumericProcessor(5,

if __name__ == "__main__":
    main()
