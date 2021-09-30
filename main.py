import extract as ex

file_path_csv_one = "ETL/input_files/csv_data_1.csv"
file_path_csv_two = "ETL/input_files/csv_data_2.csv"

file_path_json = "ETL/input_files/json_data.json"


if __name__ == '__main__':
    print('Hello world')
    ex.read_csv(file_path_csv_one)
    ex.read_csv(file_path_csv_two)
    ex.read_json(file_path_json)
