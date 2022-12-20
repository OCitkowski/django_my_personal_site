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

        add_type_keys = []
        add_keys = []
        add_owners = []
        add_sources = []

        for count in range(options['counts'][0]):
            opt = options['counts']

            # ***************************************************
            try:
                fake = Faker(locale_list)
                name = fake.catch_phrase()
                type_key = TypeKey(name=name)
                type_key.save()
                print(f'{count} create TypeKey model named- {type_key}')
            except:
                raise CommandError('Poll "%s" does not exist')

            add_type_keys.append(type_key)

            # ***********************Key****************************
            try:
                fake = Faker(locale_list)
                domain_name = fake.domain_name()

                type_key_fake = fake.random.choices(add_type_keys)
                add_key = Key(link=domain_name, type_key=type_key_fake[0])
                add_key.save()
                print(f'{count} create Key model named- {add_key}')
                add_keys.append(add_key)
            except:
                raise CommandError('Poll "%s" does not exist')

            # **********************Owner*****************************
            try:
                fake = Faker(locale_list)
                name = fake.name()
                comment = fake.sentence(nb_words=10, variable_nb_words=False)
                add_owner = Owner(name=name, comment=comment)
                add_owner.save()
                print(f'{count} create Owner model named- {add_owner}')
                add_owners.append(add_owner)
            except:
                raise CommandError('Poll "%s" does not exist')

            # **********************Source*****************************
            try:
                fake = Faker(locale_list)
                name = fake.email()
                comment = fake.sentence(nb_words=10, variable_nb_words=False)
                add_source = Source(name=name, comment=comment)
                add_source.save()
                print(f'{count} create Source model named- {add_source}')
                add_sources.append(add_source)
            except:
                raise CommandError('Poll "%s" does not exist')

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
