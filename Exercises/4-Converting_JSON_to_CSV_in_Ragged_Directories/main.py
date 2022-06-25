import json
import os
import csv
from helper_package.helper_functions import convert_json_to_csv




def main():
    # declare data file path
    DATA_PATH = "./data/"

    # os.walk through the ragged directories for json files
    for root, dirs, files in os.walk(DATA_PATH):
        # loop through files
        for file in files:
            # check for json file
            if(file.endswith('.json')):
                convert_json_to_csv(root, file)





if __name__ == '__main__':
    main()
