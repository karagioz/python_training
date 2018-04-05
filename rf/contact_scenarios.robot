*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname1  middlename1  lastname1  nickname1  title1  company1  address1  fax1  mobilephone1  workphone1  homephone1  email1  email2_1  email3_1  homepage1  1  May  2017  3  July  2018  address2_1  secondaryphone1  notes1
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Edit contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    ${new_contact}=  New Contact  new_firstname  new_middlename  new_lastname  new_nickname  new_title  new_company  new_address  new_fax  new_mobilephone  new_workphone  new_homephone  new_email  new_email2  new_email3  new_homepage  10  October  2015  13  november  2016  new_address2  new_secondaryphone  new_notes |
    Edit Contact  ${contact}  ${new_contact}
    ${new_list}=  Get Contact List
    ${new_contact}=  Fix New Contact Id  ${contact}  ${new_contact}
    Set List Value  ${old_list}  ${index}  ${new_contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}
