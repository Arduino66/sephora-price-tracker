# Sephora Price Tracker

## Project Overview

The goal of this project is to track the price history of Sephora products and set up automatic alerts when the prices drop to an all-time low. The project uses **Airflow** for orchestrating workflows and **Playwright** for web scraping Sephora product details, including their names, prices, and other related data. This data is stored and processed for future price analysis.

### Features:
- Scraping Sephora product data (including name, price, and other details).
- Storing product data in a database.
- Creating an Airflow DAG for automation of the scraping and data processing workflows.
- Alerting system when a product reaches an all-time low price.

---

## Project Setup

### Prerequisites

Before running the project, ensure that you have the following installed:

- **Docker**: To containerize and run the application.
- **Python**: For running the Playwright scripts and managing dependencies.
- **Git**: To clone the project and push it to a repository.

### Installing Dependencies

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/<your-github-username>/sephora-price-tracker.git
    ```

2. Navigate to the project folder:

    ```bash
    cd sephora-price-tracker
    ```

3. Install the required Python dependencies using **pip**:

    ```bash
    pip install -r requirements.txt
    ```

4. Build and run the Docker containers (for Airflow):

    ```bash
    docker-compose up -d
    ```

---

## How to Set Up and Run

1. **Docker**: The project uses Docker to set up a local Airflow environment. Once the containers are running, Airflow will be available at `http://localhost:8080`. 

2. **Running the Airflow DAG**: The main workflow is defined in the DAG, which automates scraping and tracking the prices of the products. Airflow will handle this task based on the schedule defined in the DAG configuration.

3. **Adding Alerts**: Once the price data is collected, you can set up alerts to notify you when products hit the target price.

---

## Files and Directories

- **airflow_project**: Contains all the configuration files for Airflow.
- **dags/**: Contains the main Airflow DAG for scraping and automation.
- **requirements.txt**: Lists the required Python packages for the project.
- **README.md**: Project documentation (this file).
- **.gitignore**: Specifies which files to ignore in the version control (e.g., Docker, virtual environments).

---

