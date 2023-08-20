
import csv
import pickle

'''
table_data = [
    ["Table 1", "1", "9:00-12:00"],
    ["Table 2", "2", "12:00-15:00"],
    ["Table 3", "3", "15:00-18:00"],
    ["Table 4", "4", "9:00-12:00"],
    ["Table 5", "5", "18:00-21:00"],
    ["Table 6", "6", "21:00-22:30"]
]


def write_table_data_to_csv(table_data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table_data)
    print(f"Data written to {filename} successfully.")


write_table_data_to_csv(table_data,'table_data.csv')
'''

def read_pickle_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Load the pickled data from the file
            data = pickle.load(file)

            # Return the data or perform further operations
            return data
    except IOError:
        print(f"Error: Unable to read file '{file_path}'")

print(read_pickle_file('sorted_array.bin'))


