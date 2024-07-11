# PROBLEM 1

## Build and Run the Docker Image

1. **Build the Docker Image**

   ```sh
   docker build -t problem1-image .

   ```

2. **Run the Docker Container**

   ```sh
   docker run -it --rm --name problem1-container -v "$(pwd)":/problem1 problem1-image
   ```

# Data Validation

I generate an addition function to validate the data before processing with it.
The valid data doens't have Null value or empty string, and the number of age also need to make sense by making sure it's in the range 0 - 120.

I have added the sample data with invalid values, feels free to uncomment that and test it out.
