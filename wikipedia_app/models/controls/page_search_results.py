from selene.support.shared import browser
from wikipedia_app.models.helpers import selector_id


def results_wiki():
    return browser.all(selector_id('page_list_item_title'))
