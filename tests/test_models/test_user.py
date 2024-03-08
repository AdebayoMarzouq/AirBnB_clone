""" _summary_
"""
import unittest
import time
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_attributes_default_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attributes_types(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_inherited_attributes(self):
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_str_representation(self):
        expected_str = "[User] ({}) {}".format(
            self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_save_method(self):
        original_updated_at = self.user.updated_at
        time.sleep(0.1)
        self.user.save()
        self.assertNotEqual(original_updated_at, self.user.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            '__class__': "User",
            'email': "",
            'password': "",
            'first_name': "",
            'last_name': "",
        }
        for key, value in expected_dict.items():
            if key == '__class__':
                self.assertEqual(value, self.user.__class__.__name__)
            else:
                self.assertTrue(hasattr(self.user, key))


if __name__ == '__main__':
    unittest.main()
