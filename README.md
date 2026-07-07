# Automated Credit Management API

A high-performance RESTful API built with FastAPI for automated credit processing, transaction logging, and validation.

A lightweight, secure backend REST API engine engineered using **FastAPI** and **Python** to automate financial credit allocations and entry postings.

## 🛠️ Core Technical Features
- **FastAPI Framework:** Implements asynchronous routing for rapid transaction throughput.
- **Data Validation & Integrity:** Utilizes Pydantic schemas to validate financial data schemas and enforce currency constraints.
- **Robust System Logging:** Features localized structured logging to capture audit trails, tracking successful postings and intercepting execution anomalies.
- **Interactive Documentation:** Out-of-the-box integration with Swagger UI (`/docs` endpoint) for transparent API testing and endpoint evaluation.

## 📂 System Architecture
1. **Request Ingestion:** REST client POST requests hit the `/api/v1/credit` endpoint.
2. **Validation Layer:** Payloads are scrutinized by data contracts (Account verification, negative-amount rejection).
3. **Audit Execution:** System records transaction metadata via Python's native logging framework prior to database simulation.

## 🚀 Getting Started

### 1. Clone the Repository
Run this command in your terminal to download the project source code:
```bash
git clone [https://github.com/muzammil64049/fastapi-credit-banking-api.git](https://github.com/muzammil64049/fastapi-credit-banking-api.git)
cd fastapi-credit-banking-api
