##📌 About The Project
AutoSight is a Python-based modular sales analytics engine that:

    Connects to a PostgreSQL database

    Ingests CSV sales data

    Performs revenue aggregation

    Analyzes daily revenue trends

    Predicts next-day revenue

    Generates revenue visualization charts

    Exports executive-ready JSON reports

    Maintains structured logging

This project demonstrates backend data pipeline architecture and analytical workflow design.

##🏗 Architecture Overview

autosight_project/
│
├── main.py              → Orchestrator
├── db.py                → Database connection
├── ingestion.py         → CSV ingestion layer
├── analysis.py          → Trend & prediction logic
├── visualization.py     → Revenue charts
├── reporting.py         → JSON export layer
├── logger_config.py     → Logging configuration
├── .env                 → Environment variables (ignored)
├── autosight.log        → Runtime logs
└── README.md

Each module follows single-responsibility principle.

##📊 Features Implemented
#🔹 Data Ingestion

    Reads CSV data

    Inserts into PostgreSQL

#🔹 Revenue Analytics

    Product-wise revenue

    Overall performance metrics

    Daily revenue aggregation

#🔹 Trend Analysis

    Percentage-based revenue change detection

    Categorized into:

    Strong Growth

    Moderate Growth

    Decline

#🔹 Revenue Prediction

    Moving-average based logic

    Handles zero-division safely

    Uses recent data for stability

#🔹 Visualization

    Line chart of daily revenue

    Output: revenue.png

#🔹 JSON Reporting

Exports structured:

report.json

Includes:

    Executive summary

    Product performance

    Trend insights

    Predicted revenue

#🔹 Logging

    Centralized logging system

    Logs saved in autosight.log

    Tracks pipeline steps & errors

##🛠 Tech Stack

    Python 3.13

    PostgreSQL

    psycopg2

    matplotlib

    python-dotenv

    Git & GitHub

##▶️ How To Run

#1️⃣ Clone repository

git clone https://github.com/kartikeyvashist/autosight.git
cd autosight

#2️⃣ Create .env
    DB_HOST=localhost
    DB_NAME=autoinsight_db
    DB_USER=postgres
    DB_PASSWORD=your_password
    DB_PORT=5432
#3️⃣ Install dependencies

    pip install -r requirements.txt

#4️⃣ Run pipeline

    python main.py

##📈 Project Status

#🟡 In Progress
Currently improving:

    Prediction logic

    Architecture robustness

    Data visualization enhancements