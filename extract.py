import csv
import json
import xml.etree.ElementTree as ElementTree


def read_csv(file_path_csv):
    with open(file_path_csv, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row)


def read_json(file_path_json):
    with open(file_path_json) as json_file:
        data = json.load(json_file)
        for row in data['fields']:
            print(row)


def read_xml(xml_file_path):
    tree = ElementTree.parse(xml_file_path)
    root = tree.getroot()

    for object_main_tag in root.findall('objects'):
        data = dict()
        object_tag = object_main_tag.findall('object')
        for part in object_tag:
            data[part.attrib['name']] = part.find('value').text
        print(data)
