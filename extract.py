import csv
import json
import xml.etree.ElementTree as ElementTree
import os


class Extractor:
    path: str = None
    data = []

    def __init__(self, path: str = os.getcwd()):
        print(path)
        abs_path = os.path.abspath(path)
        normal_path = os.path.normpath(abs_path)
        self.path = os.path.join(normal_path, 'input_files')

    def extract_data(self):
        readers = {
            '.csv': self._read_csv,
            '.json': self._read_json,
            '.xml': self._read_xml,
        }
        files = os.listdir(self.path)

        for file in files:
            filename, file_extension = os.path.splitext(file)
            filepath = os.path.join(self.path, file)
            readers[file_extension](filepath)

        return self.data

    def _read_csv(self, filepath: str):
        with open(filepath, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data.append(row)

    def _read_json(self, filepath: str):
        with open(filepath) as json_file:
            data = json.load(json_file)
            for row in data['fields']:
                self.data.append(row)

    def _read_xml(self, filepath: str):
        tree = ElementTree.parse(filepath)
        root = tree.getroot()

        for object_main_tag in root.findall('objects'):
            self._get_data_from_xml_row(object_main_tag)

    def _get_data_from_xml_row(self, object_main_tag: ElementTree.Element):
        data = dict()
        object_tag = object_main_tag.findall('object')

        for part in object_tag:
            data[part.attrib['name']] = part.find('value').text

        self.data.append(data)
