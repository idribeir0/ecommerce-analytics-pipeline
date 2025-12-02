# 🛒 E-commerce Analytics Pipeline

**End-to-end data engineering pipeline for real-time e-commerce analytics**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![dbt](https://img.shields.io/badge/dbt-1.7+-orange.svg)](https://www.getdbt.com/)
[![Airflow](https://img.shields.io/badge/Airflow-2.8+-017CEE.svg)](https://airflow.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-latest-2496ED.svg)](https://www.docker.com/)

---

## 🎯 Project Status

🚧 **Work in Progress** — Building production-grade data pipeline

**Current Phase:** Foundation & Architecture

---

## 🏗️ Architecture
```
Event Generator (Python)
    ↓
AWS S3 (Bronze Layer)
    ↓
dbt Transformations (Silver → Gold)
    ↓
Orchestration (Airflow)
    ↓
Data Warehouse (AWS Athena)
    ↓
API (FastAPI) + Dashboard (Streamlit)
```

---

## 🛠️ Tech Stack

- **Orchestration:** Apache Airflow
- **Transformations:** dbt (data build tool)
- **Storage:** AWS S3
- **Warehouse:** AWS Athena / DuckDB (local dev)
- **API:** FastAPI
- **Visualization:** Streamlit
- **Infrastructure:** Docker, Terraform
- **Language:** Python 3.9+

---

## 📊 Business Metrics

Pipeline will generate insights on:
- Conversion rate (page view → purchase)
- Average order value
- Top products by revenue
- User retention & churn
- Device/country analytics

---

## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/idribeir0/ecommerce-analytics-pipeline.git
cd ecommerce-analytics-pipeline

# Install dependencies
pip install -r requirements.txt

# Start services (Docker)
docker-compose up -d
```

*(Detailed setup instructions coming soon)*

---

## 📊 Generate Sample Data
```bash
# Generate 1000 fake e-commerce events
python data_generator/generate_events.py
```

This creates:
- `data/raw_events/events_TIMESTAMP.jsonl` — JSON Lines format (one event per line)
- `data/raw_events/events_TIMESTAMP.csv` — CSV format for easy inspection

**Event schema:**
```json
{
  "event_id": "uuid",
  "user_id": "user_0001",
  "event_type": "page_view|add_to_cart|purchase",
  "product_id": "prod_0001",
  "product_name": "Innovative cloud solution",
  "category": "Electronics|Clothing|Home|Sports|Books",
  "price": 199.99,
  "timestamp": "2025-11-15T14:30:00",
  "device": "mobile|desktop|tablet",
  "country": "US|BR|UK|DE|FR|CA",
  "revenue": 199.99,  // only for purchases
  "quantity": 2       // only for purchases
}
```

---

**Event distribution (realistic funnel):**
- 60% page_view
- 25% add_to_cart
- 15% purchase

## 📂 Project Structure
```
├── data_generator/     # Fake event generation scripts
├── airflow/           # Orchestration DAGs
├── dbt/              # SQL transformations
├── api/              # FastAPI endpoints
├── dashboard/        # Streamlit app
├── terraform/        # Infrastructure as Code
└── docs/            # Architecture diagrams
```

---

## 🎓 Learning Objectives

This project demonstrates:
- ✅ Modern data stack (dbt + Airflow)
- ✅ Medallion architecture (Bronze → Silver → Gold)
- ✅ Data quality testing
- ✅ Orchestration & scheduling
- ✅ API design & deployment
- ✅ Infrastructure as Code

---

## 📈 Roadmap

- [x] Project setup
- [x] Event generator
- [ ] dbt models (staging → marts)
- [ ] Airflow DAGs
- [ ] FastAPI endpoints
- [ ] Streamlit dashboard
- [ ] AWS deployment
- [ ] CI/CD pipeline

---

## 👤 Author

**Ione Ribeiro**  
Data Engineer/Data Analyst | Building production-grade data systems


---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details