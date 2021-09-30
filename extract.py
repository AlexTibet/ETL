import csv
import json


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
