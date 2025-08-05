# django_blog_app

A modern Django starter project with a beautiful, responsive frontend powered by Tailwind CSS and Lucide icons. This app provides a robust backend using Django and a clean structure for rapid development of your next blog or web application.

## Features

- Django 5.2+ backend
- SQLite database (default, easy to swap)
- Responsive UI with Tailwind CSS
- Lucide icons for a modern look
- Ready-to-extend app structure (`pages` app included)
- Example templates for landing and feature pages

## Getting Started

### Prerequisites

- Python 3.10+
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (recommended)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/django_blog_app.git
   cd django_blog_app
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv virtual
   source virtual/Scripts/activate  # On Windows: virtual\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install django
   ```

4. **Run migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Visit:**  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure

- `mysite/` – Django project settings and configuration
- `pages/` – Example Django app (add your models, views, etc.)
- `templates/pages/` – HTML templates (landing page, etc.)
- `db.sqlite3` – Default SQLite database (excluded from version control)
- `virtual/` – Virtual environment (excluded from version control)

## Customization

- Add your own apps in the project directory.
- Update templates in `templates/pages/`.
- Configure static files and media in `mysite/settings.py`.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


