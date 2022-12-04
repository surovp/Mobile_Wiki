import allure
from selene.support.shared import browser
from wikipedia_app.utils.browserstack.get import video_url


def screenshot(*, name='screenshot'):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        #можем указать свое наименование, которое будет в отчёте
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


def screen_xml_dump(*, name='page xml dump'):
    allure.attach(
        browser.driver.page_source,
        name=name,
        attachment_type=allure.attachment_type.XML
    )


def video_from_browserstack(session_id, *, name='video recording'):
    url = video_url(session_id=session_id)

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name=name,
        attachment_type=allure.attachment_type.HTML,
    )
