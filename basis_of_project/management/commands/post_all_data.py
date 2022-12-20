from django.core.management.base import BaseCommand, CommandError
from handbook.models import TypeKey, Key, Owner, Source, STATUS, Note
from faker import factory, Faker

from home_page.models import Home
from about_me_page.models import TextAboutMe, PersonalInformation, Services
from resume_page.models import Skills, Education, Experience

from basis_of_project.utils import STATUS_CHOICES
import sqlite3

models = [Home, TextAboutMe, PersonalInformation, Services, Skills, Education, Experience]


class Command(BaseCommand):
    # https: // docs.djangoproject.com / en / 4.1 / howto / custom - management - commands /
    help = 'Fill'

    #
    # def add_arguments(self, parser):
    #     parser.add_argument('model_name', nargs='+', type=str)

    def get_data_from_old(self, table_name):
        con = sqlite3.connect("copySQLite/db.sqlite3")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        sql_data = cursor.fetchall()
        return sql_data

    def fill_data(self, model):
        old_data = self.get_data_from_old('home_page_home')
        for row in old_data:
            try:
                if model.__name__ == 'Home':
                    add_new = model(title_en=row[1], status=row[4])
                    add_new.save()
                    print(row)
            except:
                pass

    def handle(self, *args, **options):
        # if options["model_name"][0] in model_names:
        for model in models:
            self.fill_data(model)

        self.stdout.write(self.style.SUCCESS('Successfully created models'))
