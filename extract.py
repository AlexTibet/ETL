import os
from readers import CSVReader, JSONReader, XLSReader, Reader
from typing import Type


class Extractor:
    path: str
    data: list
    _readers: dict[str, Type[Reader]]

    def __init__(self, path: str = os.getcwd()):
        self.path = os.path.join(path, 'input_files')
        self.data = []
        self._readers = {
            '.csv': CSVReader,
            '.json': JSONReader,
            '.xml': XLSReader,
        }

    def extract_data(self) -> [dict]:
        files = os.listdir(self.path)

        for file in files:
            filename, file_extension = os.path.splitext(file)
            filepath = os.path.join(self.path, file)

            reader = self._readers[file_extension]()
            self.data.extend(reader.get_data(filepath))

        return self.data
