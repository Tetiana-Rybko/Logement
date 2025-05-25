import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logement.settings')
django.setup()

from django.contrib.auth import get_user_model
from belledemeure.models import Property, Amenity

User = get_user_model()
fake = Faker('en_US')


def clear_data():
    print("Clearing old data...")
    Property.objects.all().delete()
    Amenity.objects.all().delete()
    User.objects.filter(is_staff=False).delete()  # удалить всех не-админов

def create_amenities():
    print("Creating amenities...")
    amenities_list = [
        "Wi-Fi", "Parking", "Furnished", "Air Conditioning", "Heating",
        "Washing Machine", "Dishwasher", "Elevator", "Gym", "Pool"
    ]
    amenities = []
    for name in amenities_list:
        amenity, created = Amenity.objects.get_or_create(name=name)
        amenities.append(amenity)
    return amenities

def create_landlords(n=5):
    print(f"Creating {n} landlords...")
    landlords = []
    for _ in range(n):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='password123'
        )
        landlords.append(user)
    return landlords

def create_properties(landlords, amenities):
    print("Creating properties...")

    districts = ["Innenstadt", "Heiligkreuz", "Nordviertel", "Südviertel", "Pfaffendorf"]
    nearby_places = ["Supermarket", "School", "Park", "Train Station", "Hospital"]
    transport = ["Bus Stop", "Train Station", "Tram Line", "Subway"]

    for landlord in landlords:
        # Каждому арендодателю создаём 3-5 объектов
        for _ in range(random.randint(3, 5)):
            is_for_sale = random.choice([True, False])
            district = random.choice(districts)

            if is_for_sale:
                prop = Property.objects.create(
                    owner=landlord,
                    title=fake.sentence(nb_words=5),
                    description=fake.paragraph(nb_sentences=3),
                    address=fake.street_address() + ", Trier",
                    price=round(random.uniform(100000, 1000000), 2),
                    property_type='sale',
                    district=district,
                    square_meters=random.randint(50, 200),
                    floor=random.randint(1, 10),
                    rooms=random.randint(2, 6),
                    year_built=random.randint(1950, 2023),
                    nearby=", ".join(random.sample(nearby_places, 2)),
                    transport=", ".join(random.sample(transport, 2)),
                    installment_available=random.choice([True, False]),
                    mortgage_available=random.choice([True, False]),
                    is_available=True,
                )
            else:
                prop = Property.objects.create(
                    owner=landlord,
                    title=fake.sentence(nb_words=5),
                    description=fake.paragraph(nb_sentences=3),
                    address=fake.street_address() + ", Trier",
                    price=round(random.uniform(300, 2000), 2),  # price per month
                    property_type='rent',
                    district=district,
                    rooms=random.randint(1, 5),
                    furnished=random.choice([True, False]),
                    has_appliances=random.choice([True, False]),
                    wifi=random.choice([True, False]),
                    parking=random.choice([True, False]),
                    transport=", ".join(random.sample(transport, 2)),
                    is_available=True,
                )

            prop.amenities.set(random.sample(amenities, random.randint(1, len(amenities))))
            prop.save()

def run():
    clear_data()
    amenities = create_amenities()
    landlords = create_landlords()
    create_properties(landlords, amenities)
    print("Database seeding complete!")

if __name__ == '__main__':
    run()