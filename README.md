# Personal Finance Tracker API

Production-ready Django REST API with Clean Architecture + SOLID principles

## Features
- Custom User with JWT authentication
- Repository + Service Layer pattern
- CSV transaction import (Celery)
- Monthly reports & budget alerts
- Swagger docs: `/api/docs/`
- Docker + Redis + Celery ready

## Tech Stack
- Django 5 + DRF
- PostgreSQL + Redis
- Celery + RabbitMQ/Redis
- JWT + drf-spectacular
- Pytest + Clean Architecture

## Quick Start
```bash
docker-compose up --build
