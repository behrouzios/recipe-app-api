from django.test import TestCase
# from app.calc import add,subtract
from django.contrib.auth import get_user_model



# class CalcTests(TestCase):
#     def test_add_numbers(self):

#         self.assertEqual(add(3,8),11)



#     def test_subtract_numbers(self):

#         self.assertEqual(subtract(11,5),6)

class ModelTests(TestCase):
    def test_create_user(self):
        email="behrouz@gmail.com"
        password="Testpas1234"
        user=get_user_model().objects.create_user(email=email,password=password)
        self.assertEqual(user.email ,email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalize(self):
        email="behroz@gmail.com"
      
        user=get_user_model().objects.create_user(email,"2353nwert")
        self.assertEqual(user.email ,email.lower())


    def test_new_user_invalid_email(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "12344556")

    def test_create_superuser(self):
        user=get_user_model().objects.create_superuser(
            "test2@google.com",
            "2353nwert"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)