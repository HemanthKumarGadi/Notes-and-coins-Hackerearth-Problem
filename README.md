# Notes-and-coins-Hackerearth-Problem
Notes and coins Hackerearth Problem Solution
Question asked for Tiger analytics Hiring Coding round
Probel Statement :
Problem
You are given M number of coins and P number of notes.

Write a program to separate the two forms of money without creating two separate classes for notes and coins.

(The order of the output should be the same as that of the input).

Input format

First line : N
Next N lines : Space-separated string S and an integer 
 (where S is either a Coin or a Note and 
 denotes the denomination of a coin or a note)
Output format
Print the string Coins : followed by M lines, each of which contains an integer denoting the denominations of the coins.
Print the string Notes : followed by P lines, each of which contains an integer denoting the denominations of the notes.

Constraints


Description of Classes:

You need to design 3 classes:

Bag
Coin
Note
Note and Coin Class
Both the classes have common attributes as well as common methods.

Attributes:
Val: refers to the denomination of the coin or note

Methods:
setvalue(int val): Set the denomination of the coin to the value which is passed as a parameter.

Bag Class
This should be a generic class.

Methods
add(Type t): Add the coin or note to the bag.
Display(): Display the denomination of the coin or note.

Sample Input
7
Note 83
Coin 19
Coin 85
Note 8
Note 30
Coin 56
Coin 53
Sample Output
Coins :
19
85
56
53
Notes :
83
