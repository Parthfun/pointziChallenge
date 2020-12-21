Feature: Pointzi Successful Login

  Scenario Outline: Login pointzi dashboard page
    Given launch google chrome
    When open pointzi dashboard page
    Then Enter email "<username>" and password "<password>"
    When click on login button

    Examples:
      | username       | password     |
      | dbca@gmail.com | plmn1357plmn |
      | test@gmail.com | pass9876     |
