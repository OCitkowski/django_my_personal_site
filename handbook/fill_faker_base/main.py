from faker import factory, Faker
from handbook.serializers import TypeKeySerializer

fake = Faker()

locale_list = ['en-US', 'uk-UA', 'de-DE']

if __name__ == '__main__':
    fake = Faker(locale_list)
    # *********************TypeKey****************************
    name = fake.catch_phrase()
    print({name})
    data = {'name': f'{name}'}

    tk = TypeKeySerializer(data)
    tk.save()
