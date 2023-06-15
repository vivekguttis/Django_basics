from faker import Faker
from my_app2.models import person
import random


class populatepersons:

    def __init__(self):
        pass

    def run(self):
fake=Faker()
LIMIT=100
for i in range(LIMIT):
    person_obj=person.objects.create(
        fname=fake.first_name(),
        lname=fake.last_name(),
        age=random.randrange(1,99),
        gender=random.choice(["m","f","o"]),
        email=fake.email(),


        )
    print(person_obj)
obj=populatepersons()
obj.run()

