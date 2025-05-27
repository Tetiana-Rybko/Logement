import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Logement.settings')
django.setup()

from django.contrib.auth import get_user_model
from belledemeure.models import Property, Amenity

User = get_user_model()
fake = Faker('en_US')


def clear_data():
    print("Clearing old data...")
    Property.objects.all().delete()
    Amenity.objects.all().delete()
    User.objects.filter(is_staff=False).delete()

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
    print("Creating rental properties...")

    districts = ["Innenstadt", "Heiligkreuz", "Nordviertel", "Südviertel", "Pfaffendorf"]
    nearby_places = ["Supermarket", "School", "Park", "Train Station", "Hospital"]
    transport = ["Bus Stop", "Train Station", "Tram Line", "Subway"]

    for landlord in landlords:

        for _ in range(random.randint(3, 5)):

            prop = Property.objects.create(
                owner=landlord,
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                address=fake.street_address() + ", Trier",
                price_per_night=round(random.uniform(30, 200), 2),
                property_type='rent',
                has_furniture=random.choice([True, False]),
                has_appliances=random.choice([True, False]),
                has_wifi=random.choice([True, False]),
                has_parking=random.choice([True, False]),
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

