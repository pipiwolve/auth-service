



# **Django Auth API — Usage Guide**





**Base URL**

```
https://auth-service-2gbd.onrender.com
```



------





## **🔐 1. Register**





- **URL**: /auth/register/

- **Method**: POST

- **Headers**:

  Content-Type: application/json

- **Request Body**:



```
{
  "username": "jaden",
  "email": "jaden@example.com",
  "password": "testpass1234",
  "phone": "1234567890"
}
```



- **Success Response**:



```
{
  "message": "User registered successfully",
  "data": {
    "username": "jaden",
    "email": "jaden@example.com",
    "phone": "1234567890"
  }
}
```



- **Error Response**:



```
{
  "message": "Registration failed",
  "errors": {
    "email": ["This field must be unique."]
  }
}
```



------





## **🔑 2. Login**





- **URL**: /auth/login/

- **Method**: POST

- **Headers**:

  Content-Type: application/json

- **Request Body**:



```
{
  "email": "jaden@example.com",
  "password": "testpass1234"
}
```



- **Success Response**:



```
{
  "message": "Login successful",
  "data": {
    "token": "your_token_here",
    "user_id": 1,
    "username": "jaden",
    "email": "jaden@example.com"
  }
}
```



- **Error Response**:



```
{
  "message": "Login failed",
  "errors": {
    "detail": "Invalid email or password"
  }
}
```



------





## **✅ 3. Validate Permission**





- **URL**: /auth/permission

- **Method**: POST

- **Headers**:

  Content-Type: application/json

  Authorization: Token your_token_here

- **Request Body**:



```
{
  "permission": "accounts.view_customuser"
}
```



- **Authorized Response**:



```
{
  "status": "authorized"
}
```



- **Unauthorized Response**:



```
{
  "status": "unauthorized"
}
```





