# Logs - Blog Posting Web Application

Welcome to **Logs**, a CRUD-based blog posting web application built with Django and Python. This project allows users to Create, Read, Update, and Delete blog posts with ease, using Django's robust backend and a clean user interface.

## Features
- **Create Posts**: Write and publish new blog posts.
- **Read Posts**: View all published blog entries in an organized list or individually.
- **Update Posts**: Edit your existing blog posts.
- **Delete Posts**: Remove unwanted posts from the application.
  
## Prerequisites
Make sure you have the following installed on your system:
- **Python 3.x**
- **Django 4.x**
- **pip** (Python package installer)
  
## Setup & Installation

1. Clone the repository to your local machine:
   ```bash
   https://github.com/Clean8876/Logs.git
   cd Logs
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application in your browser at `http://127.0.0.1:8000/`.

## Usage
Once the server is running, navigate to the homepage where you can:
- View all blog posts
- Add a new blog post
- Edit or delete existing posts by clicking on them
- Manage your posts efficiently using Django's built-in admin panel

## Directory Structure
```
logs/
├── logs/                   # Project settings
├── blog/                   # Main app for blog management
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates for blog
│   ├── models.py           # Database models
│   ├── views.py            # Application logic
│   └── urls.py             # URL routing for blog
├── manage.py               # Django's command-line utility
└── requirements.txt        # Python dependencies
```



## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to use, modify, and contribute to this project! If you encounter any issues, please open a new issue or submit a pull request.
