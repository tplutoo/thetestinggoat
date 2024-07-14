import pytest
from selenium import webdriver


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

        # She is invited to enter a to-do item straight away
        pytest.fail("Finish the test!")

        # Satisfied, she goes back to sleep

