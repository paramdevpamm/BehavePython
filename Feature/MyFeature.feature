Feature: Assignment

  Scenario: Open orbitz
    Given I open the browser to "https://www.orbitz.com/" on chrome
    Then The Sign in option should be displayed
    When I click on flight
    And I Click on round trip
    Then Validate the round trip icon is displayed
    When I Enter from as "San Francisco" and destination as "New York"
    And Select departing date as "7" days and returning as "14" days from now
    And I click on search for flights
    Then Sort dropdown should be displayed
    When I select "Price (Highest)" in sort dropdown
    And I click on the first option
    And Click on continue
    And I click on the first option
    And Click on continue
    Then Check out page should be displayed with "San Francisco" and destination as "New York"