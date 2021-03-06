#!/usr/bin/env python
import os
import sys
import django
from app import settings


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    django.setup()
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
