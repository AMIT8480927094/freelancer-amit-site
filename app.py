from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# ========================
# List of 75 services
# ========================
services = [
    {
        "id": 1,
        "name": "GST Registration",
        "price": "1000 - 1500",
        "description": "Register your business under GST to comply with Indian tax regulations."
    },
    {
        "id": 2,
        "name": "ITR Filing (Individual)",
        "price": "500 - 1000",
        "description": "Income Tax Return filing for salaried or freelance individuals."
    },
    {
        "id": 3,
        "name": "PVT LTD Company Registration",
        "price": "3000 - 5000",
        "description": "Incorporate your private limited company with MCA filings and PAN/TAN."
    },
    # ...continue like this up to id 75
    {
        "id": 75,
        "name": "Instagram Creator Website Design",
        "price": "1000 - 2000",
        "description": "Custom portfolio site for influencers and creators using HTML/Python."
    }
]

# ========================
# ROUTES
# ========================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def all_services():
    return render_template('services.html', services=services)

@app.route('/service/<int:service_id>')
def service_detail(service_id):
    # Find service by ID
    service = next((s for s in services if s["id"] == service_id), None)
    if not service:
        return "Service not found", 404
    return render_template('service_detail.html', service=service)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html', services=services)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Run app for deployment
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
