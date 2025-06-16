# 📝 Django Blog REST API

This is a production-ready Django + DRF REST API for a blog application with:
- JWT Authentication (Register / Login / Logout)
- CRUD for Posts & Comments
- MySQL as database
- DRF browsable API + optional Swagger/OpenAPI docs
- Unit tests for key endpoints
- Deployed on Heroku (free tier)

---

## 🚀 **Live Demo**
👉 [View API](https://YOUR-LIVE-RENDER-URL.onrender.com)  

---

## ⚙️ **Tech Stack**
- Django 4+
- Django REST Framework
- djangorestframework-simplejwt (JWT Auth)
- MySQL
- Gunicorn (for production)
- Heroku (deployment)

---

## 🧑‍💻 **Features**
✅ User registration + JWT login/logout  
✅ Create, list, update, delete posts (auth required)  
✅ Comment on posts (auth required)  
✅ Public view for posts + comments  
✅ DRF browsable API + optional Swagger UI  
✅ Basic tests: auth + post + comment  

---

## 🛠 **Local Setup**
```bash
git clone https://github.com/r-rony08/django-blog-backend/.git
cd django-blog-backend

# create virtual environment
python -m venv venv
# or venv\Scripts\activate on Windows

pip install -r requirements.txt

# configure .env file
# DEBUG=False
# SECRET_KEY=your-secret-key
# DB_NAME=your_db_name
# DB_USER=your_db_user
# DB_PASSWORD=your_db_password
# DB_HOST=127.0.0.1

python manage.py migrate
python manage.py runserver
