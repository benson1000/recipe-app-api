"""Django command to wait for the database to be available"""

"""from typing import Any
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("waiting for database")
        db_up=False
        while db_up is False:
            try:
                self.check(databases=['default'])
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database Unavailable, writing for 1 second")
                time.sleep(1)
                
        self.stdout.write(self.style.SUCCESS("Database available!"))"""