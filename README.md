# ScrapperData

## Overview

ScrapperData is a web scraping project that utilizes Selenium to collect data from the avito.com website. The project includes two versions of the code: one for local execution and the other designed to run on a cloud platform.

## Project Structure

- `local_scraper.py`: Python script for local execution, scrapes data from avito.com.
- `cloud_scraper.py`: Python script designed for cloud environments, also scrapes data from avito.com.

## Local Scraper

### Prerequisites
- Ensure you have Python installed on your local machine.
- Install Selenium on your local machine or on your solution cloud.


### Usage
1. Open `local_scraper.py` in a text editor.
2. Update the configuration variables, such as the target URL and other settings.
3. Run the script using the following command:


## Cloud Scraper

### Prerequisites
- Ensure you have access to a cloud platform (e.g., AWS, GCP) and the necessary credentials.

### Usage
1. Open `cloud_scraper.py` in a text editor.
2. Update the configuration variables, including cloud-specific settings.
3. Deploy the script on your preferred cloud platform, ensuring you have the required resources and permissions.
4. Execute the script based on your cloud provider's instructions.

## Important Note

- Be mindful of web scraping ethics and legality. Ensure you comply with the terms of service of the avito.com website.
- Consider rate-limiting and respectful scraping practices to avoid putting unnecessary load on the target server.

## License

This project is licensed under the [MIT License](LICENSE).
