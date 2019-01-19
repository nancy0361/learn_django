# Django Learning Note

## Tutorial Links
This note is taken from the Django official tutorial which is linked below: 
* Tutorial 1: Project Creation:
https://docs.djangoproject.com/en/2.0/intro/tutorial01/
* Tutorial 2: Model Creation & User Management:
https://docs.djangoproject.com/en/2.0/intro/tutorial02/
* Tutorial 3: View Creation:
https://docs.djangoproject.com/en/2.0/intro/tutorial03/

## Useful Commands
1. Under the directory, run this command to create a mysite directory:

`django-admin startproject mysite`

2. Quick start the development server by running (only developing use):

`python3 manage.py runserver`

3. Under the same directory with manage.py, run this command to create a new app:

`python3 manage.py startapp myapp`

4. To create models, run this first:

`python3 manage.py migrate`
> A model is the single, definitive source of truth about your data. 
> It contains the essential fields and behaviors of the data you’re storing.

5. After write new model (or update old ones), update it to migration by:

`python3 manage.py makemigrations polls`

6. To run the Django shell:

`python3 manage.py shell`

