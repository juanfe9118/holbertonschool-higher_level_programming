# Python - if/else, loops, functions
### This directory is for learning how to use the if/else statements as well as loops in Python. Below is a description of all the files contained in this directory.

#### lists.h
* Header file containing all the neccesary libraries for the C scripts in this project as well as the prototypes for all the functions.

#### 0-positive_or_negative.py
* Python script that prints whether the number stored in the variable number is positive or negative.

#### 1-last_digit.py
* Python script that prints the last digit of the number stored in the variable number.

#### 2-print_alphabet.py
* Python script that prints the ASCII alphabet, in lowercase, not followed by a new line.

#### 3-print_alphabt.py
* Python script that prints the ASCII alphabet, in lowercase except q and e, not followed by a new line.

#### 4-print_hexa.py
* Python script that prints all numbers from 0 to 98 in decimal and in hexadecimal.

#### 5-print_comb2.py
* Python script that prints all numbers from 0 to 99 separated by a comma and a space.

#### 6-print_comb3.py
* Python script that prints all possible different combinations of two digits.

#### 7-islower.py
* Python script that checks for lowercase character.

#### 8-uppercase.py
* Python script that prints a string in uppercase followed by a new line.

#### 9-print_last_digit.py
* Python script that prints the last digit of a number.

#### 10-add.py
* Python script that adds two integers and returns the result.

#### 11-pow.py
* Python script that computes a to the power of b and return the value.

#### 12-fizzbuzz.py
* Python script that prints the numbers from 1 to 100 separated by a space, for multiples of three print Fizz instead of the number and for multiples of five print Buzz and for numbers which are multiples of both three and five print FizzBuzz.

#### 13-insert_number.c
* C function that inserts a number into a sorted singly linked list.

#### 100-print_tebahpla.py
* Python script that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.

#### 101-remove_char_at.py
* Python script that creates a copy of the string, removing the character at the position n (not the Python way, the "C array index").

#### 102-magic_calculation.py
* Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:

  3           0 LOAD_FAST                0 (a)
	      3 LOAD_FAST                1 (b)
	      6 COMPARE_OP               0 (<)
	      9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
	     34 BINARY_ADD
	     35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
