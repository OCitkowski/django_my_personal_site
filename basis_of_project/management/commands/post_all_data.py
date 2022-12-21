from django.core.management.base import BaseCommand, CommandError
from handbook.models import TypeKey, Key, Owner, Source, STATUS, Note
from faker import factory, Faker

from home_page.models import Home
from about_me_page.models import TextAboutMe, PersonalInformation, Services
from resume_page.models import Skills, Education, Experience

from basis_of_project.utils import STATUS_CHOICES
import sqlite3

models = {Home: 'home_page_home',
          TextAboutMe: 'about_me_page_textaboutme',
          PersonalInformation: 'about_me_page_personalinformation',
          Services: 'about_me_page_services',
          Skills: 'resume_page_skills',
          Education: 'resume_page_education',
          Experience: 'resume_page_experience',
          }


class Command(BaseCommand):
    # https: // docs.djangoproject.com / en / 4.1 / howto / custom - management - commands /
    help = 'Fill'

    def get_data_from_old(self, table_name):

        con = sqlite3.connect("copySQLite/db.sqlite3")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        sql_data = cursor.fetchall()
        return sql_data

    def fill_data(self, model, old_data):
        for row in old_data:
            try:
                if model.__name__ == 'Home':
                    add_new = model(title_en=row[1], status=row[4])
                    add_new.save()
                    print(row, model.__name__)

                if model.__name__ == 'TextAboutMe':
                    add_new = model(text=row[1], title=row[2])
                    add_new.save()
                    print(row, model.__name__)

                if model.__name__ == 'PersonalInformation':
                    add_new = model(address=row[1], age=row[2], email=row[3], first_name=row[4], freelance=row[5],
                                    name=row[6], phone=row[7], residence=row[8], resume=row[9], second_name=row[10])
                    add_new.save()
                    print(row, model.__name__)

                if model.__name__ == 'Services':
                    add_new = model(icon_text=row[1], text=row[2], title=row[3])
                    add_new.save()
                    print(row, model.__name__)

                if model.__name__ == 'Skills':
                    add_new = model(level=row[2], status=row[3], title=row[1])
                    add_new.save()
                    print(row, model.__name__)

                if model.__name__ == 'Education':
                    add_new = model(date_end=row[5], date_start=row[4], place=row[2], status=row[6], text=row[3],
                                    title=row[1])
                    add_new.save()
                    print(row, model.__name__)

                if model.__name__ == 'Experience':
                    add_new = model(company=row[2], date_end=row[5], date_start=row[4], status=row[6], text=row[3],
                                    title=row[1])
                    add_new.save()
                    print(row, model.__name__)


            except Exception as inst:
                print(type(inst))  # the exception instance
                print(inst.args)  # arguments stored in .args
                print(inst)  # __str__ allows args to be printed directly,
                print(f'{model.__name__} failed ')

    def handle(self, *args, **options):
        for model, table_name in models.items():
            old_data = self.get_data_from_old(table_name)
            self.fill_data(model, old_data)

        self.stdout.write(self.style.SUCCESS('Successfully created models'))
