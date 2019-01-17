# Django Learning Note

This note is taken from the Django official tutorial: https://docs.djangoproject.com/en/2.0/intro/tutorial01/

## Project Creation
1. Under the directory, run this command to create a mysite directory:
`django-admin startproject mysite`

2. Quick start the development server by running (only developing use):
`python3 manage.py runserver`

3. Under the same directory with manage.py, run this command to create a new app:
`python3 manage.py startapp myapp`

4. To use the database/models, run this first:
`python3 manage.py migrate`
> A model is the single, definitive source of truth about your data. 
> It contains the essential fields and behaviors of the data you’re storing.

