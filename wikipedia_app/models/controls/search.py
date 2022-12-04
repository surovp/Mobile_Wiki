from wikipedia_app.models.helpers import accessibility_id, selector_id
from selene.support.shared import browser


def search_wiki():
    browser.element(accessibility_id("Search Wikipedia")).click()
    return browser.element(selector_id('search_src_text'))
