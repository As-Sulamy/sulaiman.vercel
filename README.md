# Portfolio Website - Django

A professional portfolio website built with Django, featuring a dark mode theme with Tailwind CSS.

## Features

- **Project Showcase**: Display projects with images, technologies, and external links
- **Professional Blog**: Markdown-supported technical articles
- **Contact System**: Functional contact form with database storage
- **Admin Dashboard**: Fully configured Django Admin for content management
- **Dark Theme**: Modern, high-end dark mode design with Tailwind CSS

## Tech Stack

- Django 4.2+
- Tailwind CSS (via CDN)
- PostgreSQL/SQLite
- Markdown support with django-markdownx

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` for the website and `http://127.0.0.1:8000/admin` for the admin dashboard.

## Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── projects/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── forms.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── contact.html
│   ├── services.html
│   ├── blog/
│   └── projects/
└── media/
    ├── projects/
    └── blog/
```

## Color Palette

- **Background**: #0f172a (Deep Slate)
- **Text**: #f8fafc (Light)
- **Primary Accent**: #38bdf8 (Sky Blue)
- **Secondary Accent**: #10b981 (Emerald)

## License

MIT License
