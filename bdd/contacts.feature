Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname>, <middlename>, <lastname>, <nickname>, <title>, <company>, <address>, <fax>, <mobilephone>, <workphone>, <homephone>, <email>, <email2>, <email3>, <homepage>, <option1>, <option2>, <byear>, <option3>, <option4>, <ayear>, <address2>, <secondaryphone> and <notes>
    When I add the contact to the list
    Then the new contact list is equal the old list with the added contact

    Examples:
    | firstname | middlename | lastname | nickname | title | company | address | fax | mobilephone | workphone | homephone | email | email2 | email3 | homepage | option1 | option2 | byear | option3 | option4 | ayear | address2 | secondaryphone | notes |
    | firstname1 | middlename1 | lastname1 | nickname1 | title1 | company1 | address1 | fax1 | mobilephone1 | workphone1 | homephone1 | email1 | email2_1 | email3_1 | homepage1 | 1 | May | 2017 | 3 | July | 2018 | address2_1 | secondaryphone1 | notes1 |
    | firstname2 | middlename2 | lastname2 | nickname2 | title2 | company2 | address2 | fax2 | mobilephone2 | workphone2 | homephone2 | email2 | email2_2 | email3_2 | homepage2 | 2 | June | 2018 | 4 | August | 2019 | address2_2 | secondaryphone2 | notes2 |


Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal the old list without the deleted contact


Scenario Outline: Edit a contact
    Given a non-empty contact list
    Given a random contact from the list
    Given a contact with <firstname>, <middlename>, <lastname>, <nickname>, <title>, <company>, <address>, <fax>, <mobilephone>, <workphone>, <homephone>, <email>, <email2>, <email3>, <homepage>, <option1>, <option2>, <byear>, <option3>, <option4>, <ayear>, <address2>, <secondaryphone> and <notes>
    When I edit the contact according to the new contact information
    Then the new contact list is equal the old list with the updated contact

    Examples:
    | firstname | middlename | lastname | nickname | title | company | address | fax | mobilephone | workphone | homephone | email | email2 | email3 | homepage | option1 | option2 | byear | option3 | option4 | ayear | address2 | secondaryphone | notes |
    | new_firstname | new_middlename | new_lastname | new_nickname | new_title | new_company | new_address | new_fax | new_mobilephone | new_workphone | new_homephone | new_email | new_email2 | new_email3 | new_homepage | 10 | October | 2015 | 13 | november | 2016 | new_address2 | new_secondaryphone | new_notes |
