# Billing API

A backend service for subscription-based billing, built with **FastAPI** and **PostgreSQL**.

This project demonstrates how to design and implement a real-world backend system with customers, plans, subscriptions, and invoices, using modern Python tooling and **containerized infrastructure**, both **locally** and **in the cloud (AWS)**.

---

## 🚀 Live Demo (AWS EC2)

The application is currently deployed on **AWS EC2** and publicly accessible.

- **Swagger UI:**  
  http://16.171.172.53:8000/docs

- **Health check:**  
  http://16.171.172.53:8000/health

> ⚠️ This is a demo environment for learning and evaluation purposes.  
> The public IP may change if the EC2 instance is restarted.

---

## ✨ Features

- Customer management
- Subscription plans (monthly billing)
- Subscriptions with business rules:
  - One active subscription per customer
  - Automatic invoice generation on subscription creation
- Relational data model with PostgreSQL
- Database migrations with Alembic
- Containerized development and deployment
- Cloud deployment on AWS EC2

---

## 🧱 Tech Stack

### Backend
- Python 3.12
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- PostgreSQL
- Alembic migrations

### DevOps / Infrastructure
- Docker
- Docker Compose
- AWS EC2 (Amazon Linux)
- Linux networking & security groups

---

## 🗂️ Domain Model (simplified)

- **Customer**
- **Plan**
- **Subscription**
- **Invoice**

A subscription links a customer to a plan and automatically generates invoices for each billing period.

---

## 🚀 Running the project locally

### Prerequisites
- Docker
- Docker Compose

### Start the application
```bash
docker compose up --build
```

### API access
- API base URL: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- Health check: http://localhost:8000/health

---

## ☁️ Deployment (AWS EC2)

This project is deployed on an **AWS EC2 instance** using Docker and Docker Compose.

### Architecture
- AWS EC2 (Amazon Linux)
- Docker & Docker Compose
- FastAPI API container
- PostgreSQL container with persistent volume
- Private Docker network between services

### Deployment overview
1. Provisioned an EC2 instance and configured security groups (SSH + API port).
2. Installed Docker and Docker Compose on the server.
3. Built and ran the application using a production Docker Compose configuration.
4. PostgreSQL runs internally and is not exposed publicly.
5. API is exposed via the EC2 public IP on port `8000`.

### Running services
- `api` – FastAPI application served by Uvicorn
- `postgres` – PostgreSQL database with persistent storage

### Health & documentation
- Health endpoint: `GET /health`
- Swagger UI: `/docs`

---

## 🔍 Example flow

1. Create a customer
2. Create a subscription plan
3. Create a subscription for the customer
4. An invoice is automatically generated
5. List invoices by customer

All steps can be tested directly via **Swagger UI**.

---

## 🧪 Database migrations

### Generate a new migration
```bash
docker compose run --rm api alembic revision --autogenerate -m "migration message"
```

### Apply migrations
```bash
docker compose run --rm api alembic upgrade head
```

---

## 🧠 Design decisions

- UUIDs are used as primary keys for public-safe identifiers
- Integer cents are used for monetary values to avoid floating-point errors
- Subscription and invoice creation happens in a single database transaction
- A fixed 30-day billing period is used for simplicity in the initial version

---
