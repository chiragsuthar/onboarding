# Customer Onboarding Project

Customer Onboarding Project is a Django application developed for efficient customer onboarding by extracting data from documents using AWS Textract API.

## Overview

The project aims to streamline the customer onboarding process by allowing users to upload documents, extracting relevant data, and creating customer profiles based on the extracted information. It utilizes AWS Textract API for text extraction and Django admin for backend management.

## Features

- User authentication system
- Create customer profiles
- Upload document images
- Extract data from documents using AWS Textract
- Backend management through Django admin
- Responsive and user-friendly interface

## Installation

### Requirements

- Python 3.6+
- Django 3.x
- AWS account (for AWS Textract)

### Setup

1. Clone the repository:
   
   ```
   git clone <repository_url>
   cd customer_onboarding_project
   
3. Create a virtual environment and activate it:
   
   ```
   For Windows
   python -m venv env
   .\env\Scripts\activate

   
   For Linux/mac
   python -m venv env
   source env/bin/activate
   
5. Install dependencies:
   
   ```
   pip install -r requirements.txt
   
7. Configure AWS credentials:
- Set up your AWS credentials in your local environment. You can do this by using AWS CLI (`aws configure`) or setting environment variables.

6. Run migrations:
   
   ```
   python manage.py makemigrations
   python manage.py migrate
   
8. Start the development server:
   
   ```
   python manage.py runserver
   
10. Open your browser and go to `http://127.0.0.1:8000` to access the application.

## Usage

- Upon user login, navigate to the "Create Customer" or "List Customer" menu options.
- Under "Create Customer", select the document type, upload document images, and trigger the API for data extraction.
- The extracted data will be displayed in the Django admin interface under the respective customer profile.
- In the "List Customer" section, view a list of existing customer profiles.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to Mobihive Labs Limited for the project requirements and specifications.
- Inspired by AWS Textract documentation and Django documentation.
