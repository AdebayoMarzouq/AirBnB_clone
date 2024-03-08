""" _summary_
"""
import unittest
import time
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_attributes_default_values(self):
        self.assertEqual(self.review.text, "")
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")

    def test_attributes_types(self):
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)

    def test_inherited_attributes(self):
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_str_representation(self):
        expected_str = "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_save_method(self):
        original_updated_at = self.review.updated_at
        time.sleep(0.1)
        self.review.save()
        self.assertNotEqual(original_updated_at, self.review.updated_at)

    def test_to_dict_method(self):
        expected_dict = {
            '__class__': "Review",
            'place_id': "",
            'user_id': "",
            'text': "",
        }
        for key, value in expected_dict.items():
            if key == '__class__':
                self.assertEqual(value, self.review.__class__.__name__)
            else:
                self.assertTrue(hasattr(self.review, key))


if __name__ == '__main__':
    unittest.main()
