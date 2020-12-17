Feature: Register to pointzi
  Scenario:
    Given launch google chrome
    Then open pointzi dashboard page
    Then click on register
    And Enter email "dcba@gmail.com" password "plmn1357plmn" and confirm password "plmn1357plmn"
    Then click next
    And select role and No. of app users
    Then click next
    And Enter First name "abcd" Lastname "dcba" Company name "xyz" and phone number ""
    Then click sign up
    And user is successfully signed up
