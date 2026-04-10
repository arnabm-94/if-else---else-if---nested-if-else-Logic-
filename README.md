# if-else---else-if---nested-if-else-Logic-
This program is a simple login validation system that checks a user’s username and password using if, elif, else, and nested if-else statements. 

The program first uses an if statement to check whether the entered username contains the '@' symbol. This ensures the username looks like an email ID.

Once this condition is true, the program asks for the password and then uses multiple elif (else-if) conditions to handle different cases:

1. Both username and password are correct
2. Username is correct but password is wrong
3. Username is wrong but password is correct
4. Both username and password are wrong

Inside several elif blocks, the program uses nested if-else statements. These nested conditions allow the user to re-enter the incorrect credential and check it again before finally accepting or rejecting the login.

The else statement at the end runs when the username does not contain '@', indicating an invalid username format.

Overall, the use of if-elif-else helps the program choose between different login scenarios, while nested if-else allows retry logic for incorrect inputs, making the login process more interactive and structured.
