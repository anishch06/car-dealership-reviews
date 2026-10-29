# Car Dealership Reviews — Capstone Mockup

> **Demo/mock project:** this is a runnable local starter with fictional dealer data. It is not proof that a real cloud deployment, GitHub Actions run, or course submission has succeeded.

## Project name
Car Dealership Reviews

## What is included
- Django JSON API for dealers, dealer reviews, car makes/models, sentiment demo, and session login/logout.
- Simple frontend pages under `server/frontend/static/`.
- cURL commands and **sample/mock outputs** in `submission_evidence/`.
- A GitHub Actions workflow that runs Django checks.
- Local URL placeholders for screenshots and deployment URL documentation.

## Run locally (Windows / macOS / Linux)
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000/ . Admin login is at `/admin/`; create a superuser with:
```bash
python manage.py createsuperuser
```
Do not use a real password in screenshots or commit credentials.

## API endpoints
- `GET /api/dealers/` — all dealers
- `GET /api/dealers/<id>/` — one dealer
- `GET /api/dealers/state/Kansas/` — dealers in Kansas
- `GET /api/dealers/<id>/reviews/` — reviews for a dealer
- `GET /api/cars/` — makes and models
- `POST /api/analyze-review/` — demo sentiment for JSON `{"review":"Fantastic services"}`
- `POST /api/login/` — JSON `{"username":"demo","password":"demo123"}` (demo account only if created as described below)
- `POST /api/logout/` — logout current session

## Create a demo user
```bash
python manage.py shell
```
Then:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.filter(username="demo").delete()
User.objects.create_user(username="demo", password="demo123")
exit()
```

## GitHub
Create an empty public repository on GitHub, then from this folder run:
```bash
git init
git add .
git commit -m "Add car dealership reviews capstone mockup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```
Replace the placeholder URL with your own repository. This README does not contain a real public GitHub URL until you push it.

## Cloud deployment
The included `deploymentURL` is a placeholder. Deploying Django to a real provider requires a configured host, database, environment variables, and a production server. Do not submit a placeholder as a real deployment URL.

## Add fictional demo data
After migrations, run:
```bash
python manage.py seed_demo
```
This creates a few fictional dealers and a sample review so the home page and APIs have data.
