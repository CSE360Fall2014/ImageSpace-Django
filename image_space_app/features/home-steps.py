from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()

@step(r'Given I am a new user')
def access_url(step):
    #logout
    pass

@step(r'I load the "(.*)" page')
def access_url(step, url):
    url = "http://localhost:8000"
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I fill in "(.*)" with "(.*)"')
def fill_in(step, param, val):
    #fill value
    pass

@step(r'I press "(.*)"')
def press_button(step, button):
    #press button
    pass

@step(r'I see the header "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('a.brand')
    assert header