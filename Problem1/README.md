# PROBLEM 1

## Build and Run the Docker Image

1. **Build the Docker Image**
   docker build -t problem1-image .

2. **Run the Docker Container**
   docker run -it --rm --name problem1-container -v "$(pwd)":/problem1 problem1-image
