from django.test import TestCase
from .models import UserProfile, Pet, Application
from django.urls import reverse
from django.contrib.auth.models import User


## Model Tests ##

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
        UserProfile.objects.create_user(username="test@gmail.com", first_name="test", last_name="name", phone_number="(02)99999999", address="test address", suburb="test suburb", postcode="2727", password="password")
    
    # Field Tests #

    # test user username
    def test_user_email(self):
        test = UserProfile.objects.get(username = "test@gmail.com")
        self.assertEqual(test.username, "test@gmail.com")
    
    # test user first name
    def test_user_first_name(self):
        test = UserProfile.objects.get(username = "test@gmail.com")
        self.assertEqual(test.first_name, "test")
    
    # test user last name
    def test_user_last_name(self):
        test = UserProfile.objects.get(username = "test@gmail.com")
        self.assertEqual(test.last_name, "name")
    
    # test user phone number
    def test_user_phone(self):
        test = UserProfile.objects.get(username = "test@gmail.com")
        self.assertEqual(test.phone_number, "(02)99999999")
    
    # test user address
    def test_user_address(self):
        test = UserProfile.objects.get(username = "test@gmail.com")
        self.assertEqual(test.address, "test address")

    # test user suburb
    def test_user_suburb(self):
        test = UserProfile.objects.get(username = "test@gmail.com")
        self.assertEqual(test.suburb, "test suburb")
    
    # test user postcode
    def test_user_postcode(self):
        test = UserProfile.objects.get(username = "test@gmail.com")
        self.assertEqual(test.postcode, "2727")
    
    # test user password
    def test_user_password(self):
        test = UserProfile.objects.get(username = "test@gmail.com")
        self.assertEqual(test.password, "password")

    # test user phone number validator
    def test_user_phone_validator(self):
        with self.assertRaises(ValidationError):
            UserProfile.objects.create(username="test@gmail.com", first_name="test", last_name="name", phone_number="(02)9999999999999999999999999999", address="test address", suburb="test suburb", postcode="2727", password="password")
        
    
# test the application model
class ModelApplicationTest(TestCase):
    # initialise test variable
    def setUp(self):
        Pet.objects.create(name="Sasha", species="Dog", breed="Border Collie", age=19, gender="Female", description="test desc", image_path="static/images/CattleDog.png", status="Available", suburb="test suburb", state="NSW", fee=5.50)
        UserProfile.objects.create_user(username="test3@gmail.com", first_name="test", last_name="name", phone_number="(02)99999999", address="test address", suburb="test suburb", postcode="2727", password="password")
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
            Application.objects.create(username="test3@gmail.com", pet=1, application_status="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", application_note="test note", adoption_date='2023-10-25 19:30:45')

# Needs the key validation
# Needs to be updated to the latest model.

## Views Tests ##
class ViewsTest(TestCase):
    def test_login(self):
          user = UserProfile.objects.create_user(username="test3@gmail.com", first_name="test", last_name="name", phone_number="(02)99999999", address="test address", suburb="test suburb", postcode="2727", password="password")
          self.client.login(username='test3@gmail.com', password='password')
          response = self.client.get(reverse('registration/login.html'))
          self.assertEqual(response.status_code, 200)
    def test_login_page(self):
        response = self.client.get(reverse('login_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        
    def test_sign_up_page(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')
        
    def test_pet_detail(self):
        response = self.client.get(reverse('pet_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rescues_site/pets.html')
        
    def test_home(self):
        response = self.client.get(reverse(''))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rescues_site/home.html')
        
    def test_about_us(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rescues_site/about_us.html')
        
    def test_service(self):
        response = self.client.get(reverse('service'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rescues_site/service.html')

    def test_pet_list(self):
        response = self.client.get(reverse('pet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rescues_site/pet_list.html')

    def test_admin_user(self):
        response = self.client.get(reverse('admin_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rescues_site/admin_user.html')
        
## Form Tests ##
class FormTest(TestCase):
    def test_valid_form_submission(self):
        # create form
        form_data = {
            'first_name': 'test',
            'last_name': 'name',
            'address': 'test address',
            'suburb': 'test suburb',
            'postcode': '2727',
            'email': 'test@test.com',
            'phone_number': '(02)99999999',
            'password': 'test password'
        }
        # submit
        response = self.client.post(reverse('sign_up'), data=form_data)
        # test the redirect
        self.assertEqual(response.status_code, 302)
        # test the existence of this object
        self.assertTrue(UserProfile.objects.filter(username='test@test.com').exists())
