Feature: This is the feature of Test App Home page validation

  @device-iPhone8Plus @smoke
  Scenario: This is the scenario for doing home page validation on iPhone 8 Plus

    Given I am on the app home page of the app
    When I enter the value "1" in text field 1
    And I enter the value "2" in text field 2
    Then I click on the calculate sum
    And I validate the sum is "3"

#  @device-iPhoneX
#  Scenario: This is the scenario for doing home page validation on iPhoneX
#
#    Given I am on the app home page of the app
#    When I enter the value "1" in text field 1
#    And I enter the value "2" in text field 2
#    Then I click on the calculate sum
#    And I validate the sum is "3"