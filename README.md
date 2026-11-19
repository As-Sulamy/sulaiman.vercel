# Portfolio Website - Django

A professional portfolio website built with Django, featuring matching dark and light themes across the public site and its content dashboard.

## Features

- **Project Showcase**: Display projects with images, technologies, and external links
- **Professional Blog**: Markdown-supported technical articles
- **Contact System**: Functional contact form with database storage
- **Admin Dashboard**: Responsive content dashboard with matching dark and light themes
- **Theme Toggle**: Persistent dark/light mode shared between the public site and admin
- **Inspiration Tree**: An animated tree with five fixed branches for up to five inspirations

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
python manage.py migrate
```

Migrations require a reachable MongoDB instance and are not part of the static asset build.

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` for the website and `http://127.0.0.1:8000/admin` for the admin dashboard.

The Vercel static build copies files from `media/` into its static output and serves them under `/media/`, independently of MongoDB. Add and commit any images, documents, or other media that must ship with the deployment. Django admin uploads written to the server's local filesystem are not durable on Vercel and are not automatically included in future deployments. Database-backed pages still need MongoDB to render their content; this only makes the media files independently available.

### Paystack Support

The Support Me bar and checkout modal use Paystack Checkout and verify completed payments on the server. Configure the encryption key before entering your Paystack secret in Django Admin.

Generate a long random Django key:
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Set it in local PowerShell before starting Django:
```powershell
$env:DJANGO_SECRET_KEY = "your-generated-django-secret"
python manage.py runserver
```

For Vercel, add `DJANGO_SECRET_KEY` under the project's Environment Variables and redeploy. Keep it stable: it encrypts the Paystack secret stored in the database.

Then open Django Admin → **Paystack & Support Settings**:
- Create the single settings record.
- Add your Paystack **secret key** there. It is encrypted before storage and is never displayed again.
- Adjust the suggested naira amounts or disable support checkout as needed.
- Use a Paystack test key for testing and a live key only in production.

Do not commit Paystack credentials or your `DJANGO_SECRET_KEY` to source control. The older `PAYSTACK_SECRET_KEY` environment variable remains supported as a fallback for existing deployments.

Your profile and About details are editable in Admin under **Profile**. Add up to five people under **Inspirations**; enter their short biography in **About / biography**, what you learned from them in **Why they inspire me**, and an optional image credit. Their portraits fill fixed branch positions in the animated tree, with unused branches remaining visible. Your profile remains at the root, and selecting a node opens its details. The admin dashboard shares the site's saved dark/light theme preference. Project inquiries from the separate **Hire Me** form are saved in Admin under **Hire Me Inquiries**.

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
