# FastAPI Authentication System

A secure authentication system built with FastAPI, SQLAlchemy, and JWT for user management and authentication.

## Features

- User Registration
- JWT Token Authentication
- Secure Password Hashing
- User Profile Management
- RESTful API Endpoints

## Prerequisites

- Python 3.9 or higher
- pip
- virtualenv

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MAhmadtech/Authentication-with-fastapi-.git
cd Authentication-with-fastapi-
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pydantic
pip install python-jose[cryptography]
pip install passlib[bcrypt]
pip install python-multipart
```

## Project Structure

```
.
├── config.py          # Database configuration
├── main.py            # FastAPI application entry point
├── models/            # Pydantic models
├── routes/            # API routes
├── repository/        # Database operations
├── tables/            # Database table definitions
└── venv/             # Virtual environment
```

## API Endpoints

### User Registration
- **POST /signup**
  - Register a new user with username, password, email, phone number, and name
  - Returns JWT token upon successful registration

### Authentication
- JWT token-based authentication
- Token generation and validation

## Usage

1. Run the application:
```bash
uvicorn main:app --reload
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Security

- Passwords are hashed using bcrypt
- JWT tokens are used for authentication
- Input validation using Pydantic models

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

MAhmadtech