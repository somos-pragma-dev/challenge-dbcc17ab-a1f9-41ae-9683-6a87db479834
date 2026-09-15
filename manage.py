#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv)


def check_environment():
    """Verify that the environment is properly configured."""
    required_vars = ['DJANGO_SETTINGS_MODULE']
    missing = [var for var in required_vars if not os.environ.get(var)]
    
    if missing:
        print(f"Warning: Missing environment variables: {', '.join(missing)}")
        return False
    return True


def run_migrations():
    """Execute database migrations."""
    print("Running migrations...")
    execute_from_command_line(['manage.py', 'migrate', '--verbosity=2'])


def create_superuser():
    """Create an admin superuser interactively."""
    print("Creating superuser...")
    execute_from_command_line(['manage.py', 'createsuperuser'])


def run_tests():
    """Run the test suite."""
    print("Running tests...")
    execute_from_command_line(['manage.py', 'test', '--verbosity=2'])


def collect_static_files():
    """Collect static files to the configured directory."""
    print("Collecting static files...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])


def check_system():
    """Perform system checks to identify configuration issues."""
    print("Performing system checks...")
    execute_from_command_line(['manage.py', 'check'])


def show_urls():
    """Display all URL routes in the application."""
    print("Available URL patterns:")
    execute_from_command_line(['manage.py', 'show_urls'])


def make_migrations(app_name=None):
    """Create new migrations based on model changes."""
    if app_name:
        print(f"Creating migrations for {app_name}...")
        execute_from_command_line(['manage.py', 'makemigrations', app_name])
    else:
        print("Creating migrations for all apps...")
        execute_from_command_line(['manage.py', 'makemigrations'])


def shell_plus():
    """Open Django shell with extended features."""
    try:
        from django_extensions.management import shell_plus
        shell_plus()
    except ImportError:
        print("django-extensions not installed. Using default shell.")
        execute_from_command_line(['manage.py', 'shell'])


def get_project_root():
    """Return the absolute path to the project root directory."""
    return Path(__file__).resolve().parent


def setup_django_environ():
    """Configure Django environment settings."""
    root = get_project_root()
    
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    os.environ.setdefault('DJANGO_SECRET_KEY', os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-key-change-in-production'))
    os.environ.setdefault('DEBUG', os.environ.get('DEBUG', 'True'))


def run_server(host='127.0.0.1', port=8000, reload=True):
    """Start the development server."""
    cmd = ['manage.py', 'runserver', f'{host}:{port}']
    if reload:
        cmd.append('--noreload')
    
    subprocess.run(cmd)


def database_command(command):
    """Execute a database management command."""
    valid_commands = ['migrate', 'makemigrations', 'showmigrations', 'dbshell', 'flush']
    
    if command not in valid_commands:
        print(f"Invalid database command. Valid options: {', '.join(valid_commands)}")
        return
    
    execute_from_command_line(['manage.py', command])


if __name__ == '__main__':
    setup_django_environ()
    
    if not check_environment():
        sys.exit(1)
    
    main()