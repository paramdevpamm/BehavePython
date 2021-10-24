import time

import allure
from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import timedelta, date, datetime

from selenium.webdriver.support.select import Select


@given('The URL should open')
def navigateToURL(context):
    print("Text")
    context.driver = webdriver.Chrome()


@given('I open the browser to "{text}" on chrome')
def navigateToGivenURL(context, text):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(text)
    time.sleep(2)


@when('I click on flight')
def clickOnFlight(context):
    context.driver.find_element(By.XPATH, "//a[@href='?pwaLob=wizard-flight-pwa']").click()


@when('I Click on round trip')
def clickOnRoundTrip(context):
    context.driver.find_element(By.XPATH, "//a[@href='?flightType=roundtrip']").click()
    context.driver.save_screenshot('clickOnRoundTrip.png')
    allure.attach(context.driver.get_screenshot_as_png(), name='clickOnRoundTrip', attachment_type=allure.attachment_type.PNG)


@when('I Enter from as "{text}" and destination as "{text2}"')
def selectToAndFromField(context, text, text2):
    fromField = context.driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']")
    searchPopFrom = context.driver.find_element(By.ID, "location-field-leg1-origin")
    fromField.send_keys(text)
    time.sleep(2)
    searchPopFrom.send_keys(Keys.ENTER)
    time.sleep(2)

    toField = context.driver.find_element(By.XPATH, "//button[@aria-label='Going to']")
    toField.send_keys(text2)
    time.sleep(2)
    searchPopTo = context.driver.find_element(By.ID, "location-field-leg1-destination")
    searchPopTo.send_keys(Keys.ENTER)
    time.sleep(2)


@when('Select departing date as "{fromDate}" days and returning as "{toDate}" days from now')
def selectToAndFromDate(context, fromDate, toDate):
    print('sample')
    # Nov 18, 2021 //button[@aria-label='Nov 26, 2021 selected, current check out date.']
    # button[aria-label='Nov 27, 2021']
    startDate = date.today() + timedelta(days=7)
    startDate = datetime.strftime(startDate, '%b %d, %Y')
    returnDate = date.today() + timedelta(days=14)
    returnDate = datetime.strftime(returnDate, '%b %d, %Y')

    dateSelect = context.driver.find_element(By.XPATH, "//button[@id='d1-btn']")
    dateSelect.click()
    context.driver.find_element(By.XPATH("//button[@aria-label='" + startDate + "']")).click()
    context.driver.find_element(By.XPATH("//button[@aria-label='" + returnDate + "']")).click()


@when('I click on search for flights')
def clickOnSearchFlight(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']")
    time.sleep(5)


@when('I select "{optionToSelect}" in sort dropdown')
def selectOptionInSortDropDown(context, optionToSelect):
    time.sleep(5)
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='listings-sort']"))
    select.select_by_value(optionToSelect)


@when('I click on the first option')
def selectFirstOptionInFlightResult(context):
    context.driver.find_element(By.XPATH, "//button[@data-test-id='select-link']").click()


@when('Click on continue')
def clickOnContinue(context):
    context.driver.find_element(By.XPATH, "//button[@data-test-id='select-button']").click()


@then('Validate the round trip icon is displayed')
def validateRoundTripSwapIcon(context):
    status = context.driver.find_element(By.CSS_SELECTOR("SwapLocationsDesktop > .uitk-icon")).is_displayed()
    assert status is True


@then('Sort dropdown should be displayed')
def sortDropDownShouldBeDisplayed(context):
    status = context.driver.find_element(By.XPATH, "//select[@id='listings-sort']").is_displayed()
    assert status is True

@then('Check out page should be displayed with "{fromPlace}" and destination as "{destinationPlace}"')
def validateCheckoutScreenIsDisplayed(context, fromPlace, destinationPlace):
    status = context.driver.find_element(By.XPATH, "//button[contains(.,'Check out')]").is_displayed()
    assert status is True
    fromDest = context.driver.find_element(By.XPATH, "//*[@id='summary-container']/article/div[1]/div[2]/div[1]")
    toDest = context.driver.find_element(By.XPATH, "//*[@id='summary-container']/article/div[1]/div[3]/div[1]")
    assert fromPlace in fromDest
    assert destinationPlace in toDest


@then('The Sign in option should be displayed')
def validateSignInOptionIsDisplayed(context):
    status = context.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").is_displayed()
    assert status is True
