#Feature: Store Searching
#
#  Scenario: Search from the search bar
#      Given a web browser is at the opencart home page
#      When the user enters "Samsung" into the search bar
#      Then products related to "Samsung" are shown on the results page
#
#  Scenario: Searching from cathegory menu with subcategories
#      Given a web browser is at the opencart home page
#      When the mouse hovers on [category] from cathegory menu
#      And [category] has subcategories
#      Then subcategories related to [category] are displayed in popup menu
#
#  Scenario: Searching from popup menu related to subcategories
#      Given popup related to subcategories
#      When the user clicks on [subcategory] from given popup
#      Then products related to [subcategory] are shown on the results page
#
#  Scenario: Changing to [another subcategory] from same category
#      Given a web browser is at page dispalying products related to [subcategory]
#      When the user clicks on [another subcategory] from subcategory menu
#      Then only products related to [another subcategory] are dispalyed on result page
#
#  Scenario: All [subcategories] in [subcategory menu] and [popup subcategory menu] of same [category] are same
#      Given a web browser is at page dispalying products related to subcategory
#      When the user clicks on [category]
#      Then same [subcategories] are displayed in [popup subcategory menu]
#      And  same [subcategories] are displayed in [subcategory menu]
#
#  Scenario: Sorting products
#      Given a web browser is at page displaying products related to some subcategory
#      When the user chooses [rule] from [sort by menu] for products to be sorted by
#      Then all previous products are displayed based on [rule]
