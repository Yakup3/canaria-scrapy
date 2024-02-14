# Scraping Pipeline Project

## Overview

This project is a web scraping pipeline built using Python, Scrapy, PostgreSQL, and Docker. It extracts data from JSON files, processes it, and stores it in a PostgreSQL database. The entire application is containerized using Docker and orchestrated with Docker Compose. Additionally, it provides functionality to query the database and retrieve the processed data in CSV format.

## Setup Instructions

**Prerequisites**: Ensure that Docker and Docker Compose are installed on your system.

To set up and run the project, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```
   cd canaria-scrapy
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Build and run the Docker containers:

   ```
   docker-compose up --build
   ```

**Note**: If you encounter any issues related to the database service not being ready when the Scrapy service starts, ensure that you have the `wait-for-it.sh` script available and executable in your project directory. This script is used to wait for the PostgreSQL database service to be ready before starting the Scrapy service.

## Pipeline Process

1. **Scraping**: The project includes a Scrapy spider (`json_spider.py`) that extracts data from JSON files (`sample.json` and `sample2.json`). It parses the JSON data and creates `JobItem` objects containing various fields.

2. **Data Processing**: The scraped data is processed using Scrapy's item pipeline. The `PostgreSQLPipeline` class in `pipelines.py` handles the processing of items before inserting them into the PostgreSQL database. It establishes a connection to the database, creates a table if it doesn't exist, and inserts records into the `raw_table`.

3. **Database Interaction**: The `query.py` script provides a `Database` class for interacting with the PostgreSQL database. It allows querying the database to retrieve processed data and save it to a CSV file.

4. **Dockerization**: The entire application is containerized using Docker and orchestrated with Docker Compose. The `docker-compose.yaml` file defines services for Scrapy, PostgreSQL, and any other necessary dependencies.

## Additional Notes

- Make sure to update the database connection information in the following files if any changes are made:
  - `docker-compose.yaml`: Update the PostgreSQL environment variables to match the new database configuration.
  - `dockerfile`: If necessary, ensure that the `wait-for-it.sh` command waits for the correct host and port combination before starting the Scrapy spider.
  - `query.py`: Update the database initialization parameters to reflect the new database connection details.
  - `settings.py`: Update the PostgreSQL connection settings to match the new database configuration.
