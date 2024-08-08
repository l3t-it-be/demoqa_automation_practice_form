from pathlib import Path

import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def manage_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'

    browser.config.window_width = 1440
    browser.config.window_height = 880

    browser.config.set_value_by_js = True

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--headless')

    browser.config.driver_options = driver_options

    yield

    browser.quit()


def path(file_name):
    return str(Path(__file__).parent.parent.joinpath(f'resources/{file_name}'))
