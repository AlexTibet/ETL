import csv
import json
import xml.etree.ElementTree as ElementTree
from typing import TextIO, NoReturn
from abc import ABC


class Reader(ABC):
    data = []

    def get_data(self, file_path):
        pass

    def _parse_file(self, file):
        pass


class CSVReader(Reader):

    def get_data(self, file_path: str) -> [dict]:
        with open(file_path, 'r') as csv_file:
            self._parse_file(csv_file)
        return self.data

    def _parse_file(self, file: TextIO) -> NoReturn:
        reader = csv.DictReader(file)
        for row in reader:
            self.data.append(row)


class JSONReader(Reader):

    def get_data(self, file_path: str) -> [dict]:
        with open(file_path) as json_file:
            self._parse_file(json_file)
        return self.data

    def _parse_file(self, file: TextIO) -> NoReturn:
        data = json.load(file)
        for row in data['fields']:
            self.data.append(row)


class XLSReader(Reader):

    def get_data(self, file_path: str) -> [dict]:
        tree = ElementTree.parse(file_path)
        root = tree.getroot()

        for object_main_tag in root.findall('objects'):
            self._parse_main_tag(object_main_tag)

        return self.data

    def _parse_main_tag(self, object_main_tag: ElementTree.Element) -> NoReturn:
        row = dict()
        object_tag = object_main_tag.findall('object')

        for part in object_tag:
            row[part.attrib['name']] = part.find('value').text

        self.data.append(row)
