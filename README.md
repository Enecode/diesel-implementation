# Diesel-Implementation

A backend server build with with Django Framework that can handle HTTP requests efficiently. The server will receive data from a sensors, validate it, and store it in the database.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Django 3.0.5 or higher
- Django Rest Framework 3.11.0 or higher
- Django Rest Framework JWT 1.11.0 or higher (OPTIONAL)

### Installing

1. Clone the repository

```
git clone https://github.com/Enecode/diesel-implementation.git
```
3. create a virtual environment and activate it (linux)

```
python -m venv venv
```
for windows
```
python -m venv venv
```

activate the virtual environment (linux)

```
source venv/bin/activate
```

for windows
```
venv\Scripts\activate
```

1. Install the requirements

```
pip install -r requirements.txt
```

3. Run the server

```
python manage.py runserver
```

## Running the tests

1. Run the tests

```
python manage.py test
```

## Built With ❤️ using Django Rest Framework

- [Django](https://www.djangoproject.com/) - The web framework used
- [Django Rest Framework](https://www.django-rest-framework.org/) - The REST API framework used

## Author

- **Jacob Isah** - [Enecode](https://github.com/Enecode/)
