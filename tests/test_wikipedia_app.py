import allure
from selene import have
from wikipedia_app.models.controls.page_search_results import results_wiki
from wikipedia_app.models.controls.search import search_wiki


def test_search():
    with allure.step('Search "Browser stack"'):
        search_wiki().type('BrowserStack')

    with allure.step('Check results'):
        results_wiki().should(have.size_greater_than(0))
