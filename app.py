from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session management

# ✅ Define all services here (30 total)
services_info = {
    "bookkeeping": {"title": "Monthly Bookkeeping", "desc": "Tally or Excel based monthly bookkeeping services.", "price": "₹1,000 – ₹2,000/month"},
    "reconciliation": {"title": "Ledger & Bank Reconciliation", "desc": "Monthly reconciliation of ledger and bank accounts.", "price": "₹500 – ₹1,000/month"},
    "finalaccounts": {"title": "Final Account Preparation", "desc": "Profit & Loss and Balance Sheet creation.", "price": "₹1,500 – ₹3,000"},
    "gstregistration": {"title": "GST Registration", "desc": "GST registration for businesses.", "price": "₹500 – ₹800"},
    "gstfiling": {"title": "GST Return Filing", "desc": "GSTR-1 & 3B monthly filing.", "price": "₹300 – ₹700/month"},
    "gstupdate": {"title": "GST Amendment/Cancellation", "desc": "Update or cancel GST registration.", "price": "₹400 – ₹600"},
    "ewaybill": {"title": "E-invoice & E-way Bill Setup", "desc": "Setup of e-invoice and e-way bills.", "price": "₹300 – ₹500"},
    "itc": {"title": "ITC Reconciliation", "desc": "Input tax credit reconciliation.", "price": "₹500 – ₹800"},
    "pan": {"title": "PAN/TAN Application", "desc": "Apply for PAN or TAN.", "price": "₹150 – ₹300"},
    "itr": {"title": "Individual ITR Filing", "desc": "ITR for salaried individuals.", "price": "₹300 – ₹500"},
    "itrbusiness": {"title": "ITR Filing (Business/Freelancer)", "desc": "Tax return filing for business/freelancer.", "price": "₹600 – ₹1,000"},
    "tds": {"title": "TDS Return Filing", "desc": "Quarterly TDS returns.", "price": "₹600 – ₹1,200/quarter"},
    "advancetax": {"title": "Advance Tax Calculation", "desc": "Tax estimation and planning.", "price": "₹300"},
    "proprietorship": {"title": "Proprietorship Registration", "desc": "Start your own proprietorship firm.", "price": "₹500 – ₹800"},
    "msme": {"title": "MSME / Udyam Registration", "desc": "Micro/small business registration.", "price": "₹300"},
    "fssai": {"title": "FSSAI Registration", "desc": "Food license registration.", "price": "₹500 – ₹700"},
    "startupindia": {"title": "Startup India/DPIIT Registration", "desc": "Register under Startup India.", "price": "₹1,000"},
    "shoplicense": {"title": "Shop & Establishment License", "desc": "Get your shop license legally.", "price": "₹800 – ₹1,200"},
    "companyinc": {"title": "Company Incorporation", "desc": "Register a Pvt Ltd company.", "price": "₹3,000 – ₹5,000"},
    "dsc": {"title": "DIN, DSC Filing", "desc": "Digital Signature & DIN for directors.", "price": "₹500 – ₹800"},
    "roc": {"title": "Annual ROC Filing", "desc": "MCA forms like AOC-4, MGT-7.", "price": "₹1,200 – ₹2,000"},
    "dirkyc": {"title": "Director KYC", "desc": "DIR-3 KYC filing.", "price": "₹300"},
    "pfesi": {"title": "PF & ESI Registration", "desc": "Get PF and ESI for employees.", "price": "₹500 each"},
    "pfesireturn": {"title": "Monthly PF/ESI Return Filing", "desc": "Monthly compliance returns.", "price": "₹300 – ₹600"},
    "salaryslip": {"title": "Salary Slip Preparation", "desc": "Monthly slips for employees.", "price": "₹200/employee"},
    "pt": {"title": "Professional Tax Registration", "desc": "Register for PT in your state.", "price": "₹400"},
    "projectreport": {"title": "Project Report for Loan", "desc": "Custom reports for bank loan.", "price": "₹1,000 – ₹2,000"},
    "invoice": {"title": "Invoice/Letterhead Design", "desc": "Professional invoice design.", "price": "₹300"},
    "docchecklist": {"title": "Document Checklist Preparation", "desc": "Checklist for your services.", "price": "₹300"},
    "quotation": {"title": "Quotation Format Creation", "desc": "Quotation formats for clients.", "price": "₹300"},
}

# Dummy users (for login/signup)
users = {'client@example.com': 'password123'}

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services_page():
    return render_template('services.html', services=services_info)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html', services=services_info)

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

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

@app.route('/service/<name>')
def service_detail(name):
    if name in services_info:
        return render_template("service_details.html", service=services_info[name])
    else:
        return "Service not found", 404

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
