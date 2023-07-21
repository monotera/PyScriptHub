# CSV Processing Application

This is a CSV processing application built with Flask, Docker, and Celery. It provides an API endpoint to upload CSV files, process them asynchronously, and retrieve the processed results.

The application consists of several components:

1. **docker-compose.yml**: Defines a Docker Compose configuration that sets up the application services, including the Flask application, Redis message broker, and Celery worker.

2. **Dockerfile**: Contains the instructions to build a Docker image for the Flask application.

3. **app.py**: Implements the Flask application with two routes: `/api/upload` for uploading CSV files and `/api/result/<task_id>` for retrieving the processed results.

4. **csv_controller.py**: Contains the `process_csv` function responsible for processing the CSV file, aggregating the data, and writing the results to an output file.

5. **celery_worker.py**: Sets up a Celery worker and defines the `process_csv_task` task that asynchronously executes the `process_csv` function.

## Getting Started

To run the CSV processing application, follow these steps:

1. Install Docker and Docker Compose on your system.

2. Clone this repository to your local machine.

3. Build the Docker image and start the services by running the following command in the project directory:

   ```
   docker-compose up --build
   ```

4. The application will be accessible at `http://localhost:5000`. You can use tools like cURL or Postman to interact with the API endpoints.

## Usage

- **Uploading a CSV file**: Send a POST request to `http://localhost:5000/api/upload` with a `csvFile` field containing the CSV file to be processed. For example, you can use the provided `smallTest.csv` or `bigTest.csv` file.

  Example using cURL:
  ```
  curl -F "csvFile=@smallTest.csv" http://localhost:5000/api/upload
  ```

- **Retrieving processed results**: Send a GET request to `http://localhost:5000/api/result/<task_id>`, where `<task_id>` is the ID returned when uploading the CSV file. The response will contain the processed results as a downloadable CSV file.

  Example using cURL:
  ```
  curl http://localhost:5000/api/result/<task_id> --output result.csv
  ```

Please note that `<task_id>` should be replaced with the actual task ID returned when uploading the CSV file. The processed results will be downloaded and saved as `result.csv` in the current directory.

## Dependencies

The application relies on the following dependencies:

- Flask: Web framework for building the API endpoints.
- Celery: Distributed task queue system for asynchronous processing.
- Redis: Message broker and backend for Celery.
- Dask: Parallel computing library for handling large-scale CSV processing.

Please ensure that the necessary dependencies are installed and configured correctly.

## Author

This CSV processing application was developed by [Nelson Mosquera](https://github.com/monotera).

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore, modify, and use this CSV processing application according to your needs.

If you encounter any issues or have suggestions for improvements, please don't hesitate to open an issue or submit a pull request. Contributions are welcome!

Happy CSV processing!