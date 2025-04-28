#  **Sephora Price Tracker** 📈💅

## 💡 **Project Overview**

This project aims to **track the price history** of products on the **Sephora website** and provide **automatic alerts** when the price of desired products reaches an all-time low.

Using **Python**, **Playwright**, **Airflow**, and **Docker**, the system collects product details such as **name, brand, price, ingredients,** and more, and stores them in a **database**. The **Airflow DAG** automates the data scraping process, enabling periodic data collection. Alerts can be set up to notify the user when specific products drop to their desired price.

## ⚙️ **Technologies Used**

- 🐍 **Python**
- 🌐 **Playwright** (Web scraping)
- 🐳 **Docker**
- 📊 **Airflow** (Task automation)
- 📁 **PostgreSQL** (Database)
- 📬 **Email Alerts** 

## 🚀 **Project Goals**

- Track the price history of Sephora products over time.
- Set up alerts when a product reaches an all-time low price.
- Automate the scraping process using **Airflow**.
- Store product data in a **PostgreSQL** database.

## 💑 **How to Set Up and Run**

### Prerequisites

Make sure you have the following installed:

- 🖥️ **Git**: [Download Git](https://git-scm.com/)
- 🐳 **Docker**: [Download Docker](https://www.docker.com/get-started)
- 📆 **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
- 📧 **PostgreSQL**: Will be automatically set up with Docker

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sephora-price-tracker.git
cd sephora-price-tracker
```

### 2. Set Up Docker Environment

Run the following command to build and start the Docker containers:

```bash
docker-compose up --build -d
```

This will start the **Airflow**, **PostgreSQL**, and other necessary services.

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install all necessary Python packages for the project.

### 4. Set Up Airflow

Create a user to access the **Airflow UI**:

```bash
docker-compose run --rm webserver airflow users create \
  --username <your-username> \
  --firstname <your-firstname> \
  --lastname <your-lastname> \
  --email <your-email@example.com> \
  --role Admin \
  --password <your-password>
```

Once the user is created, open the **Airflow UI** at `http://localhost:8080` and log in.

### 5. Trigger the Scraping DAG

From the **Airflow UI**, you can trigger the scraping DAG that will automatically start scraping data from Sephora.

## 📝 **Project Roadmap**

- Add a UI to visualize price trends.
- Implement more granular price tracking (e.g., daily price tracking).
- Integrate with **Slack** or other messaging platforms for alerts.

## 📂 **File Structure**

```bash
sephora-price-tracker/
├── dags/
│   ├── sephora_scraper.py       # Scraper script
│   └── airflow_dag.py           # Airflow DAG configuration
├── requirements.txt             # Python dependencies
├── docker-compose.yml           # Docker Compose configuration
├── Dockerfile                   # Docker image configuration
└── README.md                    # Project documentation
```

### 🎉 **Thank You for Checking Out the Project!**

Happy price tracking! 💸

---
**Disclaimer:** This project is for personal use and is not affiliated with Sephora in any way.

