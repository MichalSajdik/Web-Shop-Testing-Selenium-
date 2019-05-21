Feature: Shopping Cart

#  Scenario: Adding to shopping cart - unsuccessfully
#    Given a web browser is displaying details about product
#    When the user clicks Add to Cart
#    And all required information is not filled in
#    Then all required information that were not filled in are highlighted

  Scenario: Adding to shopping cart - successfully
    Given logged in account
    And a web browser is displaying details about product
    When the user clicks Add to Cart
    Then product is added to cart
    And message informing about successful operation is displayed

  Scenario: Adding to shopping cart with unrealistic parameters for quantity
    Given logged in account
    And a web browser is displaying details about product
    When Qty value is set to "66666666666666666"
    And all required information is filled in
    And the user clicks Add to Cart
    Then quantity in shopping cart should be "66666666666666666" or apropriate warning should be showed

  Scenario: Adding to shopping cart with not valid values for quantity
    Given logged in account
    And a web browser is displaying details about product
    When the user clicks Add to Cart
    And all required information is filled in
    And Qty value is set to "not valid value"
    Then error message is displayed to user
#
#  Scenario: Adding to shopping cart with not valid values for date
#    Given logged in account
#    And a web browser is displaying details about product
#    When the user clicks Add to Cart
#    And all required information is filled in
#    And [Date] value is set to "not valid value"
#    Then error message is displayed to user
#
  Scenario: Displaying shopping cart popup
    Given a web browser is at the opencart home page
    And user added item to shopping cart
    When the user clicks at cart total
    Then a popup is dispalyed with content of products in shopping cart

  Scenario: Viewing shopping cart through popup
    Given logged in account
    And a web browser is at the opencart home page
    And user added item to shopping cart
    When the user clicks at cart total
    And the user clicks at "View cart"
    Then web page of shopping cart is displayed

  Scenario: Viewing shopping cart through menu
    Given logged in account
    And a web browser is at the opencart home page
    When the user clicks at shopping cart button
    Then web page of shopping cart is displayed

  Scenario: Removing item from shopping cart
    Given logged in account
    And web page of shopping cart in displayed
    When the user clicks at the remove button
    Then item is removed from shopping card

