# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

* Purpose: counts rolls
* name: roll counter
* parameters: none
* return: roll list
* algorithm:
  1. set count equal to 0
  2. while count is less than num rolls
     1. if num rolls > 0
        1. roll total is equal to a random int between 2 and 12
        2. roll list using roll total index - 2 is plus equal to 1
        3. count plus equal to 1
  3. return roll list

* Purpose: prints score
* name: sum tally
* parameters: none
* return: none
* algorithm:
  1. prints sum of 2-12 using roll list index 0-10 multiplied by asterisks
  2. call roll counter
  3. call sum tally

* Purpose: runs main program
* name: main
* parameters: none
* return: num rolls and roll list
* algorithm:
  1. call roll counter
  2. call sum tally
  3. return num rolls and roll list


1. call main