from django.core.management.base import BaseCommand
from home_page.models import Home
from about_me_page.models import TextAboutMe, PersonalInformation, Services
from resume_page.models import Skills, Education, Experience


class Command(BaseCommand):
    help = '''This command removes all data from the site
    delete_all_data [model] (from models name)
    exercise - python manage.py delete_all_data -resume 
    '''

    def add_arguments(self, parser):
        parser.add_argument('model', nargs='+', type=str)

    def delete_model(self, model_name):
        models = []
        try:
            if model_name == 'Home' or model_name == 'all':
                Home.objects.all().delete()
                models.append('Home')

            if model_name == 'PersonalInformation' or model_name == 'all':
                PersonalInformation.objects.all().delete()
                models.append('PersonalInformation')
            if model_name == 'TextAboutMe' or model_name == 'all':
                TextAboutMe.objects.all().delete()
                models.append('TextAboutMe')
            if model_name == 'Services' or model_name == 'all':
                Services.objects.all().delete()
                models.append('Services')

            if model_name == 'Skills' or model_name == 'all':
                Skills.objects.all().delete()
                models.append('Skills')
            if model_name == 'Education' or model_name == 'all':
                Education.objects.all().delete()
                models.append('Education')
            if model_name == 'Experience' or model_name == 'all':
                Experience.objects.all().delete()
                models.append('Experience')

            self.stdout.write(self.style.SUCCESS(f'Successfully removes all data from the models {models}'))
        except:
            pass

    def handle(self, *args, **options):
        model_name = options['model'][0]
        self.delete_model(model_name)
