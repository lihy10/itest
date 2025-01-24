import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autotest_platform.settings')
django.setup()

if __name__ == '__main__':
    from daphne.cli import CommandLineInterface
    CommandLineInterface.entrypoint(['-b', '0.0.0.0', '-p', '8000', 'autotest_platform.asgi:application']) 