from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy login users (can be expanded to DB later)
users = {'client@example.com': 'password123'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

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
    services_info = {
        # Accounting & Bookkeeping
        "bookkeeping": {"title": "Monthly Bookkeeping", "desc": "Tally or Excel based monthly bookkeeping services.", "price": "₹1,000 – ₹2,000/month"},
        "reconciliation": {"title": "Ledger & Bank Reconciliation", "desc": "Monthly reconciliation of ledger and bank accounts.", "price": "₹500 – ₹1,000/month"},
        "finalaccounts": {"title": "Final Account Preparation", "desc": "Preparation of Profit & Loss and Balance Sheet.", "price": "₹1,500 – ₹3,000"},

        # GST Services
        "gstregistration": {"title": "GST Registration", "desc": "New GST Registration for businesses.", "price": "₹500 – ₹800"},
        "gstfiling": {"title": "GST Return Filing", "desc": "Monthly GSTR-1 & 3B filing services.", "price": "₹300 – ₹700/month"},
        "gstupdate": {"title": "GST Amendment/Cancellation", "desc": "Update or cancel your existing GST registration.", "price": "₹400 – ₹600"},
        "ewaybill": {"title": "E-invoice & E-way Bill Setup", "desc": "Setup for e-invoicing and e-way bills.", "price": "₹300 – ₹500"},
        "itc": {"title": "ITC Reconciliation", "desc": "Reconcile your input tax credit.", "price": "₹500 – ₹800"},

        # Income Tax Services
        "pan": {"title": "PAN/TAN Application", "desc": "Apply for PAN or TAN online.", "price": "₹150 – ₹300"},
        "itr": {"title": "Individual ITR Filing", "desc": "Tax return for salaried individuals.", "price": "₹300 – ₹500"},
        "itrbusiness": {"title": "ITR Filing (Business/Freelancer)", "desc": "Tax return filing for business or freelancers.", "price": "₹600 – ₹1,000"},
        "tds": {"title": "TDS Return Filing", "desc": "Quarterly filing of TDS returns.", "price": "₹600 – ₹1,200/quarter"},
        "advancetax": {"title": "Advance Tax Calculation", "desc": "Calculation of advance tax liabilities.", "price": "₹300"},

        # Business / Startup Registration
        "proprietorship": {"title": "Proprietorship Registration", "desc": "Register a proprietorship firm.", "price": "₹500 – ₹800"},
        "msme": {"title": "MSME / Udyam Registration", "desc": "Register under MSME/Udyam.", "price": "₹300"},
        "fssai": {"title": "FSSAI Registration", "desc": "Food license registration.", "price": "₹500 – ₹700"},
        "startupindia": {"title": "Startup India/DPIIT Registration", "desc": "Get DPIIT/Startup India certificate.", "price": "₹1,000"},
        "shoplicense": {"title": "Shop & Establishment License", "desc": "Local shop & establishment registration.", "price": "₹800 – ₹1,200"},

        # ROC & MCA Filing
        "companyinc": {"title": "Company Incorporation", "desc": "Register a Private Limited Company.", "price": "₹3,000 – ₹5,000"},
        "dsc": {"title": "DIN, DSC Filing", "desc": "Director Identification & DSC services.", "price": "₹500 – ₹800"},
        "roc": {"title": "Annual ROC Filing", "desc": "File AOC-4, MGT-7 with MCA.", "price": "₹1,200 – ₹2,000"},
        "dirkyc": {"title": "Director KYC", "desc": "DIR-3 KYC for company directors.", "price": "₹300"},

        # Payroll & Compliance
        "pfesi": {"title": "PF & ESI Registration", "desc": "Register under PF & ESI.", "price": "₹500 each"},
        "pfesireturn": {"title": "PF/ESI Return Filing", "desc": "Monthly PF and ESI return filing.", "price": "₹300 – ₹600"},
        "salaryslip": {"title": "Salary Slip Preparation", "desc": "Monthly salary slip creation.", "price": "₹200/month per employee"},
        "pt": {"title": "Professional Tax Registration", "desc": "Get your PT certificate from state.", "price": "₹400"},

        # Reports & Business Documents
        "projectreport": {"title": "Project Report for Loan", "desc": "Custom project report for business loan.", "price": "₹1,000 – ₹2,000"},
        "invoice": {"title": "Invoice/Letterhead Design", "desc": "Stylish professional business invoice.", "price": "₹300"},
        "docchecklist": {"title": "Document Checklist Preparation", "desc": "Documents checklist for services.", "price": "₹300"},
        "quotation": {"title": "Quotation Format Creation", "desc": "Create business quotation templates.", "price": "₹300"}
    }

    if name in services_info:
        return render_template("service_details.html", service=services_info[name])
    else:
        return "Service not found", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
