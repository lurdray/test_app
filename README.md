# test_app API

## Overview
The `test_app` API provides a robust interface for [briefly describe the main functionality, e.g., managing financial transactions, user data, etc.]. This API is designed to facilitate seamless integration with [mention any specific services or functionalities].

## Live API Documentation
You can access the live API documentation at the following URL:
[API Documentation](https://test-money.fyber.site/swagger/)

##Test Users with available balance
username: ray
password: 0000

username: henry
password: 0000

## GitHub Repository
The source code for this project is available on GitHub:
[GitHub Repository](https://github.com/lurdray/test_app.git)

## Getting Started Locally

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/lurdray/test_app.git
   cd test_app/test_app/
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

4. **Collect Static Files**
   ```bash
   python3 manage.py collectstatic
   ```

5. **Start the Development Server**
   ```bash
   python3 manage.py runserver
   ```

## Running Tests
To execute the test suite, use the following command:
```bash
python3 manage.py test
 ```
