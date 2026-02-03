# Data Quality Monitoring Pipeline (FinTech Use Case)

## Project Overview
This project simulates a production-style data quality monitoring pipeline for financial transaction data.

The pipeline validates incoming datasets and detects potential data integrity issues before downstream processing.

---

## Objectives
- Detect missing values in critical columns
- Detect abnormal data volume spikes
- Validate schema consistency
- Generate alert messages

---

## Tech Stack
- Python
- Pandas
- Modular pipeline design
- Basic alerting logic

---

## Project Structure
data-quality-monitoring-project/
│
├── checks/
│    ├── __init__.py
│    ├── data_quality_checks.py
│
├── alerts/
│    ├── __init__.py
│    ├── alert_logic.py
│
├── data/
│    ├── sample_transactions.csv   (optional sample only)
│
├── requirements.txt
├── README.md

## Data Quality Checks Implemented

### 1. Missing Value Detection
Detects null values in critical financial fields.

---

### 2. Schema Validation
Validates:
- Expected column names
- Expected data types
- Nullable integer handling

---

### 3. Volume Spike Detection
Detects sudden increase or drop in dataset size.

---

### 4. Alert System
Triggers alerts when validation rules fail.

## How To Run

Clone repository:

git clone <your repo link>


Install dependencies:

pip install -r requirements.txt


Run checks:

py -m checks.data_quality_checks


---

## 📊 Example Output

[ALERT] Missing Values Detected

Details:

{'TransactionID': 2512}

Data quality checks completed.

## Real-World Relevance
This project simulates production monitoring for fintech data pipelines where data integrity is critical.
