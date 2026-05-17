from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # checks input data
        #   if it is appropriate for the current data processor
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        # process the input data
        pass

    def output(self) -> tuple[int, str]:
        # outputs ingested data
        # is not overrided
        pass



# each spesialized class will need to override these methods
#   overriders of validate have the same signature as in DataProcessor
#   overiders of ingest have their own specific signatures to match the types they expect
#       if user doesn't validate the data before calling ingest, and data is invalid - raise exception
class NumericProcessor(DataProcessor):
    """
        ingests int, float and list of both(int, float, mixed)
        converts data into str and stores it internally,
        waiting to be extracted using the output method"""
    def __init__(self, data: int | float | list: Any):
        self.data = data
        self.string = None


    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False


    def ingest(self, data: int|float|list[int|float]) -> str:
        pass


class TextProcessor(DataProcessor):
    pass

class LogProcessor(DataProcessor):
    pass
