Feature: A new user comes to home page and fills the email and password to login.
         But website returns the same home page as reply

    Scenario: New user tries login
        Given I am a new user
        And I load the "home" page
        And I fill in "email-input" with "John@doe.com"
        And I fill in "password-input" with "password"
        When I press "sign_in"
        I see the header "ImageSpace"