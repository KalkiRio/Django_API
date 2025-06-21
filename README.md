# Django API - Task Manager

Live at: https://django-api-cnez.onrender.com

A Django RESTful API project for managing tasks and user accounts, with JWT authentication and modern best practices.

---

## Features

- **User Authentication:** JWT-based user registration and login.
- **Task Management:** CRUD operations for tasks.
- **RESTful APIs:** Built using Django REST Framework.
- **Filtering & Pagination:** Integrated with `django-filter` for flexible data queries.
- **API Documentation:** Swagger/OpenAPI support via `drf-yasg`.
- **CORS Support:** Cross-Origin Resource Sharing enabled.
- **Deployment Ready:** Includes configuration for Render.com deployment.

---

## Project Structure

```
Django_API/
│
├── .env                     # Environment variables (should not be committed)
├── .gitignore               # Standard Git ignore file
├── requirements.txt         # Project-level Python dependencies
├── document.md              # Additional documentation (if present)
│
└── task_manager/
    ├── manage.py                # Django management script
    ├── requirements.txt         # App-level dependencies (duplicate for Render)
    ├── render.yaml              # Render.com deployment configuration
    ├── db.sqlite3               # SQLite DB (for development, not for production)
    ├── accounts/                # Django app for user accounts
    │   ├── models.py            # User models
    │   ├── serializers.py       # DRF serializers for users
    │   ├── views.py             # User-related API views (register, login, etc.)
    │   ├── urls.py              # User API routes
    │   └── ...                  # Other standard Django app files
    ├── tasks/                   # Django app for tasks
    │   ├── models.py            # Task models
    │   ├── serializers.py       # DRF serializers for tasks
    │   ├── views.py             # Task-related API views
    │   ├── urls.py              # Task API routes
    │   └── ...                  # Other standard Django app files
    └── task_manager/            # Main Django project settings
        ├── settings.py          # Main Django settings
        ├── urls.py              # Root URL configuration
        ├── wsgi.py / asgi.py    # WSGI/ASGI application entrypoints
        └── ...
```

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/KalkiRio/Django_API.git
cd Django_API/task_manager
```

### 2. Create and Activate a Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables

- Copy `.env.example` to `.env` (if available) or create a `.env` file.
- Define your `DJANGO_SECRET_KEY`, and other sensitive settings (see `settings.py` for required variables).

### 5. Apply Database Migrations

```sh
python manage.py migrate
```

### 6. Create a Superuser (Optional, for admin interface)

```sh
python manage.py createsuperuser
```

### 7. Run the Development Server

```sh
python manage.py runserver
```

---

## API Usage

- **Swagger/OpenAPI UI:** After running the server, visit [http://localhost:8000/swagger/](http://localhost:8000/swagger/) for interactive API docs.
- **Authentication:** Most API endpoints require JWT authentication. Obtain a token from `/api/token/` or `/api/auth/login/` (see `accounts/urls.py`).

---

## Deployment

Deployment is configured for [Render.com](https://render.com/) via `render.yaml`. Key steps:

- Set environment variables on Render, especially `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `ALLOWED_HOSTS`.
- Use the build and start commands from `render.yaml`:
  - Build: `pip install -r requirements.txt`
  - Start: `gunicorn task_manager.wsgi:application`

---

## Key Dependencies

- Django 5.x
- Django REST Framework
- Simple JWT (`djangorestframework_simplejwt`)
- drf-yasg (Swagger/OpenAPI docs)
- django-cors-headers
- django-filter
- Gunicorn (for production WSGI)
- psycopg2-binary (for PostgreSQL, if moving to production)

See `requirements.txt` for full list.

---

## Contributing

Pull requests are welcome! For significant changes, please open an issue to discuss what you would like to change.

---

## Links

- [View `tasks` app files](https://github.com/KalkiRio/Django_API/tree/main/task_manager/tasks)
- [View `accounts` app files](https://github.com/KalkiRio/Django_API/tree/main/task_manager/accounts)
- [Settings example](https://github.com/KalkiRio/Django_API/blob/main/task_manager/task_manager/settings.py)
