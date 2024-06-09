from typing import Any
from api.models import Faculty
from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    help = 'Load data from CSV file into Faculty table'

    def handle(self, *args: Any, **options: Any) -> str | None:
        with open('/home/rishab/Desktop/lunux/Code/gdsc/profBattle/api/management/commands/research2(1).csv', mode='r') as file:
            csv_reader = csv.reader(file)
            
            next(csv_reader)
            count = 1
            for row in csv_reader:
                print(count)
                Faculty.objects.create(
                    name = row[0],
                    role = row[1],
                    department = row[2],
                    publications = int(row[3]),
                    strict = int(row[4]),
                    skill = int(row[5]),
                    marks = int(row[6]),
                    fit = int(row[7]),
                    ap = int(row[8]),
                    link = row[9]
                )
                count += 1