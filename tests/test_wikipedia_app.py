from selene import have
from selene.support.shared import browser
from models.controls.page_search_results import results_wiki
from models.controls.search import search_wiki


def test_search():

    search_wiki().type("BrowserStack")

    results_wiki().should(have.size_greater_than(0))

    browser.quit()


