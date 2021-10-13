import csv


def get_fieldnames(data):
    fieldnames = []
    for row in data:
        for key in row.keys():
            fieldnames.append(key)
    return fieldnames


def load_to_tsv(output_file_name, data: []) -> bool:
    try:
        with open(output_file_name, 'wt') as tsv_file:
            fieldnames = get_fieldnames(data)
            writer = csv.DictWriter(tsv_file, fieldnames=fieldnames)

            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except Exception as err:
        print(err)
        return False
