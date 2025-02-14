import csv

#Maximum accepted age
MAX_AGE = 120
#Minimum accepted age
MIN_AGE = 0

# Function to validate the data before processing
def validate_data(data):
    valid_data = []
    invalid_data = []

    for record in data:
        # parse the data in record
        first_name, last_name, age = record
        # Check for null or empty strings
        if not first_name or not last_name or not age:
            invalid_data.append(record)
            continue
        
        # Check if age is a valid number and within range
        try:
            age = int(age)
            if age < MIN_AGE or age > MAX_AGE:
                invalid_data.append(record)
                continue
        except ValueError:
            invalid_data.append(record)
            continue
        
        valid_data.append(record)
    
    # Write invalid records to a separate CSV file
    with open('invalid_data.csv', 'w', newline='') as invalid_file:
        writer = csv.writer(invalid_file)
        writer.writerow(['first_name', 'last_name', 'age'])
        writer.writerows(invalid_data)
    
    return valid_data

# Function to generate a fixed-width file according to the "spec"
def generate_fixed_width_file(data, spec, output_file):

    # Validate the data, only use data that is valid
    data = validate_data(data)

    #An array to store values from data that have combined with fixed-width values
    fixed_width_lines = []

    """
    Loop through each record in the data, generate a fixed-width record and save them into an array:
        [length for _, length in spec]: Extract the "length" value after 
                iterating over "spec" and getting their value, 
                "_" holds the field_name, "length" holds the width value.
            The return value is (10,10,3)

        zip(record, [length for _, length in spec]): Combines the values of the record with their respective lengths.
            Exp: when record=("John", "Doe", "23"), zip return [("John", 10), ("Doe", 10), ("23",3)]

        for field, width in zip(record, [length for _, length in spec])]: 
            Iterates through the zipped list, "field" holds value of the first element, "width" holds the second.

        str(field)[:width]: Truncates the value of "field" by the length of "width".

        str(field)[:width].ljust(width): ljust() function fills the remaining space (if any) with blank spaces.

        fixed_width_lines.append(line): Save the new line into array fixed_width_lines array.
    """
    for record in data:
        line = ''.join([str(field)[:width].ljust(width) for field, width in zip(record, [length for _, length in spec])])
        fixed_width_lines.append(line)


    """
        Open the output_file with "write" permission.
        Loop through each line in the fixed_width_lines array and write them into the output_file
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in fixed_width_lines:
            # "\n": Adds a line break after each line
            f.write(line + '\n')


# Function to parse the fixed-width-file to generate a csv file
def parse_fixed_width_file(input_file, output_file, spec):
    # Open the input_file with 'read' permission, inputfile is an object of input_file
    # Open the output_file with 'write' permission, outputfile is an object of output_file
    with open(input_file, 'r', encoding='utf-8') as inputfile, open(output_file, 'w', newline='',encoding='utf-8') as outputfile:
        # Create a CSV writer object to write to the output_file 
        writer = csv.writer(outputfile)

        # Write the header row into output_file
        # [field for field, _ in spec] returns the field_name from spec (first_name,last_name,age)
        writer.writerow([field for field, _ in spec])
        
        # Loop through each line in the input file
        for line in inputfile:
            # Create an empty array to store for each parsed record.
            record = []
            # Create a starting position 
            start = 0
            # Loop through each "field" and "width" defined in the spec
            for field, width in spec:
                # Extract the substring from 'line' starting at 'start' position with 'width' length 
                # and save into record array
                # .strip() function removes any remaining whitespace
                record.append(line[start:start + width].strip())
                # Move the start position to the end of the current field
                start += width

            # Write the parsed record as a row in the output CSV file    
            writer.writerow(record)


if __name__ == "__main__":

    #The given spec illustrates the field name (column name) with its fixed width
    # Exp: field name of 'first_name' will have a max width of 10
    spec = [('first_name', 10), ('last_name', 10), ('age', 3)]

    #Sample data 
    data = [
        ("John", "Doe", "23"),
        ("Jane", "Smith", "30"),
        ("Albert", "Einstein", "76"),
        ("Thái", "An", "29"),
        ("爱", "希望", "102")
    ]

    # Sample data with invalid values
    # Uncomment to test it out
    # data = [
    #     ("John", "Doe", "23"),
    #     ("Jane", "Smith", "30"),
    #     ("Albert", "Einstein", "76"),
    #     ("", "An", "29"),
    #     ("爱", "希望", "190"),
    # ]
    
    #Call the function to generate the fixed-width file
    #Pass the name of the fixed-width file we want into the function
    generate_fixed_width_file(data, spec, 'fixed_width_file.txt')

    # Call the function to parse the fixed-width file and generate a CSV file
    parse_fixed_width_file('fixed_width_file.txt', 'output.csv', spec)
