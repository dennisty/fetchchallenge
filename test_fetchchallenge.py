import unittest
from fetchchallenge import FetchGame
from selenium import webdriver


class TestFetchGame(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.fetch_game = FetchGame(self.driver)
        self.fetch_game.open_game()

    def tearDown(self):
        self.driver.quit()

    def test_get_fake_bar(self):
        fake_bar = self.fetch_game.find_fake_bar()
        print('Fake bar = {}'.format(fake_bar))
        weigh_list = self.fetch_game.get_weigh_list()
        print('Weighed {} times'.format(len(weigh_list)))
        print('Weigh list:')
        for w in weigh_list:
            print(w)
        alert = self.fetch_game.select_bar(fake_bar)
        result = alert.text
        print('Alert message: {}'.format(result))
        self.assertEqual(result, 'Yay! You find it!')

        