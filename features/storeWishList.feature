Feature: Store Wish list


    Scenario: Registering into page
      Given a logout page: "http://mys01.fit.vutbr.cz:8064/index.php?route=account/logout" is displayed
      When user went to registration page: "http://mys01.fit.vutbr.cz:8064/index.php?route=account/register"
      Then a "http://mys01.fit.vutbr.cz:8064/index.php?route=account/register" page is displayed


    Scenario: Adding product to wish list
      Given a web page displaying details about product "http://mys01.fit.vutbr.cz:8064/index.php?route=product/product&product_id=40"
      When the user clicks on function Add to Wish List
      Then a message informing of success is displayed


    Scenario: Viewing product in wish list
      Given a web page displaying details about product "http://mys01.fit.vutbr.cz:8064/index.php?route=product/product&product_id=40"
      When the user clicks on Wish List
      Then login page: "http://mys01.fit.vutbr.cz:8064/index.php?route=account/login" is displayed, because user is not logged in

#    Scenario: Deleting product from wish list
#      Given wish list page: "http://mys01.fit.vutbr.cz:8064/index.php?route=account/wishlist"
#      When the user clicks on first delete button belonging to one of products
#      Then selected product is removed from wish list
#      And deleted product is not displayed anymore
#
#    Scenario: Viewing details about product from wish list through image
#      Given all products diplayed in wish list
#      When the user clicks on image of one of products
#      Then details about product are shown on result page
#
#    Scenario: Viewing details about product from wish list through product name
#      Given all products diplayed in wish list
#      When the user clicks on product name of one of products
#      Then details about product are shown on result page
