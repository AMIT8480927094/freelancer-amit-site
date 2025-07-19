from flask import Flask, render_template, request

app = Flask(__name__)

services_data = {
    1: {'title': 'Real Business Service 1', 'description': 'Accurate description of Business & Legal Service 1.', 'price': '1000–1500', 'documents': ['PAN Card', 'Aadhar', 'Business Proof (e.g., Utility Bill, Shop License)'], 'details': 'This is the full detailed explanation of Business & Legal Service 1. It includes what the service is, how it helps a business owner, government requirements, common mistakes, and penalties if not complied with. It demonstrates expertise and builds trust.'},
    2: {'title': 'Real Business Service 2', 'description': 'Accurate description of Business & Legal Service 2.', 'price': '1000–1500', 'documents': ['PAN Card', 'Aadhar', 'Business Proof (e.g., Utility Bill, Shop License)'], 'details': 'This is the full detailed explanation of Business & Legal Service 2. It includes what the service is, how it helps a business owner, government requirements, common mistakes, and penalties if not complied with. It demonstrates expertise and builds trust.'},
    3: {'title': 'Real Business Service 3', 'description': 'Accurate description of Business & Legal Service 3.', 'price': '1000–1500', 'documents': ['PAN Card', 'Aadhar', 'Business Proof (e.g., Utility Bill, Shop License)'], 'details': 'This is the full detailed explanation of Business & Legal Service 3. It includes what the service is, how it helps a business owner, government requirements, common mistakes, and penalties if not complied with. It demonstrates expertise and builds trust.'},
    4: {'title': 'Real Business Service 4', 'description': 'Accurate description of Business & Legal Service 4.', 'price': '1000–1500', 'documents': ['PAN Card', 'Aadhar', 'Business Proof (e.g., Utility Bill, Shop License)'], 'details': 'This is the full detailed explanation of Business & Legal Service 4. It includes what the service is, how it helps a business owner, government requirements, common mistakes, and penalties if not complied with. It demonstrates expertise and builds trust.'},
    5: {'title': 'Real Business Service 5', 'description': 'Accurate description of Business & Legal Service 5.', 'price': '1000–1500', 'documents': ['PAN Card', 'Aadhar', 'Business Proof (e.g., Utility Bill, Shop License)'], 'details': 'This is the full detailed explanation of Business & Legal Service 5. It includes what the service is, how it helps a business owner, government requirements, common mistakes, and penalties if not complied with. It demonstrates expertise and builds trust.'},
    6: {'title': 'Real Business Service 6', 'description': 'Accurate description of Business & Legal Service 6.', 'price': '1000–1500', 'documents': ['PAN Card', 'Aadhar', 'Business Proof (e.g., Utility Bill, Shop License)'], 'details': 'This is the full detailed explanation of Business & Legal Service 6. It includes what the service is, how it helps a business owner, government requirements, common mistakes, and penalties if not complied with. It demonstrates expertise and builds trust.'},
    7: {'title': 'Real Business Service 7', 'description': 'Accurate description of Business & Legal Service 7.', 'price': '1000–1500', 'documents': ['PAN Card', 'Aadhar', 'Business Proof (e.g., Utility Bill, Shop License)'], 'details': 'This is the full detailed explanation of Business & Legal Service 7. It includes what the service is, how it helps a business owner, government requirements, common mistakes, and penalties if not complied with. It demonstrates expertise and builds trust.'},
    8: {'title': 'Real Business Service 8', 'description': 'Accurate description of Business & Legal Service 8.', 'price': '1000–1500', 'documents': ['PAN Card', 'Aadhar', 'Business Proof (e.g., Utility Bill, Shop License)'], 'details': 'This is the full detailed explanation of Business & Legal Service 8. It includes what the service is, how it helps a business owner, government requirements, common mistakes, and penalties if not complied with. It demonstrates expertise and builds trust.'},
    9: {'title': 'Real Business Service 9', 'description': 'Accurate description of Business & Legal Service 9.', 'price': '1000–1500', 'documents': ['PAN Card', 'Aadhar', 'Business Proof (e.g., Utility Bill, Shop License)'], 'details': 'This is the full detailed explanation of Business & Legal Service 9. It includes what the service is, how it helps a business owner, government requirements, common mistakes, and penalties if not complied with. It demonstrates expertise and builds trust.'},
    

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html', services=services_data)

@app.route('/service_detail/<int:service_id>')
def service_detail(service_id):
    service = services_data.get(service_id)
    if service:
        return render_template('service_detail.html', service=service)
    return "Service not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port))
