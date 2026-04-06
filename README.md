# Finance-Backend-API
A FastAPI-based backend application for managing users and financial records with full CRUD operations, built using SQLAlchemy and Pydantic, featuring interactive API documentation via Swagger UI.
Finance Backend API

This is a FastAPI-based backend application developed as part of an assessment project.  
It provides RESTful APIs to manage users and their financial records (income/expenses).  
The project demonstrates clean backend architecture, database modeling, and API development using modern Python frameworks.


Features-

-  User Management (Create, Read, Update, Delete)
-  Financial Records Management (Income & Expenses)
-  Data validation using Pydantic schemas
-  Database integration using SQLAlchemy ORM
-  High-performance backend with FastAPI
-  Auto-generated API documentation (Swagger UI & ReDoc)
-  Modular project structure (scalable and maintainable)


Tech Stack-

- Backend Framework: FastAPI  
- Language: Python 3.8+  
- Database: SQLite (default, can be switched to PostgreSQL/MySQL)  
- ORM: SQLAlchemy  
- Validation: Pydantic  
- Server: Uvicorn  


Project Structure-

finance-backend/
│
├── app/
│ ├── main.py # Application entry point
│ ├── models.py # SQLAlchemy ORM models
│ ├── schemas.py # Pydantic schemas for validation
│ ├── database.py # Database connection & session
│ │
│ ├── routes/
│ │ ├── users.py # User-related APIs
│ │ └── records.py # Financial record APIs
│ │
│ └── utils/ # Helper functions (if any)
│
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── venv/ # Virtual environment (not included in GitHub)



Installation & Setup

Follow the steps below to run the project locally:

1. Clone the Repository

bash:
git clone https://github.com/your-username/finance-backend.git
cd finance-backend
2. Create a Virtual Environment

bash:
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3. Install Dependencies
bash:
pip install -r requirements.txt
4. Run the Application
bash:
uvicorn app.main:app --reload

API Documentation

Once the server is running, open your browser and visit:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

These provide interactive API documentation where you can test endpoints directly.



