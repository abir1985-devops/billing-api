# Billing API

A backend service for subscription-based billing, built with FastAPI and PostgreSQL.

This project demonstrates how to design and implement a real-world backend system with customers, plans, subscriptions, and invoices, using modern Python tooling and containerized infrastructure.

---

## ✨ Features

- Customer management
- Subscription plans (monthly billing)
- Subscriptions with business rules:
  - One active subscription per customer
- Automatic invoice generation on subscription creation
- Relational data model with PostgreSQL
- Database migrations with Alembic
- Containerized development environment

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

### DevOps
- Docker
- Docker Compose

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

---

### API access

API base URL: http://localhost:8000

Swagger UI: http://localhost:8000/docs

Health check: http://localhost:8000/health

---

### Example flow

Create a customer

Create a subscription plan

Create a subscription for the customer

An invoice is automatically generated

List invoices by customer

All steps can be tested directly via Swagger UI.

---

### Database migrations

Generate a new migration:

docker compose run --rm api alembic revision --autogenerate -m "migration message"

### Apply migrations:

docker compose run --rm api alembic upgrade head

---

###Design decisions

- UUIDs are used as primary keys for public-safe identifiers

- Integer cents are used for monetary values (avoids floating-point errors)

- Single transaction for subscription + invoice creation

- 30-day billing period used for simplicity in v1

