#THINGS TO KEEP IN MIND:
# - I have previous coding experience and have implemented complicated things so some parts may not make sense
# - I realize that the code is messy and needs to be touched up
# ------------------------------------------------------------------------------------------------------------------------
# Mitchell Braun
# 10/23/2018
# Assignment 3 part 1


def programmer():
    while(True):
        Decimal = 0;
        BinaryNumber = "";

        while(True):
            print("");
            Decimal = int(input("What is the decimal number?"));
            print("");
            if Decimal < 0 :
                print("");
                print("Please Enter a decimal number that is not negative");
                print("");
            else:
                break;
    
        while not (Decimal < 1):
            if Decimal % 2 == 1:
                BinaryNumber = BinaryNumber + "1";
                Decimal = Decimal // 2;
            if Decimal % 2 == 0:
                BinaryNumber = BinaryNumber + "0";
                Decimal = Decimal // 2;

        BinaryNumber = BinaryNumber[::-1];

        while True:  
            i = 0;
            if int(BinaryNumber[i]) == 1:
                break;
            if int(BinaryNumber[i]) == 0:
                BinaryNumber = BinaryNumber[:i] + BinaryNumber[i + 1:];
            i = i+1;

        print("");
        print("Binary Number: ", BinaryNumber);
        print("");
        while(True):
            print("");
            print("Do you want to do another calculation? -- Type 'Y' for yes and 'N' for no");
            repeat = input("");
            if repeat == "N":
                break;
            elif repeat == "Y":
                print("");
                print("LOL ok nerd");
                print("");
                break;
            else:
                print("");
                print("Please put in 'Y' or 'N'");
                print("");
        if(repeat == "N"):
            break;

def scientific():
    while(True):  
        myList = [0] * 3;
        result = 0;
        while(True):   
            while(True):
                try:
                    print("");
                    print("Type an equation -- SPACES inbetween the characters -- Ex: 2 + 2 & Ex: 2 ** 3");
                    equation = input("");
                    myList[0], myList[1], myList[2] = equation.split();
                    break;
                except ValueError:
                    print("");
                    print("Please enter a valid input");
                    print(""); 
            if myList[1] == "+":
                result = int(myList[0]) + int(myList[2]);
                break;
            elif myList[1] == "-":
                result = int(myList[0]) - int(myList[2]);
                break;
            elif myList[1] == "*":
                result = int(myList[0]) * int(myList[2]);
                break;
            elif myList[1] == "/":
                result = int(myList[0]) / int(myList[2]);
                break;
            elif myList[1] == "**":
                result = int(myList[0]) ** int(myList[2]);
                break;
            else :
                print("");
                print("Please put a valid input");
                print("");
        print("");
        print("Solution: ", result);
        print("");
        while(True):
            print("");
            print("Do you want to do another calculation? -- Type 'Y' for yes and 'N' for no");
            print("");
            repeat = input("");
            if repeat == "N":
                break;
            elif repeat == "Y":
                print("");
                print("LOL ok nerd");
                print("");
                break;
            else:
                print("");
                print("Please put in 'Y' or 'N'");
                print("");
        if(repeat == "N"):
            break;


while(True):
    print("");
    print("Welcome to Assignment 3 part 1");
    print("You have the choice of using Progammer mode or Scientific mode");
    print("Type programmer or scientific for choosing the mode.      ");
    print("");
    switch = input("");
    
    if switch == "programmer":
        checker = True;
        programmer();
        while(True):
            print("");
            print("Do you wanna switch? -- Type 'Y' for yes and 'N' for no");
            print("");
            repeat = input("");
            if repeat == "N":
                break;
            elif repeat == "Y":
                print("");
                print("LOL ok nerd");
                print("");
                if checker == True:
                    scientific();
                    checker = False;
                else:
                    programmer();
                    checker = True;
            else:
                print("");
                print("Please put in 'Y' or 'N'");
                print("");

        break;
    elif switch == "scientific":
        checker = True;
        scientific();
        while(True):
            print("");
            print("Do you wanna switch? -- Type 'Y' for yes and 'N' for no");
            print("");
            repeat = input("");
            if repeat == "N":
                break;
            elif repeat == "Y":
                print("");
                print("LOL ok nerd");
                print("");
                if checker == True:
                    programmer();
                    checker = False;
                else:
                    scientific();
                    checker = True;
            else:
                print("");
                print("Please put in 'Y' or 'N'");
                print("");

        break;
    else :
        print("");
        print("Please type in 'programmer' or 'scientific'");
        print("");
        switch = "";