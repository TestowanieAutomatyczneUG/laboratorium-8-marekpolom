import unittest, nose

from request.request import SearchFood


class TestFood(unittest.TestCase):

    def setUp(self):
        self.temp = SearchFood        

    def test_name(self):
        self.assertEqual(self.temp.byName('Arrabiata')['meals'][0]['idMeal'], '52771')

    def test_name_error(self):
        self.assertRaises(Exception, self.temp.byName(654564))

    def test_area(self):
        self.assertEqual(self.temp.byArea('Polish')['meals'][0]['idMeal'], '53018')

    def test_area_error(self):
        self.assertRaises(Exception, self.temp.byName(2222222))

    def test_category(self):
        self.assertEqual(self.temp.byCategory('Seafood')['meals'][0]['idMeal'], '52959')

    def test_category_error(self):
        self.assertRaises(Exception, self.temp.byName(76554))

    def test_all_categories(self):
        self.assertEqual(self.temp.categories()['categories'][0]['strCategory'], 'Beef')

    def test_random(self):
        self.assertGreater(len(self.temp.random()['meals']), 0)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    nose.run()
