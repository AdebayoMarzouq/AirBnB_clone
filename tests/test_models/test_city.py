""" _summary_
"""
import unittest
import time
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_attributes_default_values(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_attributes_types(self):
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_inherited_attributes(self):
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_str_representation(self):
        expected_str = "[City] ({}) {}".format(
            self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_save_method(self):
        original_updated_at = self.city.updated_at
        time.sleep(0.1)
        self.city.save()
        self.assertNotEqual(original_updated_at, self.city.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            '__class__': "City",
            'state_id': "",
            'name': "",
        }
        for key, value in expected_dict.items():
            if key == '__class__':
                self.assertEqual(value, self.city.__class__.__name__)
            else:
                self.assertTrue(hasattr(self.city, key))


if __name__ == '__main__':
    unittest.main()
