from django.core.management.base import BaseCommand, CommandError
from handbook.models import TypeKey, Key, Owner, Source, STATUS, Note
from faker import factory, Faker

# locale_list = ['en-US', 'uk-UA', 'de-DE']
locale_list = ['en-US']


class Command(BaseCommand):
    # https: // docs.djangoproject.com / en / 4.1 / howto / custom - management - commands /
    help = 'Fill'

    def add_arguments(self, parser):
        parser.add_argument('counts', nargs='+', type=int)

    def handle(self, *args, **options):

        add_keys = Key.objects.all()
        add_owners = Owner.objects.all()
        add_sources = Source.objects.all()

        for count in range(options['counts'][0]):
            opt = options['counts']
            # ***********************Note****************************
            try:
                fake = Faker(locale_list)

                fake_owner = fake.random.choices(add_owners)[0]
                fake_source = fake.random.choices(add_sources)[0]
                fake_key = fake.random.choices(add_keys)[0]
                fake_comment = fake.sentence(nb_words=10, variable_nb_words=False)
                fake_text = fake.pystr(max_chars=20)
                print(f'{fake_owner} / {fake_source} / {fake_key} / {fake_comment} / {fake_text}')

                add_note = Note(owner=fake_owner,
                                source=fake_source,
                                key=fake_key,
                                status=STATUS[0],
                                text=fake_text,
                                comment=fake_comment)
                add_note.save()
                print(f'{count} create Note model named- {add_note}')

            except:
                # print(f'{fake_owner} / {fake_source} / {type(fake_key)} / {fake_comment} / {fake_text}')
                raise CommandError('Poll "%s" does not exist')

            self.stdout.write(self.style.SUCCESS('Successfully created models'))
