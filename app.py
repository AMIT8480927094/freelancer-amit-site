from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy users (for login)
users = {'client@example.com': 'password123'}

# All 30+ services dictionary
services = {
    "bookkeeping": {
        "title": "Monthly Bookkeeping",
        "desc": "Tally or Excel based monthly bookkeeping services.",
        "price": "₹1,000 – ₹2,000/month"
    },
    "reconciliation": {
        "title": "Ledger & Bank Reconciliation",
        "desc": "Monthly reconciliation of ledger and bank accounts.",
        "price": "₹500 – ₹1,000/month"
    },
    "finalaccounts": {
        "title": "Final Account Preparation",
        "desc": "Preparation of P&L and Balance Sheet.",
        "price": "₹1,500 – ₹3,000"
    },
    "gstregistration": {
        "title": "GST Registration",
        "desc": "New GST Registration for businesses.",
        "price": "₹500 – ₹800"
    },
    "gstfiling": {
        "title": "GST Return Filing",
        "desc": "Monthly GSTR-1 & 3B filing services.",
        "price": "₹300 – ₹700/month"
    },
    "gstupdate": {
        "title": "GST Amendment/Cancellation",
        "desc": "Update or cancel your existing GST registration.",
        "price": "₹400 – ₹600"
    },
    "ewaybill": {
        "title": "E-invoice & E-way Bill Setup",
        "desc": "Configuration for e-invoicing and e-way bills.",
        "price": "₹300 – ₹500"
    },
    "itc": {
        "title": "ITC Reconciliation",
        "desc": "Reconcile your input tax credit with GSTR-2A.",
        "price": "₹500 – ₹800"
    },
    "pan": {
        "title": "PAN/TAN Application",
        "desc": "Get your PAN or TAN quickly and easily.",
        "price": "₹150 – ₹300"
    },
    "itr": {
        "title": "Individual ITR Filing (Salaried)",
        "desc": "ITR filing for salaried individuals.",
        "price": "₹300 – ₹500"
    },
    "itrbusiness": {
        "title": "ITR Filing (Business/Freelancer)",
        "desc": "Tax return filing for businesses and freelancers.",
        "price": "₹600 – ₹1,000"
    },
    "tds": {
        "title": "TDS Return Filing",
        "desc": "Quarterly TDS return filing.",
        "price": "₹600 – ₹1,200/quarter"
    },
    "advancetax": {
        "title": "Advance Tax Calculation",
        "desc": "Plan and calculate advance tax liability.",
        "price": "₹300"
    },
    "proprietorship": {
        "title": "Proprietorship Registration",
        "desc": "Register your business as a proprietorship.",
        "price": "₹500 – ₹800"
    },
    "msme": {
        "title": "MSME / Udyam Registration",
        "desc": "Micro, Small & Medium Enterprise registration.",
        "price": "₹300"
    },
    "fssai": {
        "title": "FSSAI Registration",
        "desc": "Get your food license online.",
        "price": "₹500 – ₹700"
    },
    "startupindia": {
        "title": "Startup India/DPIIT Registration",
        "desc": "Register under Startup India & DPIIT.",
        "price": "₹1,000"
    },
    "shoplicense": {
        "title": "Shop & Establishment License",
        "desc": "Legal license for shop/business premises.",
        "price": "₹800 – ₹1,200"
    },
    "companyinc": {
        "title": "Company Incorporation (with CA/CS)",
        "desc": "Incorporate your private limited company.",
        "price": "₹3,000 – ₹5,000"
    },
    "dsc": {
        "title": "DIN, DSC Filing",
        "desc": "Director Identification & Digital Signature Certificate.",
        "price": "₹500 – ₹800"
    },
    "roc": {
        "title": "Annual ROC Filing",
        "desc": "Annual ROC filing including AOC-4, MGT-7 etc.",
        "price": "₹1,200 – ₹2,000"
    },
    "dirkyc": {
        "title": "Director KYC",
        "desc": "DIR-3 KYC submission for directors.",
        "price": "₹300"
    },
    "pfesi": {
        "title": "PF & ESI Registration",
        "desc": "Register under Provident Fund and ESI.",
        "price": "₹500 each"
    },
    "pfesireturn": {
        "title": "PF/ESI Return Filing",
        "desc": "Monthly filing for PF and ESI returns.",
        "price": "₹300 – ₹600"
    },
    "salaryslip": {
        "title": "Salary Slip Preparation",
        "desc": "Generate monthly employee salary slips.",
        "price": "₹200/month per employee"
    },
    "pt": {
        "title": "Professional Tax Registration",
        "desc": "Apply for state PT registration.",
        "price": "₹400"
    },
    "projectreport": {
        "title": "Project Report for Loan",
        "desc": "Customized loan/project reports for banks.",
        "price": "₹1,000 – ₹2,000"
    },
    "invoice": {
        "title": "Invoice/Letterhead Design",
        "desc": "Professional invoice/letterhead design.",
        "price": "₹300"
    },
    "docchecklist": {
        "title": "Document Checklist Preparation",
        "desc": "Get ready checklists for your business filings.",
        "price": "₹300"
    },
    "quotation": {
        "title": "Quotation Format Creation",
        "desc": "Custom quotation templates for your business.",
        "price": "₹300"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services_page():
    return render_template('services.html', services=services_info)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html', services=services)

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service/<name>')
def service_detail(name):
    if name in services:
        return render_template("service_details.html", service=services[name])
    else:
        return "Service not found", 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email] == password:
            session['user'] = email
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email not in users:
            users[email] = password
            session['user'] = email
            return redirect(url_for('home'))
        else:
            return render_template('signup.html', error='User already exists')
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
