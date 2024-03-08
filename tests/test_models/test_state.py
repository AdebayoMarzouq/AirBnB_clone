""" _summary_
"""
import unittest
import time
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_attributes_default_values(self):
        self.assertEqual(self.state.name, "")

    def test_attributes_types(self):
        self.assertIsInstance(self.state.name, str)

    def test_inherited_attributes(self):
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_str_representation(self):
        expected_str = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_save_method(self):
        original_updated_at = self.state.updated_at
        time.sleep(0.1)
        self.state.save()
        self.assertNotEqual(original_updated_at, self.state.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            '__class__': "State",
            'name': "",
        }
        for key, value in expected_dict.items():
            if key == '__class__':
                self.assertEqual(value, self.state.__class__.__name__)
            else:
                self.assertTrue(hasattr(self.state, key))


if __name__ == '__main__':
    unittest.main()
