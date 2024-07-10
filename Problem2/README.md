# PROBLEM 1

## Build and Run the Docker Image

1. **Build the Docker Image**

   ```sh
   docker build -t problem2-image .

   ```

2. **Run the Docker Container**

   ```sh
   docker run -it --rm --name problem2-container -v "$(pwd)":/problem2 problem2-image
   ```
