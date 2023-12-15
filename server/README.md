# Django

Back-End with Django 🚀

Currently, 8 official plugins are available:

-   [django](https://github.com/django/django) The Web framework for perfectionists with deadlines 🚀

-   [django-rest-framework](https://github.com/encode/django-rest-framework/tree/master) Web APIs for Django 🎸

-   [django-cors-headers](https://github.com/adamchainz/django-cors-headers) Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS) ⚙️

-   [python-dotenv](https://github.com/theskumar/python-dotenv) Reads key-value pairs from a `.env` file and can set them as environment variables. It helps in developing applications following the 12-factor principles. ⚙️

-   [Pillow](https://github.com/python-pillow/Pillow) Python Imaging Library (Fork) 🎑

-   [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar/) A configurable set of panels that display various debug information about the current request/response. 🔍🐛

-   [djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt) A JSON Web Token authentication plugin for the Django REST Framework. 🩹

-   [drf-yasg](https://github.com/axnsan12/drf-yasg/) Automated generation of real Swagger/OpenAPI 2.0 schemas from Django REST Framework code. ⌛

## Getting Started

Create a new environment

```bash
py -m venv .venv
```

Active environment

```bash
.venv\Scripts\activate.bat
```

Install from file requirements.txt

```bash
pip install -r requirements.txt
```

Migrate

```bash
py manage.py makemigrations
py manage.py migrate
```

Run the start server

```bash
py manage.py runserver
```

Create superuser

```bash
py manage.py createsuperuser
```

Create `.env` file

```bash
SECRET_KEY=your_secret_key
```
