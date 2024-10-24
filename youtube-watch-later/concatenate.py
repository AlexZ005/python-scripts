import re
import csv

def process_file(input_file, target_numbers):
    csvfile = 'output.csv'
    with open(csvfile, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        with open(input_file, 'r', encoding='utf-8') as file:
            time = []
            result = []
            current_number = 1
            for line in file:
                stripped_line = line.strip()
                if stripped_line != str(current_number+1):
                    # Get the row which contains the time and save it, if exists
                    if re.match(r'^(\d{1,2}):?(\d{1,2})?:?(\d{1,2})$', stripped_line):
                        time=stripped_line
                    else:
                        if stripped_line:
                            if stripped_line != 'Now playing':
                                result.append(stripped_line)
                else:
                    current_number += 1
                    result.insert(1,time)
                    print(result)
                    writer.writerow(result)
                    # Cleanup for the next video
                    time = []
                    result = []
                    result.append(current_number)
        result.insert(1,time)
        print(result)
        writer.writerow(result)
    return
input_file = 'input.txt'
target_numbers = [1, 2, 3]
output = process_file(input_file, target_numbers)