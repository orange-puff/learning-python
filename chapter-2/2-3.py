import csv

def capitalize(name):
    # strings are immutable, so we are creating a list of characters that we can mutate
    to_ret = list(name)

    # if the first letter is lower case, make it upper case
    if ord(to_ret[0]) >= ord('a') and ord(to_ret[0]) <= ord('z'):
        to_ret[0] = chr(ord(to_ret[0]) - ord('a') + ord('A'))

    # we are joining the characters of to_ret on an empty string. Test this method out by calling it on different strings
    # i.e. '-'.join(['a', 'b', 'c']) = 'a-b-c'
    return ''.join(to_ret)

def read_csv(file_name):
    to_ret = []
    with open(file_name) as file:
        csv_file = csv.reader(file)

        for line in csv_file:
            to_ret.append(line)

    return to_ret

def print_data(file_name):
    data = read_csv(file_name)
    for line in data:
        print(line)

def write_csv(file_name, output_file_name):
    data = read_csv(file_name)
    with open(output_file_name, 'w') as file:
        csv_file = csv.writer(file)

        for row in data:
            # capitalize if this is not the first row
            if row != data[0]:
                # capitalize the first and last name
                row[0] = capitalize(row[0])
                row[1] = capitalize(row[1])

            csv_file.writerow(row)

if __name__=='__main__':
    print_data('data_csv.csv')
    write_csv('data_csv.csv', 'new_data_csv.csv')