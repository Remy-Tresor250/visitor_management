# Django User Authentication and Visit Request API

This project is a RESTful API built with **Django** and **Django REST Framework (DRF)**, enabling user authentication, management, and visit request handling. It provides features such as secure token-based authentication and organization-specific visit request tracking.

## Features

- **User Authentication**: Implemented user auth during login.
- **User Management**: User registration and role assignment.
- **Visit Requests**: Create, update, and retrieve visit requests.

## Tech Stack

- **Django**: Web framework for backend development.
- **Django REST Framework (DRF)**: Toolkit for building Web APIs.
- **PSQL**: Default database for development.

## Setup Instructions

### Prerequisites

- Python 3.9 or higher installed on your system.
- A virtual environment setup (optional but recommended).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Remy-Tresor250/visitor_management.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

### Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

#### User Endpoints

- **Register a User**:
  - **POST** `/register/`
  - **Request Body**:

    ```json
    {
      "username": "trex",
      "email": "trex@example.com",
      "password": "trex1234",
      "role": "user"
    }
    ```

- **Login**:
  - **POST** `/`
  - **Request Body**:

    ```json
    {
      "username": "trex",
      "password": "trex1234"
    }
    ```

#### Visit Request Endpoints

- **Create a Visit Request**:
  - **POST** `/visit-requests/`
  - **Request Body**:

    ```json
    {
      "organization_name": "Tech Corp",
      "visit_date": "2024-12-01",
      "visit_start_time": "10:00:00",
      "visit_end_time": "12:00:00"
    }
    ```

- **Get All Visit Requests**:
  - **GET** `/visit-requests/`

### Database Models

- **User**:
  - `id`, `username`, `email`, `password`, `role`
- **VisitRequest**:
  - `id`, `organization_name`, `visit_date`, `visit_start_time`, `visit_end_time`, `status`

### Environment Variables

- `DEBUG`: Set to `True` for development, `False` for production.

### Security

- Passwords are hashed using **bcrypt**.

### Contact

For questions or collaboration, contact:

- **Name**: Remy Tresor
- **Email**: niyitegekatresor@gmail.com
- **GitHub**: [GitHub Profile](https://github.com/Remy-Tresor250)
