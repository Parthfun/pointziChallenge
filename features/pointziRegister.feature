Feature: Register to pointzi

  Scenario Outline:
    Given launch google chrome
    Then open pointzi dashboard page
    Then click on register
    And Enter email "<email>" password "<pwd>" and confirm password "<confirm>"
    Then click next
    And select role and No. of app users
    Then click next
    And Enter First name "x" Lastname "y" Company name "z" and phone number ""
    Then click sign up
    And user is successfully signed up
    Examples:
      |email                 |pwd                |confirm        |
      |pqrst@gmail.com       |plmn1357plmn       |plmn1357plmn   |
     # |test@gmail.com        |pass9876           |pass9876       |
      |test1@gmail.com       |auto6python        |autopython     |
