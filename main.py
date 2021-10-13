from extract import Extractor
import os
from load import load_to_tsv


if __name__ == '__main__':
    print('Hello world')
    extractor = Extractor()
    data = extractor.get_data()
    print(data)
    load_to_tsv('test_output.tsv', data)

