from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='hash@yahoo.com', password='testpass'):
    """create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_eamil_successful(self):
        """test creating a new user with an email is successful"""
        email = 'hossein@yahoo.com'
        password = 'hash6648'
        user = get_user_model(). objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """normalize the email"""
        email = 'test@hdjdkSKDD.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test134')

    def test_create_new_superuser(self):
        """creating super user"""
        user = get_user_model().objects.create_superuser(
            'hash@yahoo.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """test the tag represntation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """test the string recipe representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe), recipe.title)
