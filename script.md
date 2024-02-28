<!-- CREATION PROJET -->
django-admin startproject hopital

<!-- CREATION APPLICATION POUR GERER ENTITE -->
cd hopital
python manage.py startapp medecin
python manage.py startapp patient
python manage.py startapp mdeciament

<!-- DEMARCHE -->
mettre application dans setting.py
INSTALLED_APPS = [
    'medecin',
    'patient',
    'medicament',
]

<!-- EXECUTION -->
python manage.py makemigrations
python manage.py migrate

python manage.py runserver


