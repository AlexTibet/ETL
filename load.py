import csv


def load_to_tsv(output_file_name, data: []):
    with open(output_file_name, 'w') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t', newline='\n')
        for row in data:
            writer.writerow(row)
