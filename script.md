<!-- CREATION PROJET -->
django-admin startproject hopital

<!-- CREATION APPLICATION POUR GERER ENTITE -->
cd hopital
python manage.py startapp medecin
python manage.py startapp patient
python manage.py startapp mdeciament

<!-- CONFIGURATION BASE -->
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hopital',
        'USER': 'postgres',
        'PASSWORD': 'Mano-123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
<!-- AUTRE DEMARCHE -->
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


