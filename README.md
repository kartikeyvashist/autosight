AutoSight – Sales Analytics Engine
Overview
AutoSight is a modular Python-based sales analytics engine that:
Connects to PostgreSQL database
Ingests CSV sales data
Performs revenue aggregation
Analyzes daily revenue trends
Predicts next-day revenue (basic moving-average model)
Generates revenue visualization charts
Exports structured executive-ready JSON reports
Logs all operations into a centralized log file
This project demonstrates backend data pipeline architecture and analytics workflow implementation.
Architecture
AutoSight follows a modular structure:
autosight_project/
│
├── main.py              # Orchestrator
├── db.py                # Database connection logic
├── ingestion.py         # CSV ingestion layer
├── analysis.py          # Trend & prediction logic
├── visualization.py     # Revenue chart generation
├── reporting.py         # JSON export layer
├── logger_config.py     # Logging configuration
├── .env                 # Environment variables (not committed)
├── .gitignore
└── README.md

Each module handles a single responsibility.

Features
1. Data Ingestion

Reads CSV sales data and inserts it into PostgreSQL.

2. Revenue Analytics

Product-wise revenue aggregation

Overall performance metrics

Daily revenue grouping

3. Trend Analysis

Percentage-based daily change detection

Categorized as:

Strong Growth

Moderate Growth

Decline

4. Revenue Prediction

Moving-average based prediction

Handles zero-division edge cases

Uses recent revenue changes for stability

5. Visualization

Line chart of daily revenue

Saved as revenue.png

6. Reporting

Exports structured JSON:

report.json

Includes:

Executive summary

Product performance

Trend analysis

Predicted revenue

7. Logging

Centralized logging via Python logging

Logs saved in autosight.log

Tracks pipeline steps & errors

Technologies Used

Python 3.13

PostgreSQL

psycopg2

matplotlib

python-dotenv

Git & GitHub

How to Run

Clone the repository

git clone https://github.com/kartikeyvashist/autosight.git
cd autosight

Create .env file

DB_HOST=localhost
DB_NAME=autoinsight_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432

Install dependencies

pip install -r requirements.txt

Run the pipeline

python main.py
Project Status

In Progress – Actively improving architecture, analytics logic, and prediction accuracy.

Future Improvements

Advanced forecasting models

REST API layer

Web dashboard interface

Automated scheduled ingestion

Docker containerization