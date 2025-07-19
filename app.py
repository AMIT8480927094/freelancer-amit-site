from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# ========================
# List of 75 services
# ========================
services = [
    # BUSINESS & LEGAL SERVICES (1–50)
    {"id": 1, "name": "GST Registration", "price": "1000 - 1500", "description": "Register your business under GST to comply with Indian tax regulations."},
    {"id": 2, "name": "ITR Filing (Individual)", "price": "500 - 1000", "description": "Income Tax Return filing for salaried or freelance individuals."},
    {"id": 3, "name": "PVT LTD Company Registration", "price": "3000 - 5000", "description": "Register your private limited company with full documentation."},
    {"id": 4, "name": "Proprietorship Firm Registration", "price": "800 - 1200", "description": "Start your sole proprietorship legally and quickly."},
    {"id": 5, "name": "Partnership Firm Deed Drafting", "price": "1000 - 1500", "description": "Create and register your partnership deed professionally."},
    {"id": 6, "name": "MSME (Udyam) Registration", "price": "500 - 800", "description": "Register under Udyam to avail MSME government benefits."},
    {"id": 7, "name": "Digital Signature Certificate (DSC)", "price": "1000 - 1200", "description": "Get a Class 2 or Class 3 DSC for government filings."},
    {"id": 8, "name": "PAN Card Application", "price": "200 - 300", "description": "Apply for a new PAN card or correction to existing PAN."},
    {"id": 9, "name": "TAN Application", "price": "300 - 500", "description": "Get TAN for tax deduction filings (TDS)."},
    {"id": 10, "name": "PF Registration (Employees)", "price": "800 - 1000", "description": "Register your business for Provident Fund compliance."},
    # ... Services 11 to 49 here (omitted for brevity)
    {"id": 50, "name": "Professional Tax Registration", "price": "500 - 800", "description": "Register your business under state professional tax rules."},

    # WEB DESIGN & DEVELOPMENT SERVICES (51–75)
    {"id": 51, "name": "Static Website (3 Pages)", "price": "1000 - 1500", "description": "Simple 3-page HTML website for individuals or businesses."},
    {"id": 52, "name": "Business Landing Page", "price": "800 - 1000", "description": "A clean, professional landing page for your business."},
    {"id": 53, "name": "Custom Flyer Design (Digital)", "price": "200 - 400", "description": "Eye-catching flyers for promotions or announcements."},
    {"id": 54, "name": "Advertisement Poster (Digital)", "price": "300 - 500", "description": "Design attractive posters for online ads."},
    {"id": 55, "name": "Business ID Card Design", "price": "150 - 250", "description": "Custom employee ID cards for your organization."},
    {"id": 56, "name": "Logo Design (Basic)", "price": "500 - 800", "description": "Clean logo design for startups and freelancers."},
    {"id": 57, "name": "Business Visiting Card Design", "price": "200 - 300", "description": "Professional visiting cards for business contacts."},
    {"id": 58, "name": "HTML-Based Invitation Page", "price": "400 - 600", "description": "Personal event invites with links, images, and RSVP."},
    {"id": 59, "name": "Birthday Frame (Custom HTML)", "price": "300 - 400", "description": "HTML birthday templates for personalized messages."},
    {"id": 60, "name": "Personal Portfolio Website", "price": "1200 - 1500", "description": "HTML + Python portfolio website for freelancers."},
    # ... Services 61 to 74 here (omitted for brevity)
    {"id": 75, "name": "Instagram Creator Website Design", "price": "1000 - 2000", "description": "Custom portfolio site for influencers and creators using HTML/Python."}
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

# ========================
# RUN APP
# ========================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
