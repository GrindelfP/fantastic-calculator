# Fantastic Calculator v 2.0.0
## Program's components
1) **calculator_main.py** contains two main executable functions of calculator - print_intro() and perform_calculating()
(greeting and calculating).

2) **user_communication** directory consists 3 .py files:
     
     a) **greetings.py**, which contains functions, used to greet user.
     
     b) **user_input.py**, which contains functions of receiving and checking mistakes of user's number input.
     
     c) **calculator_processor.py**, which contains output of calculation.
         
3) **calculation directory** consists **calculation.py** file, containing code of final calculating and receiving of the result.
    
4) **operators** directory consists 3 .py files:
    
    a) **operations.py**, which contains all operators' calculation methods.
        
    b) **operators_class.py**, which contains class Operator, used to store operators' data.

    c) **operators_list.py**, which contain dictionaries of operator's symbols and regexes.
    
5) **checking** directory consists **operator_checking.py** file with functions, checking if user's operator is valid and if it is binary  

6) (github component) **.gitignore**

## How to use the Calculator
When You start the calculator it - 
1) welcomes You and asks You about Your name to greet You by Your name
2) explains, what operations and with what operators You can do
3) asks You to print Your first number, operator and (in some cases) second
number of Your calculation
##### Important: when You want radical(root), logarithm or exponentiation You should type Your operator as it was shown in the list and instead of "i" print there index You want
4) (optional) shows You Your mistakes and asks to correct them
5) prints You the result of Your calculation
6) asks if You want to exit the Calculator or continue calculating.

## Calculator's functional
Fantastic Calculator can do following operations: 
1) addition 
2) subtraction 
3) multiplication 
4) division
5) exponentiation of power "i" 
6) modulus 
7) radical based on natural number "i" (root with a natural index) 
8) factorial  
9) logarithms based on natural number "i"
10) natural logarithms
11) logarithms based on 10