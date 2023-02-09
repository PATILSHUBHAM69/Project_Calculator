import math
import os


class Calculator:
    def variable(self):
        first_no = int(input("Enter the first number : "))
        second_no = int(input("Enter the second number : "))
        return first_no,second_no

    def continue_next_number(self,result):
        print(" Result = ",result)
        print("Select option :")
        print(" Enter '1' to continue calculation")
        print("Enter '2' to Exit from current calculation")

    def addition(self):
        first_no, second_no = self.variable()
        result = (first_no+second_no)
        print(" Result = ", first_no ," + ",second_no,)
        self.continue_next_number(result)
        x=int(input())

        while x != 2:
            print(" Enter the next number to add : ")
            pre_result = result
            next_num = int(input())
            result = result + next_num
            print("Result = ",pre_result," + ", next_num)
            self.continue_next_number(result)
            x= int(input())

    def substraction(self):
        first_no,second_no = self.variable()
        result = (first_no - second_no)
        print(" Result = ", first_no ," - ",second_no,)
        self.continue_next_number(result)
        x=int(input())

        while x != 2:
            print(" Enter the next number to substract : ")
            pre_result = result
            next_num = int(input())
            result = result - next_num
            print("Result = ",pre_result," - ", next_num)
            self.continue_next_number(result)
            x= int(input())

    def multiplication(self):
        first_no,second_no = self.variable()
        result = (first_no * second_no)
        print(" Result = ", first_no ," * ",second_no,)
        self.continue_next_number(result)
        x=int(input())

        while x != 2:
            print(" Enter the next number to multiply : ")
            pre_result = result
            next_num = int(input())
            result = result * next_num
            print("Result = ",pre_result," * ", next_num)
            self.continue_next_number(result)
            x= int(input())
    
    def Division(self):
        first_no,second_no = self.variable()
        result = (first_no / second_no)
        print(" Result = ", first_no ," / ",second_no,)
        self.continue_next_number(result)
        x=int(input())

        while x != 2:
            print(" Enter the next number to Divide : ")
            pre_result = result
            next_num = int(input())
            result = result / next_num
            print("Result = ",pre_result," / ", next_num)
            self.continue_next_number(result)
            x= int(input())

    def Remainder(self):
        first_no,second_no = self.variable()
        result = (first_no % second_no)
        print(" Result = ", first_no ," % ",second_no,)
        print("Result = ",result)

    def Floore_Division(self):
        first_no,second_no = self.variable()
        result = (first_no // second_no)
        print(" Result = ", first_no ," // ",second_no,)
        print("Result = ",result)

    def Square(self):
        user_input = int(input(" Enter the Number to find Square : "))
        print("Result = ", user_input * user_input)

    def Squareroot(self):
        user_input = int(input(" Enter the Number to find Squareroot : "))
        print("Result = ", math.sqrt(user_input))

    def Cube(self):
        user_input = int(input(" Enter the Number to find Cube : "))
        print("Result = ", user_input * user_input * user_input )

    def Cuberoot(self):
        user_input = int(input(" Enter the Number to find Cuberoot : "))
        print("Result = ", math.pow(user_input, 1/3) )

    def N_Degree_Number(self):
        user_input = int(input(" Enter the Base Number : "))
        power = int(input(" Enter the Power Number : "))
        print("Result = ", math.pow(user_input, power) )

    def N_Root_Number(self):
        user_input = int(input(" Enter the Number to find root : "))
        root_num = int(input(" Enter the required root number : "))
        print("Result = ", math.pow(user_input, 1/root_num) )

    def Currency_conversion(self):
        
        curr_list = ['1.Rupees','2.Dollar','3.Rubel','4.Dinar','5.Pound','6.Euro','7.Yuan']
        for i in curr_list:
            print(i, end='  ')

        conversion_curr = [1,82.18,1.17,269.61,101.31,90.38,12.22]
        select_curr = int(input(" \nSelect Your Currency : "))
        print(curr_list[select_curr-1])
        req_curr= int(input(" Select the required currency : "))
        print(curr_list[req_curr-1])
        print(" --------- Currency Conversion --------- ")
        amount = int(input(" Enter amount : "))
        print(curr_list[select_curr-1], " : ", amount)
        result= ((amount * conversion_curr[select_curr-1]) / conversion_curr[req_curr-1])
        print(curr_list[req_curr-1]," : ", result)

    def area_of_triangle(self):
        a = float(input('Enter length of first side: '))  
        b = float(input('Enter length of second side: '))  
        c = float(input('Enter length of third side: '))   
        s = (a + b + c) / 2  
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
        print('The area of the triangle is %0.2f' %area) 

    def percentage(self):
        amount = (float(input(" Enter the number : ")))
        percent = (float(input(" Enter the percentage value : ")))
        print(" Result  : ", (amount * (percent/100)))
    
    def split_bills(self):
        x=1
        while x>0:
            mem_dict={}
            mem_list=[]
            if mem_dict == {}:
                expense = int(input("Enter the Expense : "))
                no_of_member = int(input("Enter the no of member :"))
                split = expense/no_of_member
                for i in range(no_of_member):
                    
                    print("Enter the name of member ",i+1," : ")
                    member = input()
                    mem_list.append(member)

                    mem_dict[member]= [split]
            else:
                expense = int(input("Enter the Expense : "))
                no_of_member = int(input("Enter the no of member : "))
                split = expense/no_of_member
                for i in enumerate(mem_list):
                    print("---->",i)
                print('select the index, space seperated to add member in expence : ')
                members= (input().split())
                for i in members:
                    mem_dict[mem_list[int(i)-1]].append(split)
            
            print("---------Total Expence--------")
            final_exp={}
            for key,values in mem_dict.items():
                total = sum(values)
                final_exp[key]= total 
            print(final_exp)
            print(" Enter 1 to Continue\n Enter 0 to return to Home : ")
            user_decision=int(input())
            if user_decision!=1:
                x=0
                                         
while True:
    try:

        print("---------Welcome to Calculator Interface-----------")
        print(" *** Operations *** ")
        choices = ['1. Addition', '2. Substraction','3. Multiplication','4.Division','5.Remainder','6.Floore_Division','7.Square','8.Squareroot','9.Cube','10.Cuberoot','11.N_Degree_Number','12.N_Root_Number','13.Currency_conversion','14.area_of_triangle','15.percentage','16.split_bills']
        for i in choices:
            print("--->", i)


        choice = int(input(" Select Index to Perform Specific Operation : "))
        print(choice)
        obj = Calculator()


        operation_dict = {1:Calculator.addition,2:Calculator.substraction,3:Calculator.multiplication,4:Calculator.Division,
        5:Calculator.Remainder,6:Calculator.Floore_Division,7:Calculator.Square,8:Calculator.Squareroot,9:Calculator.Cube,
        10:Calculator.Cuberoot,11:Calculator.N_Degree_Number,12:Calculator.N_Root_Number,13:Calculator.Currency_conversion,
        14:Calculator.area_of_triangle,15:Calculator.percentage,16:Calculator.split_bills}      

        output=operation_dict[choice](obj)
    

        print("Enter 'c' to continue operations and Enter 'q' to Exit from Calculator")
        user_continue=input()
        if user_continue != 'c':
            break
    except:
        print("\nWrong Input.........! try Again")



        