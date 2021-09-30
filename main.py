import extract as ex

file_path_csv_one = "./input_files/csv_data_1.csv"
file_path_csv_two = "./input_files/csv_data_2.csv"
file_path_json = "./input_files/json_data.json"
file_path_xml = "./input_files/xml_data.xml"


if __name__ == '__main__':
    print('Hello world')
    ex.read_csv(file_path_csv_one)
    ex.read_csv(file_path_csv_two)
    ex.read_json(file_path_json)
    ex.read_xml(file_path_xml)
