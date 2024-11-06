# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. set roll list equal to empty list multiplied by 13

* purpose:sets number of rolls
* name: roll list
* parameters: none
* return: number
* algorithm:
  1.  set number variable equal to user inout
  2. convert number to int
  3. while number is less than 1
     1. output invalid number
     2. set number equal to user input
     3. convert number to int
  4. return number


* purpose: sets roll total and the list
* name: roll total
* parameters: count
* return: roll total
* algorithm:
  1.  set roll variable equal to the sum of two random ints between 1 and 6
  2. update roll list plus one using roll as an index
  3. update count plus one
  4. return roll


* purpose: prints asterisks for the score
* name: asterisk counts
* parameters: roll list
* return: none
* algorithm:
  1. prints sum of 2-12 using roll list index 0-10 multiplied by asterisks



* purpose:allows user to roll again
* name: roll again
* parameters: none
* return: choice
* algorithm:
  1. set choice equal to user input of either y or n
  2. convert choice to lower
  3. return choice


* purpose: runs game
* name: game
* parameters: none
* return: none
* algorithm:
  1. output a statement explaining game
  2. set count equal to 0
  3. call number rolls function by setting it equal to number
  4. while count is less than number
     1. call roll function by setting it equal to roll variable
     2. count plus equals 1
  5. output roll list
  6. call asterisk count function



* purpose: runs main program
* name: main
* parameters: none
* return: none
* algorithm:
  1. call game function
  2. call roll again by setting it equal to choice variable
  3. while choice = y
     1. call game function
  4. output thank you for playing

2. call main function