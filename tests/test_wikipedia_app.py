import allure
from selene import have
from wikipedia_app.models.controls.page_search_results import results_wiki
from wikipedia_app.models.controls.search import search_wiki


def test_search():
    with allure.step('Search "Browser stack"'):
        search_wiki().type('BrowserStack')

    with allure.step('Check results'):
        results_wiki().should(have.size_greater_than(0))


def test_empty_search():
    with allure.step('Add empty field'):
        search_wiki().type('')

    with allure.step('Check results'):
        results_wiki().should(have.size(0))


def test_search_numbers():
    with allure.step('Search numbers'):
        search_wiki().type('123')

    with allure.step('Check results'):
        results_wiki().should(have.size_greater_than(0))


def test_search_special_symbols():
    with allure.step('Search symbols'):
        search_wiki().type('#%')

    with allure.step('Check results'):
        results_wiki().should(have.size(0))


def test_search_html_tag():
    with allure.step('Search tag'):
        search_wiki().type('<div>')

    with allure.step('Check results'):
        results_wiki().should(have.size_greater_than(0))
