# Auth Service

A lightweight authentication API built with Django and Django REST Framework. It provides user registration, login with token authentication, and permission validation. The service runs with Docker and is deployed on Render.

## Live API

Base URL:  
https://auth-service-r1lp.onrender.com/

## Features

- User registration with unique email
- Password hashing and validation
- Token-based login
- User permission checking
- Docker-based development environment
- Environment variable support via `.env`
- Email-based login
- Structured success and error responses with message

## Endpoints

### 1. Register

POST `/auth/register/`

Request body:
```json
{
  "username": "taha",
  "email": "taha@hsrw.com",
  "password": "TestPass1234",
  "phone": "1234567890"
}
```

Response:
```json
{
  "message": "User registered successfully",
  "data": {
    "id": 1,
    "username": "taha",
    "email": "taha@hsrw.com",
    "phone": "1234567890"
  }
}
```

### **2. Login**

POST /auth/login/

Request body:
```json
{
  "email": "taha@hsrw.com",
  "password": "TestPass1234"
}
```

Returns:
```json
{
  "message": "Login successful",
  "data": {
    "token": "...",
    "user_id": 1,
    "email": "taha@hsrw.com"
  }
}
```

### **3. Validate Permission**

POST /auth/permission/

Headers:

```
Authorization: Token <your-token>
```

Request body:

```json
{
  "permission": "accounts.change_customuser"
}
```

Response (authorized):

```json
{
  "status": "authorized"
}
```

Response (unauthorized):

```json
{
  "status": "unauthorized"
}
```

## **Quick Start (with Docker)**

1. Clone the repository

```
git clone https://github.com/pipiwolve/auth-service.git
cd auth-service
```

2. Create .env file

```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=auth-service-2gbd.onrender.com
DATABASE_URL=postgresql://pipiwolve:USAPKQo01uqQz8u2K2rHZkrw2L65CoFC@dpg-d0hjviruibrs739qq5a0-a/auth_hnn9
```

3. Build and run the containers

```
docker-compose up --build
```

4. Run migrations

```
docker-compose exec web python manage.py migrate
```

## **Testing**

You can import the updated auth-service.postman_collection.json into Postman and test the API step by step: 

register → login → validate.

## **Stack**

- Django 4.2
- Django REST Framework
- PostgreSQL
- Docker
- Render (deployment)

## **Notes**

- Passwords are hashed automatically.
- Permissions follow the format <app_label>.<codename>,  e.g. accounts.view_customuser.
- Admin access requires creating a superuser.
