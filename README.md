# multilingual-faq-apiMultilingual FAQ API

A Django-based application that allows managing and displaying Frequently Asked Questions (FAQs) with multilingual support. The application includes a WYSIWYG editor for FAQ answers, automatic translation using the googletrans library, and a REST API to retrieve FAQs in different languages.

Installation

Clone the repository:
git clone https://github.com/Gargi-Giri/multilingual-faq-api.git
cd multilingual-faq-api
Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
Install the required dependencies:
pip install -r requirements.txt
Apply the migrations:
python manage.py migrate
Run the development server:
python manage.py runserver
The app should now be running at http://localhost:8000.

API Usage

The API allows fetching FAQs in multiple languages using the ?lang= query parameter.

Get FAQs in English (default language):
curl http://localhost:8000/api/faqs/
Get FAQs in Hindi:
curl http://localhost:8000/api/faqs/?lang=hi
Get FAQs in Bengali:
curl http://localhost:8000/api/faqs/?lang=bn
Features

WYSIWYG Editor Support: FAQs' answers are editable using django-ckeditor, enabling rich text formatting.
Multilingual Support: Automatic translations of FAQs' questions and answers using 
