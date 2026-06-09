# Portfolio Website

A personal portfolio website built with **Django**, **Bootstrap**, and custom **CSS/JavaScript** to showcase my background, technical skills, projects, certifications, and contact information.

This project is designed to serve as a professional online presence and includes a working contact form with email functionality, as well as a light/dark theme toggle for a better user experience.

## Features

- Responsive portfolio layout built with Bootstrap
- Dedicated sections for:
  - About Me
  - Technical Skills
  - Projects
  - Qualifications and Certifications
  - Contact Information
- Contact form powered by Django forms
- Email sending via Gmail SMTP
- Light/Dark mode toggle with theme preference saved in `localStorage`
- Custom styling and static assets

## Tech Stack

- **Backend:** Django 6
- **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
- **Database:** SQLite (development)
- **Configuration:** python-dotenv
- **Deployment target:** PythonAnywhere

## Project Structure

```text
week_1/
├── README.md
└── portfolio/
    ├── manage.py
    ├── requirements.txt
    ├── config/
    ├── main/
    ├── static/
    └── templates/
```

## Key Application Functionality

### Contact Form
The contact form is defined in `portfolio/main/forms.py` and rendered on the homepage. When a user submits the form:

1. The request is handled in `portfolio/main/views.py`
2. Django validates the submitted data
3. An email is sent using the configured SMTP settings
4. A success message is shown after redirecting back to the homepage

### Theme Toggle
The theme toggle script in `portfolio/static/js/script.js`:

- loads the user’s saved theme from `localStorage`
- applies the theme using the `data-bs-theme` attribute
- updates the toggle button label dynamically
- saves any new preference when the user switches themes

## Local Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd portfolio
```

### 2. Create and activate a virtual environment

**Windows (cmd):**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file inside the `portfolio` directory and add your email credentials:

```env
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-app-password
```

> Note: If you are using Gmail, you will usually need an **App Password** instead of your normal account password.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Environment and Email Configuration

This project uses `python-dotenv` to load environment variables from a `.env` file.

The Django settings currently use:

- `EMAIL_HOST = "smtp.gmail.com"`
- `EMAIL_PORT = 587`
- `EMAIL_USE_TLS = True`
- `EMAIL_HOST_USER` from environment variables
- `EMAIL_HOST_PASSWORD` from environment variables

For production, sensitive values should never be hardcoded and should always be managed through environment variables.

## Deployment

This project is intended to be deployed on **PythonAnywhere**.

At a high level, deployment will involve:

1. Uploading or cloning the repository to PythonAnywhere
2. Creating a virtual environment
3. Installing dependencies from `requirements.txt`
4. Setting environment variables for email credentials
5. Configuring the web app to point to the Django project
6. Setting up static files correctly

Because this project uses Django views, forms, and SMTP email functionality, **PythonAnywhere is a more suitable deployment platform than GitHub Pages**.

## Future Improvements

- Add project screenshots to the README
- Improve contact form feedback with Bootstrap alerts instead of browser alerts
- Add production settings for deployment
- Add tests for form submission behavior
- Add a custom domain when deployed

## Author

**Mathew Meisinger**

- GitHub: <https://github.com/MathewMeisinger>
- LinkedIn: <https://www.linkedin.com/in/mathew-meisinger-3b163bb3/>
