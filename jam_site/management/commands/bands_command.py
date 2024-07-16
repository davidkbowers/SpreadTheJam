from django.core.management.base import BaseCommand
import psycopg2
from ...models import Band


class Command(BaseCommand):
    help = 'migrates bands'

    def handle(self, *args, **kwargs):
        conn = psycopg2.connect(
            host="localhost",
            database="spreadthejam",
            user="postgres",
            password="punter89")
        cursor = conn.cursor()

        try:
            sql = """ SELECT * FROM bands"""
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                band = Band()
                band.name = row[1]
                band.website_url = row[2]
                band.image_url = row[3]
                band.seatgeek_slug = row[4]
                band.save()

        finally:
            conn.close()
