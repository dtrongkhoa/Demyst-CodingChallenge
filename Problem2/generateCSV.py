import csv
import random
import datetime


def generate_csv(file_name, num_records):

    # Sample data
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown"]
    addresses = ["123 Main St", "456 Maple Ave", "789 Elm St", "101 Oak St", "202 Pine St"]

    # Open the file with "write" permission
    with open(file_name, mode='w', newline='') as file:
        # Generate a csv writer object
        writer = csv.writer(file)
        # Write the header columns into the csv file
        writer.writerow(["first_name", "last_name", "address", "date_of_birth"])

       # This For Loop will loop through the list of sample data, randomly
       # pick the values in there and write into the csv until the number row
       # are matched with the number we want.
        for _ in range(num_records):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            address = random.choice(addresses)
            date_of_birth = datetime.date(1990, 1, 1) + datetime.timedelta(days=random.randint(0, 10000))
            writer.writerow([first_name, last_name, address, date_of_birth])

            
if __name__ == "__main__":
    # The first argument is the csv file name
    # The second argument is the number of row that we want to generate``
    generate_csv('data.csv', 1000000)  # Adjust the number of records as needed
