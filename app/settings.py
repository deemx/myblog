import os.path as osp
from django.conf import settings


BASE_DIR = osp.split(osp.dirname(__file__))[0]

settings.configure(
    DEBUG=True,
    ADMINS = (('admin', 'admin@mail.com'),),
    SITE_ID = 1,
    SECRET_KEY='thesecretkey',
    ROOT_URLCONF='app.urls',
    STATIC_ROOT = '',
    STATIC_URL='/static/',
    STATICFILES_DIRS=(
        osp.join(BASE_DIR, 'static'), ),
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ),
    TEMPLATE_DIRS=(
        osp.join(BASE_DIR, 'template'), ),
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'myblogdb',
            'USER': 'mybloguser',
            'PASSWORD': 'root',
        }
    },
    MIDDLEWARE_CLASSES=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',

        'captcha',
        'tinymce',
        'app',
    ),
    WSGI_APPLICATION = 'app.wsgi.application',
)
