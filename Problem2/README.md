# PROBLEM 2

## Build and Run the Docker Image

1. **Build the Docker Image**

   ```sh
   docker build -t problem2-image .

   ```

2. **Run the Docker Container**

   ```sh
   docker run -it --rm --name problem2-container -v "$(pwd)":/problem2 problem2-image
   ```

## Details

    The give solution contains 2 separate python files: generateCSV.py and anonymiseData.py
        1. generateCSV.py: will generate a csv file with dummy data and a defined number of rows that we want.
        2. anonymiseData.py: will utilise spark to anonymise the data of first_name, last_name and address columns.

## Explanation how this solution can work on larger dataset

    The given solution can be done on a larger dataset like 2GB and so on is because it ultisies the power of Spark:

    1. When read the dataset, Spark divides the file into smaller parts and processing them in parallel, each of them will be processes independently.
    2. Spark performs in-memory computation instead of disk I/O operation, which is much faster.
    3. Spark DataFrame's API uses columnar storage, which is efficient for data processing tasks like transformations and aggregations.

# Note:

    In order to test with a 2GB dataset or more, you might need to adjust the number of rows in the `gernateCSV.py` file to create a desired volume file
