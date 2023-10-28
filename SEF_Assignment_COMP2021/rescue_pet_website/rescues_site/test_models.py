from django.test import TestCase
from .models import CustomUser, Pet, Application
from django.contrib.auth.hashers import make_password

# test the pet model
class ModelPetTest(TestCase):
    # initialise test variable
    def setUp(self):
        Pet.objects.create(name="Sasha", species="Dog", breed="Border Collie", age=19, gender="Female", description="test desc", image_path="static/images/CattleDog.png", status="Available", suburb="test suburb", state="NSW", fee=5.50)
    
    # Field tests #
    
    # test pet name
    def test_pet_name(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.name, "Sasha")
    
    # test pet species
    def test_pet_species(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.species, "Dog")
    
    # test pet breed
    def test_pet_breed(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.breed, "Border Collie")
    
    # test pet age
    def test_pet_age(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.age, 19)
    
    # test pet gender
    def test_pet_gender(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.gender, "Female")
    
    # test pet description
    def test_pet_desc(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.description, "test desc")

    # test pet image path
    def test_pet_img_path(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.image_path, "static/images/CattleDog.png")

    # test pet status
    def test_pet_status(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.status, "Available")
    
    # test pet suburb
    def test_pet_suburb(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.suburb, "test suburb")
    
    # test pet state
    def test_pet_state(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.state, "NSW")
    
    # test pet fee
    def test_pet_fee(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.fee, 5.50)
    
    # test pet date - not finished
    def test_pet_date(self):
        test = Pet.objects.get(pet_id = 1)
        self.assertEqual(test.date_added, )

    # Validator Tests #

    # test pet gender validator
    def test_pet_gender_validator(self):
        with self.assertRaises(ValidationError):
            Pet.objects.create(name="Sasha", species="Dog", breed="Border Collie", age=19, gender="Aaaaaaaaaaaaaaaaaaa", description="test desc", image_path="static/images/CattleDog.png", status="Available", suburb="test suburb", state="NSW", fee=5.50)
    # test pet status validator
    def test_pet_status_validator(self):
        with self.assertRaises(ValidationError):
            Pet.objects.create(name="Sasha", species="Dog", breed="Border Collie", age=19, gender="Female", description="test desc", image_path="static/images/CattleDog.png", status="No", suburb="test suburb", state="NSW", fee=5.50)
        
    # test pet state validator
    def test_pet_state_validator(self):
        with self.assertRaises(ValidationError):
            Pet.objects.create(name="Sasha", species="Dog", breed="Border Collie", age=19, gender="Female", description="test desc", image_path="static/images/CattleDog.png", status="Available", suburb="test suburb", state="None", fee=5.50)
    
    # test pet fee validator
    def test_pet_fee_validator(self):
        with self.assertRaises(ValidationError):
            Pet.objects.create(name="Sasha", species="Dog", breed="Border Collie", age=19, gender="Female", description="test desc", image_path="static/images/CattleDog.png", status="Available", suburb="test suburb", state="NSW", fee=5.55555555555555555555)

# test the custom user model
class ModelCustomUserTest(TestCase):
    # initialise test variable
    def setUp(self):
        testpassword = make_password("test password")
        # full field
        CustomUser.objects.create(username="test name", email="test@gmail.com", first_name="test", last_name="name", phone_number="(02)99999999", address="test address", suburb="test suburb", postcode="2727", password=testpassword, reference="test reference", is_admin=False, is_staff=False)
        # field missing unrequired values
        CustomUser.objects.create(username="test name 2", email="test@gmail.com", first_name="test", last_name="name", address="test address", suburb="test suburb", postcode="2727", password=testpassword)
    
    # Field Tests #

    # test user username
    def test_user_username(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.username, "test name")

    # test user email
    def test_user_email(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.email, "test@gmail.com")
    
    # test user first name
    def test_user_first_name(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.first_name, "test")
    
    # test user last name
    def test_user_last_name(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.last_name, "name")
    
    # test user phone number
    def test_user_phone(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.phone_number, "(02)99999999")
    
    # test user address
    def test_user_address(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.address, "test address")

    # test user suburb
    def test_user_suburb(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.suburb, "test suburb")
    
    # test user postcode
    def test_user_postcode(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.postcode, "2727")
    
    # test user password
    def test_user_password(self):
        testpassword = make_password("test password")
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.password, testpassword)
    
    # test user reference
    def test_user_reference(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.reference, "test reference")
    
    # test user admin status
    def test_user_admin(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.is_admin, False)
    
    # test user staff status
    def test_user_staff(self):
        test = CustomUser.objects.get(user_id = 1)
        self.assertEqual(test.is_staff, False)
    
    # Validator Tests #

    # test user username validator
    def test_user_username_validator(self):
        testpassword = make_password("test password")
        with self.assertRaises(ValidationError):
            CustomUser.objects.create(username="test name", email="test@gmail.com", first_name="test", last_name="name", phone_number="(02)99999999", address="test address", suburb="test suburb", postcode="2727", password=testpassword, reference="test reference", is_admin=False, is_staff=False)
            CustomUser.objects.create(username="test name", email="test@gmail.com", first_name="test", last_name="name", phone_number="(02)99999999", address="test address", suburb="test suburb", postcode="2727", password=testpassword, reference="test reference", is_admin=False, is_staff=False)

    # test user phone number validator
    def test_user_phone_validator(self):
        testpassword = make_password("test password")
        with self.assertRaises(ValidationError):
            CustomUser.objects.create(username="test name", email="test@gmail.com", first_name="test", last_name="name", phone_number="(02)9999999999999999999999999999", address="test address", suburb="test suburb", postcode="2727", password=testpassword, reference="test reference", is_admin=False, is_staff=False)
        
    
# test the application model
class ModelApplicationTest(TestCase):
    # initialise test variable
    def setUp(self):
        testpassword = make_password("test password")
        Pet.objects.create(name="Sasha", species="Dog", breed="Border Collie", age=19, gender="Female", description="test desc", image_path="static/images/CattleDog.png", status="Available", suburb="test suburb", state="NSW", fee=5.50)
        CustomUser.objects.create(username="test name 3", email="test@gmail.com", first_name="test", last_name="name", phone_number="(02)99999999", address="test address", suburb="test suburb", postcode="2727", password=testpassword, reference="test reference", is_admin=True, is_staff=True)
        Application.objects.create(user=1, pet=1, application_status="Pending", application_note="test note", adoption_date='2023-10-25 19:30:45')
    
    # Field Tests #

    # test application user key
    def test_app_user_key(self):
        test = Application.objects.get(application_id = 1)
        self.assertEqual(test.user, 1)
    
    # test application pet key
    def test_app_user_key(self):
        test = Application.objects.get(application_id = 1)
        self.assertEqual(test.pet, 1)

    # test application status
    def test_app_user_key(self):
        test = Application.objects.get(application_id = 1)
        self.assertEqual(test.application_status, "Pending")
    
     # test application note
    def test_app_user_key(self):
        test = Application.objects.get(application_id = 1)
        self.assertEqual(test.application_note, "test note")
    
    # test application adoption date
    def test_app_user_key(self):
        test = Application.objects.get(application_id = 1)
        self.assertEqual(test.adoption_date, '2023-10-25 19:30:45')
    
    # Validator Tests #

    # test application status validator
    def test_app_status_validator(self):
        with self.assertRaises(ValidationError):
            Application.objects.create(user=1, pet=1, application_status="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", application_note="test note", adoption_date='2023-10-25 19:30:45')

# Needs the key validation
# Needs to be updated to the latest model.