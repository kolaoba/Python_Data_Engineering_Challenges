import json
import os
import csv

# define helper function - flatten_json
def flatten_json(json_object):
    result = {}
    # write function to recursively flatten json
    def flatten(obj, name=''):
        # check for nested json
        if type(obj) is dict:
            for sub in obj:
                flatten(obj[sub], name + sub + '_')
        # check for nested arrays
        elif type(obj) is list:
            i = 0
            for sub in obj:
                flatten(sub, name + str(i) + '_')
                i += 1
        else:
            result[name[:-1]] = obj

    flatten(json_object)

    return result

# define helper function - convert_json_to_csv
def convert_json_to_csv(folder, file):

    # use context manager to read json file
    with open(f"{folder}/{file}", 'r') as json_file:
        # load json file
        json_obj = json.load(json_file)
        # flatten json file
        json_obj = flatten_json(json_obj)

        # create array of headers (keys)
        headers = [x for x in json_obj]
        # create array of records (values)
        records = [json_obj[x] for x in json_obj]

        # modify json filename to generate csv name
        csv_filename = file.replace('.json', '.csv')

        # use conntext manager to write data to csv file
        with open(f"{folder}/{csv_filename}", 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            # write headers first
            csv_writer.writerow(headers)
            #write records 
            csv_writer.writerow(records)