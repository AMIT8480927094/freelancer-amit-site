from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy in-memory user store
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
        if email in users:
            return render_template('signup.html', error='Account already exists')
        users[email] = password
        session['user'] = email
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/service/<name>')
def service_detail(name):
    services_info = {
        "gst": {
            "title": "GST Filing",
            "desc": "Monthly or Quarterly GST return filing for businesses and individuals.",
            "price": "₹499",
            "docs": ["PAN Card", "GST Login Details", "Sales & Purchase Data"]
        },
        "itr": {
            "title": "ITR Filing",
            "desc": "Income Tax Return filing for salaried, business & freelancers.",
            "price": "₹399",
            "docs": ["PAN Card", "Form 16 / Income Proof", "Bank Statement"]
        },
        "dsc": {
            "title": "DSC Certificate",
            "desc": "Digital Signature Certificate generation and registration.",
            "price": "₹899",
            "docs": ["PAN Card", "Aadhar Card", "Passport Photo"]
        },
        "web": {
            "title": "Website Design",
            "desc": "Responsive, modern websites with HTML, CSS, Python, and more.",
            "price": "₹1499",
            "docs": ["Your Logo", "Business Info", "Design Reference"]
        }
    }

    if name in services_info:
        return render_template("service_details.html", service=services_info[name])
    else:
        return "Service not found", 404

if __name__ == '__main__':
    app.run(debug=True)
