import os
from extract.readers import CSVReader, JSONReader, XLSReader, Reader
from typing import Type, NoReturn


class Extractor:
    path: str
    data: list
    _readers: dict[str, Type[Reader]]
    default_path = os.path.join(os.getcwd(), 'input_files')

    def __init__(self, path: str = default_path):
        self.path = path
        self.data = []
        self._readers = {
            '.csv': CSVReader,
            '.json': JSONReader,
            '.xml': XLSReader,
        }

    def get_data(self, path: str = default_path) -> [dict]:
        files: list = os.listdir(path)

        for file in files:
            self._extract_data(file, path)

        return self.data

    def _extract_data(self, file: str, path: str) -> NoReturn:
        filename, file_extension = os.path.splitext(file)
        filepath = os.path.join(path, file)

        reader = self._readers[file_extension]()
        self.data.extend(reader.get_data(filepath))

