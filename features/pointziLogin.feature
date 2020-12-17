Feature: Pointzi Successful Login

  Scenario: Login pointzi dashboard page
    Given launch google chrome
    When open pointzi dashboard page
    Then Enter email "dcba@gmail.com" and password "plmn1357plmn"
    When click on login button
    Then user must sucessfully login the dashboard page

   # Examples:
     # |    username   | password |
      #| fvv@gmail.com | asdf9876 |
