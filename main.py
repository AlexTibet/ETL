import extract as ex
import os


file_path_csv_one = "./input_files/csv_data_1.csv"
file_path_csv_two = "./input_files/csv_data_2.csv"
file_path_json = "./input_files/json_data.json"
file_path_xml = "./input_files/xml_data.xml"


if __name__ == '__main__':
    print('Hello world')
    # csv_one = ex.read_csv(file_path_csv_one)
    # csv_two = ex.read_csv(file_path_csv_two)
    # json_data = ex.read_json(file_path_json)
    # xml_data = ex.read_xml(file_path_xml)

    # extract_data = [*csv_one, *csv_two, *json_data, *xml_data]
    # print(extract_data)

    extractor = ex.Extractor()
    data = extractor.extract_data()
    print(data)

