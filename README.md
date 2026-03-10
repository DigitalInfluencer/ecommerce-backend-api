# E-commerce Backend API

A scalable **E-commerce Backend API** built with **Django** and **Django REST Framework**.
This project provides a complete backend solution for an online store including product management, shopping cart, orders, payments, delivery addresses, and product reviews.

The project is fully **Dockerized** and uses **PostgreSQL, Redis, and Celery** for scalable and production-ready architecture.

---

# Features

* JWT Authentication
* Google OAuth login
* Product catalog management
* Category and brand management
* Shopping cart system
* Wishlist functionality
* Order management
* Delivery address management
* Online payment integration (Payme / Click ready)
* Product reviews and ratings
* Email notifications
* Background tasks with Celery
* Redis caching
* API documentation with Swagger
* Dockerized development environment

---

# Tech Stack

**Backend**

* Python
* Django
* Django REST Framework

**Database**

* PostgreSQL

**Async & Caching**

* Redis
* Celery

**Infrastructure**

* Docker
* Docker Compose

**Authentication**

* JWT (SimpleJWT)
* Google OAuth

**Documentation**

* Swagger (drf-spectacular)

---

# Project Structure

```
ecommerce/
│
├── users/          # Authentication and user management
├── products/       # Products, categories, brands
├── cart/           # Shopping cart logic
├── orders/         # Order management
├── payments/       # Payment processing
├── reviews/        # Product reviews and ratings
├── delivery/       # Delivery addresses
│
├── config/         # Django project configuration
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

---

# Installation (Docker)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ecommerce-backend.git
cd ecommerce-backend
```

---

### 2. Create environment variables

```bash
cp .env.example .env
```

Update `.env` file with your settings.

Example:

```
DB_NAME=ecommerce_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

SECRET_KEY=your-secret-key
DEBUG=True
```

---

### 3. Run the project

```bash
docker compose up --build
```

---

### 4. Apply database migrations

```bash
docker compose exec web python manage.py migrate
```

---

### 5. Create superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

### 6. Access the application

Server will run at:

```
http://localhost:8000
```

Admin panel:

```
http://localhost:8000/admin/
```

Swagger API documentation:

```
http://localhost:8000/api/docs/
```

---


# API Modules

The backend consists of the following modules:

### Authentication

* Register
* Login (JWT)
* Token refresh
* Google OAuth

### Products

* Product list
* Product detail
* Categories
* Brands
* Product search

### Cart

* Add to cart
* Remove from cart
* Update quantity

### Wishlist

* Add product to wishlist
* Remove product from wishlist
* View wishlist

### Orders

* Create order
* Order history
* Order detail

### Delivery

* Manage delivery addresses

### Payments

* Payment processing
* Payment status

### Reviews

* Product reviews
* Product ratings

---

Example endpoints:

```
POST   /api/login/
POST   /api/register/

GET    /api/v1/products/
GET    /api/v1/products/popular/
GET    /api/v1/products/top-rated/

GET    /api/v1/cart/
POST   /api/v1/cart/add/
DELETE /api/v1/cart/remove/{product_id}/

POST   /api/v1/checkout/

GET    /api/v1/orders/
GET    /api/v1/orders/{id}/

POST   /api/v1/payments/create/

POST   /api/v1/reviews/
GET    /api/v1/reviews/{id}/
```

---

# API Flow

```
User
 │
 ▼
Register / Login
 │
 ▼
Browse Products
 │
 ▼
View Product Detail
 │
 ▼
Add to Cart
 │
 ▼
Create Delivery Address
 │
 ▼
Checkout
 │
 ▼
Create Order
 │
 ▼
Payment
 │
 ▼
Order Completed
 │
 ▼
Write Review
```

---

# Database Structure

```
User
 │
 ├── Wishlist
 │       │
 │       ▼
 │    Product
 │
 ▼
CartItem
 │
 ▼
Product
 │
 ▼
Category
 │
 ▼
Brand

Order
 │
 ├── OrderItem
 │       │
 │       ▼
 │    Product
 │
 ▼
Payment

DeliveryAddress

Review
 │
 ▼
Product
```

---
# System Architecture

```
              Client (Frontend / Mobile)
                       │
                       ▼
                 Django API
            (Django REST Framework)
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    PostgreSQL       Redis          Celery
    Database        Cache &       Background
                    Broker          Tasks
                                      │
                                      ▼
                              Email / Notifications
```
---

# Background Tasks

Celery is used for asynchronous tasks such as:

* Sending email notifications
* Order expiration handling
* Background processing

Redis is used as a **message broker** for Celery.

---

# API Documentation

Swagger documentation is available at:

```
http://localhost:8000/api/docs/
```

It provides interactive API testing and schema documentation.

---

# Future Improvements

* Product filtering and advanced search
* Product recommendation system
* Coupons and discount system
* Order tracking
* Product variants (size, color)
* Analytics dashboard

---

# License

This project is licensed under the **MIT License**.

---

# Author

Backend Developer Portfolio Project.
