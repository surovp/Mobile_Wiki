from selene.support.shared import browser
from models.helpers import selector_id


def results_wiki():
    browser.all(selector_id('page_list_item_title'))
