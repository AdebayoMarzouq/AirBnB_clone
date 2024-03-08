""" _summary_
"""
import unittest
import time
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attributes_default_values(self):
        self.assertEqual(self.amenity.name, "")

    def test_attributes_types(self):
        self.assertIsInstance(self.amenity.name, str)

    def test_inherited_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_str_representation(self):
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_save_method(self):
        original_updated_at = self.amenity.updated_at
        time.sleep(0.1)
        self.amenity.save()
        self.assertNotEqual(original_updated_at, self.amenity.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            '__class__': "Amenity",
            'name': "",
        }
        for key, value in expected_dict.items():
            if key == '__class__':
                self.assertEqual(value, self.amenity.__class__.__name__)
            else:
                self.assertTrue(hasattr(self.amenity, key))


if __name__ == '__main__':
    unittest.main()
