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
git clone [https://github.com/YOUR_USERNAME/fastapi-credit-banking-api.git](https://github.com/YOUR_USERNAME/fastapi-credit-banking-api.git)
cd fastapi-credit-banking-api

2. Install Dependencies
Install the required micro-framework frameworks for handling requests and serving the API:
pip install fastapi uvicorn

3. Boot the Application Server
Execute this command to start the local development environment with auto-reload enabled:
uvicorn main:app --reload

4. Interactive API Testing
Once the server initializes successfully, open your browser and navigate to the interactive Swagger UI panel to test the available endpoints live:

Interactive Docs Dashboard: http://127.0.0.1:8000/docs
