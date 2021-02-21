from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.common.by import By
import time

class FetchGame:
    def __init__(self, driver):
        self.url = 'http://ec2-54-208-152-154.compute-1.amazonaws.com/'
        self.driver = driver
        self.left_bowl_contents = []
        self.right_bowl_contents = []

    def open_game(self):
        self.driver.get(self.url)

    def add_bars_to_left_bowl(self, bar_nums):
        for bar_num in bar_nums:
            bowl_id = 'left_{}'.format(len(self.left_bowl_contents))
            square = self.driver.find_element_by_id(bowl_id)
            square.send_keys(bar_num)
            self.left_bowl_contents.append(bar_num)

    def add_bars_to_right_bowl(self, bar_nums):
        for bar_num in bar_nums:
            bowl_id = 'right_{}'.format(len(self.right_bowl_contents))
            square = self.driver.find_element_by_id(bowl_id)
            square.send_keys(bar_num)
            self.right_bowl_contents.append(bar_num)
        
    def reset_scale(self):
        # Used class name for this selector because there are 2 'reset' ids
        self.driver.find_elements_by_class_name('button')[1].click()
        self.left_bowl_contents = []
        self.right_bowl_contents = []

    def weigh_scale_contents(self):
        self.driver.find_element_by_id('weigh').click()
        return self.driver.find_elements_by_class_name('button')[0].text

    def get_weigh_list(self):
        weigh_list = self.driver.find_elements_by_css_selector('div.game-info li')
        return [weigh.text for weigh in weigh_list]

    def select_bar(self, bar_num):
        bar_id = 'coin_{}'.format(bar_num)
        bar = self.driver.find_element_by_id(bar_id)
        bar.click()
        return Alert(self.driver)

    def find_fake_bar(self):
        group1 = ['0','1','2']
        group2 = ['3','4','5']
        group3 = ['6','7','8']

        self.add_bars_to_left_bowl(group1)
        self.add_bars_to_right_bowl(group2)

        balance = self.weigh_scale_contents()

        if balance == '>':
            final_group = group2
        elif balance == '<':
            final_group = group1
        else:
            final_group = group3

        self.reset_scale()

        self.add_bars_to_left_bowl(final_group[0:1])
        self.add_bars_to_right_bowl(final_group[1:2])

        balance = self.weigh_scale_contents()

        if balance == '>':
            return final_group[1]
        elif balance == '<':
            return final_group[0]
        else:
            return final_group[2]

        