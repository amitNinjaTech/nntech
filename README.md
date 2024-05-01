# To run this app 

Method 1 - as docker container

docker build -t app .

# This command will build the Docker image based on the instructions in the Dockerfile. Replace app with your desired image name.

docker run -p 5000:5000 app

Method 2 - directly as python app 

python3 app.py

# About the App

# Date Range Search Web App

This Flask web application allows users to search for events between a custom start and end date. The application fetches data from an external API based on the selected date range and displays the results to the user.

## Files

### app.py

The `app.py` file contains the backend logic of the Flask application. Here's a breakdown of the key parts of the code:

- **Flask Setup**: The Flask application is created and initialized.

- **Routes**:
  - **`/` route**: Renders the `index.html` template. This template contains a form for users to input custom start and end dates.
  - **`/data` route (POST)**: Handles the form submission. It retrieves data from the external API based on the provided date range and returns the formatted data as a JSON response.

- **Functions**:
  - **`index` function**: Renders the `index.html` template.
  - **`get_data` function**: Handles the form submission, retrieves data from the external API, and formats the data according to the OpenAPI specification.

### openapi/spec.yaml

The `spec.yaml` file defines the OpenAPI specification for the API endpoint `/data`. This specification specifies the expected request format and the structure of the response data. Here's an overview of the contents:
- **OpenAPI Version**: The version of the OpenAPI specification used (3.0.0).
- **Info**: Metadata about the API such as title and version.
- **Paths**:
  - **`/data` endpoint**: Specifies the details of the `/data` endpoint including the expected request format, response structure, and possible error responses. This specification ensures that the API adheres to a standard and helps maintain consistency.

### templates/index.html

The `index.html` file serves as the frontend of the web application. Here's an overview of its contents:
- **Form**: Contains input fields for start and end dates where users can input custom date ranges.
- **JavaScript**: Contains JavaScript code to handle form submission and display the search results.
- **HTML**: Defines the structure of the page including form elements and a container to display the search results.

## Reason

The purpose of this application is to provide users with a simple interface to search for events within a specified date range. By allowing users to input custom start and end dates, the application offers flexibility in retrieving relevant data from the external API.

## Expected Output

When a user accesses the application, they are presented with a form containing input fields for start and end dates. After entering the desired date range and submitting the form, the application sends a request to the external API to fetch events within the specified range. The retrieved data is then displayed on the page in a structured format, providing the user with information about the events that match their criteria.
