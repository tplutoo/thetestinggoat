from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest


class TestNewVisitor:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup code: This runs before each test
        self.browser = webdriver.Firefox()
        yield
        # Teardown code: This runs after each test
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mentions to-do lists
        assert "To-Do" in self.browser.title
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text

        assert "To-Do" in header_text

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")

        assert inputbox.get_attribute("placeholder") == "Enter a to-do item"

        # She types "Buy peacock feathers" into a textbox
        # (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        assert any(row.text == "1: Buy peacock feathers" for row in rows), "New to-do item did not appear in table"

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly
        # (Edith is very methodical)
        pytest.fail("Finish the test!")

        # The page updates again, and now shows both items on her list

