# **Django Auth API — Usage Guide**





**Base URL**

```
https://auth-service-r1lp.onrender.com
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

- **Permission Type**

accounts.view_customuser

accounts.add_customuser

accounts.change_customuser

accounts.delete_customuser

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



---

## **📋 4. List Users**

- **URL**: /auth/users/

- **Method**: GET

- **Headers**:
  
  Content-Type: application/json  
  Authorization: Token your_token_here

- **Success Response**:

```
[
  {
    "id": 1,
    "username": "jaden",
    "email": "jaden@example.com",
    "phone": "1234567890"
  },
  ...
]
```

- **Error Response**:

```
{
  "detail": "Authentication credentials were not provided."
}
```

---

## **🗑 5. Delete User**

- **URL**: /auth/users/<user_id>/

- **Method**: DELETE

- **Headers**:
  
  Content-Type: application/json  
  Authorization: Token your_token_here (must be an admin)

- **Success Response**:

```
{
  "message": "User with ID <user_id> has been deleted."
}
```

- **Error Response**:

```
{
  "detail": "You do not have permission to perform this action."
}
```
