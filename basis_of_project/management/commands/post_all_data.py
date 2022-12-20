from django.core.management.base import BaseCommand, CommandError
from handbook.models import TypeKey, Key, Owner, Source, STATUS, Note
from faker import factory, Faker

from home_page.models import Home
from about_me_page.models import TextAboutMe, PersonalInformation, Services
from resume_page.models import Skills, Education, Experience

from basis_of_project.utils import STATUS_CHOICES

# locale_list = ['en-US', 'uk-UA', 'de-DE']
locale_list = ['en-US']
model_names = ['all', 'Home', 'TextAboutMe', 'PersonalInformation', 'Services', 'Skills', 'Education', 'Experience']


class Command(BaseCommand):
    # https: // docs.djangoproject.com / en / 4.1 / howto / custom - management - commands /
    help = 'Fill'

    def add_arguments(self, parser):
        parser.add_argument('model_name', nargs='+', type=str)

    def fill_home(self):
        titles = ['Django developer', 'full stack developer ']

        for title in titles:
            try:
                add_home = Home(title_en=title, status=STATUS_CHOICES[1])
                add_home.save()
                print('Hello')
            except:
                pass

    def handle(self, *args, **options):
        if options["model_name"][0] in model_names:
            self.fill_home()

        self.stdout.write(self.style.SUCCESS('Successfully created models'))

    # def fill_TextAboutMe(self):
    #     titles = ['Django developer', 'full stack developer ']
    #
    #     for title in titles:
    #         try:
    #             add_home = Home(title=title, text=STATUS_CHOICES[1])
    #             title = models.CharField(max_length=100, default='About Me.')
    #             text = models.TextField(max_length=1000, default='-----')
    #             add_home.save()
    #             print('Hello')
    #         except:
    #             pass