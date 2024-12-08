## Django CRM App

A basic CRM (Customer Relationship Management) application built using Django. This personal project showcases fundamental CRUD operations, user authentication, and a simple interface for managing customers and their details.

### Features

- User Authentication:

- Regsiter, login and logout functionality for secure access.

- CRUD Operations:

- Create, Read, Update, and Delete customer records.

- User Management:

- Only authenticated users can access the CRM dashboard.

- Responsive Design:

- Simple and clean interface for ease of use.

Technologies Used:

- Backend: Django (Python)

- Database: MySQL

- Frontend: Django templates, HTML, CSS and Bootstrap

### Installation

Follow these steps to set up the project locally:

1. Clone the repository:

```bash
git clone https://github.com/Carlos-860/django-crm.git
cd django-crm
```

2. Create a virtual environment

Note: You must activate the virtual environment every time you open the command prompt to work on your project.

```bash
python -m venv venv

source venv/bin/activate # on Linux/MacOS
source venv\Scripts\activate # on Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply migrations

```bash
python manage.py migrate
```

5. Create a superuser (for admin access):

```bash
python manage.py createsuperuser
```

6. Start the server:

```bash
python manage.py runserver
```

7. Access the app: Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Usage

- Log in with your credentials to access the CRM dashboard.
- Use the interface to manage customers:
- Create: Add new customer details.
- Read: View customer records.
- Update: Edit existing customer information.
- Delete: Remove customer records.

For administrative features, visit the Django admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)..