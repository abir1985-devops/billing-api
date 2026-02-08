# Billing API

A backend service for subscription-based billing, built with FastAPI and PostgreSQL.

This project demonstrates how to design and implement a real-world backend system with customers, plans, subscriptions, and invoices, using modern Python tooling and containerized infrastructure.

The service is deployed automatically using the infrastructure defined here:
https://github.com/abir1985-devops/billing-infrastructure

🚀 Live Demo
Swagger UI:
http://63.177.100.85/docs

Health check:
http://63.177.100.85/health

⚠️ Demo environment. The public IP may change if the EC2 instance is recreated.

✨ Features
Customer management
Subscription plans (monthly billing)
Subscriptions with business rules:
One active subscription per customer
Automatic invoice generation on subscription creation
Relational data model with PostgreSQL
Database migrations with Alembic
Containerized development and automated cloud deployment

🧱 Tech Stack
Backend
Python 3.12
FastAPI
SQLAlchemy
Pydantic

Database
PostgreSQL
Alembic migrations

DevOps / Infrastructure
Docker
Docker Compose
AWS EC2
Automated CI/CD deployment

🗂️ Domain Model (simplified)
Customer
Plan
Subscription
Invoice

A subscription links a customer to a plan and automatically generates invoices for each billing period.

🚀 Running the project locally

Prerequisites
Docker
Docker Compose

Start the application
docker compose up --build

API access
API base URL: http://localhost:8000
Swagger UI: http://localhost:8000/docs
Health check: http://localhost:8000/health

☁️ Deployment

The application is deployed automatically through CI/CD.  
The server pulls a pre-built container image and restarts services without manual intervention.

Running services
api – FastAPI application served by Uvicorn
postgres – PostgreSQL database with persistent storage
nginx – reverse proxy exposing the API

Health & documentation
Health endpoint: GET /health
Swagger UI: /docs

🔍 Example flow
Create a customer
Create a subscription plan
Create a subscription for the customer
An invoice is automatically generated
List invoices by customer

All steps can be tested directly via Swagger UI.

🧪 Database migrations

Generate a new migration
docker compose run --rm api alembic revision --autogenerate -m "migration message"

Apply migrations
docker compose run --rm api alembic upgrade head

🧠 Design decisions
UUIDs are used as primary keys for public-safe identifiers
Integer cents are used for monetary values to avoid floating-point errors
Subscription and invoice creation happens in a single database transaction
A fixed 30-day billing period is used for simplicity in the initial version