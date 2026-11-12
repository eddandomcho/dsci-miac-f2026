# Duke Statistical Consulting Initiative (DSCI) MIAC Project

**Mortgage Prepayment & Potential Credit Scalar Modeling • Fall 2026**

**Team Members**: Jennifer Lee, Daniel Murong, Khyai Agarwal, Catherine Zhang, Ethan Cho

---

## Project Objective

The objective of this project is to analyze and model mortgage loan behavior using MIAC datasets across conventional, veteran (VA), and federal (FHA) loan programs. We investigate key performance drivers, prepayment trends, and credit score dynamics to inform predictive credit scalar modeling.

---

## Repository Structure

```text
dsci-miac-f2026/
├── data/                       # Local data extracts, sample CSVs, and query outputs
│   ├── conv_credit_score_rate_spread.csv
│   ├── l1_conventional_data_202611042035.csv
│   ├── l2_conventional_data_202611042047.csv
│   └── l2_conventional_data_202611052042.csv
├── model/                      # Exploratory data analysis, modeling, and query helpers
│   ├── ethancho/               # Individual EDA scripts and exploratory notebooks
│   │   ├── eda.ipynb
│   │   └── eda.py
│   ├── libs/                   # Shared utility modules
│   │   └── pyathena_lib.py     # AWS Athena connector and query execution helper
│   └── queries/                # Analytical SQL queries for specific cohorts and filters
│       ├── filter_2020_loans.sql
│       └── nc_2024.sql
├── transform/                  # Athena SQL ETL scripts across data lake layers
│   ├── l1/                     # CTAS queries to convert raw files into Parquet
│   │   ├── l1_conventional_data.sql
│   │   └── l1_federal_data.sql
│   ├── l2/                     # Cleaned, standardized, and typed tables ready for querying
│   │   ├── l2_conventional_data.sql
│   │   ├── l2_federal_data.sql
│   │   └── l2_veteran_data.sql
│   └── csv_to_json.py          # Data conversion utility script
├── visualization/              # Visualizations, charts, and report figures
├── build.sh                    # Automated setup script (creates virtual environment & installs dependencies)
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview and documentation
```

---

## Database Structure

The project uses an AWS Athena / S3 data lake architecture organized into layered stages:

### l0: Raw Data

- Initial raw mortgage origination and monthly performance data ingested from MIAC source files.

### l1: Parquet Data (Post CTAS)

- Raw data converted to columnar Parquet format using Create Table As Select (CTAS) queries in Athena for optimized compression and query performance (see `transform/l1/`).

### l2: Cleaning, Ready for Querying

- Cleaned, deduplicated, and typed tables covering conventional, veteran (VA), and federal (FHA) loan portfolios (see `transform/l2/`).

### l3: Dataset-Level Tables for Analysis

- Cohort-filtered, feature-engineered tables and analytical extracts tailored for exploratory data analysis, rate spread evaluations, and prepayment modeling.

---

## Getting Started

### 1. Environment Setup

Run the automated build script to create a virtual environment and install project dependencies:

```bash
chmod +x build.sh
./build.sh
source venv/bin/activate
```

### 2. AWS Athena Credentials

Ensure you have a `.env` file in the project root with your AWS credentials to query Athena:

```env
ACCESS_KEY=your_aws_access_key
SECRET_ACCESS_KEY=your_aws_secret_access_key
```
