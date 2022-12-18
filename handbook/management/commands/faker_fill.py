from django.core.management.base import BaseCommand, CommandError
from handbook.models import TypeKey
from faker import factory, Faker

locale_list = ['en-US', 'uk-UA', 'de-DE']


class Command(BaseCommand):
    help = 'Fill'

    def add_arguments(self, parser):
        parser.add_argument('counts', nargs='+', type=int)

    def handle(self, *args, **options):
        for count in range(options['counts'][0]):
            opt = options['counts']

            try:
                fake = Faker(locale_list)
                name = fake.catch_phrase()
                type_key = TypeKey(name=name)
                type_key.save()
                print(f'{count} create TypeKey model named- {type_key}')
            except:
                raise CommandError('Poll "%s" does not exist')

        self.stdout.write(self.style.SUCCESS('Successfully closed poll'))
