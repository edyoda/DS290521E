class bookmymovie:
    def __init__(self):
        self.row = int(input('Enter the number of rows\n'))
        self.col = int(input('Enter the number of seats in each row\n'))
        self.no_of_seats = self.row * self.col
        self.matrix = []
        self.seat_count = 0
        self.current_income = 0
        self.total_income = 0
        self.u_details = {}
        
        for i in range(self.row):
            a = []
            for j in range(self.col):
                a.append('S')
            self.matrix.append(a)
        self.total_revenue()
            
    def show_seats(self):
        print('\nCinema:')
        print(end='  ')
        for j in range(1,self.col+1):
            print(j,end=" ")
        print()
        a = 0
        for i in self.matrix:
            a+=1
            print(a,end=' ')
            print(' '.join(i),sep=",")
            
    def buy(self):
        a = int(input('Enter the row you want to book\n'))
        b = int(input('Enter the column you want to book\n'))
        if self.matrix[a-1][b-1] == "B":
            print('This seat is already booked!!')
            return
        elif self.no_of_seats < 60:
            price = 10
            print('Ticket per person is $10, do you want to proceed ahead? Press Y/y')
        elif a < self.row//2:
            price = 10
            print('Ticket per person is $10, do you want to proceed ahead? Press Y/y')
        else:
            price = 8
            print('Ticket per person is $8, do you want to proceed ahead? Press Y/y')
        
        user_input = input()
        
        if user_input == 'Y' or user_input == 'y':
            u_dict = {}
            Uname = input('For Booking, Enter your name\n')
            Ugen = input('Enter your gender\n')
            UAge = input('Enter your Age\n')
            UPn = input('Enter your Phone Number\n')
            self.matrix[a-1][b-1] = "B"
            self.seat_count+=1
            self.current_income += price
            u_dict[(a,b)] = [Uname,Ugen,UAge,UPn,price]
            self.u_details.update(u_dict)
            print('Booked Successfully!!')
        else:
            print("Booking could not be processed!\n")
    
    def info(self):
        check_a = int(input('Enter the row you booked\n'))
        check_b = int(input('Enter the col you booked\n'))
        
        if self.matrix[check_a-1][check_b-1] == "B":
            user = self.u_details[(check_a,check_b)]
            print('Name: ',user[0])
            print('Gender: ',user[1])
            print('Age: ',user[2])
            print('Phone No: ',user[3])
            print('Ticket Price: ',user[4])
        else:
            print("This seat is not booked yet!")
    
    def total_revenue(self):
        if self.no_of_seats < 60:
            self.total_income = self.no_of_seats*10
        elif self.no_of_seats >= 60:
            first_half_income = (self.row//2)*self.col*10
            second_half_income = (self.row - self.row//2)*self.col*8
            self.total_income = first_half_income+second_half_income
            
    def stats(self):
        print('Number of Purchased Tickets: ',self.seat_count)
        self.percentage = (self.seat_count/self.no_of_seats)*100
        print('Percentage of Tickets booked ',"{:.2f}".format(self.percentage))
        print('Current Income: ',self.current_income)
        print('Total Income: ',self.total_income)
    
    def menu(self):
        ans = True
        while ans:
            print("\nEnter the number corresponding to what you want to choose:")
            self.choice = int(input('\n1. Show the seats\n2. Buy a Ticket\n3. Statistics\n4. Show Booked Tickets User Info\n0.Exit\n'))
            if self.choice == 1:
                self.show_seats()
            elif self.choice == 2:
                self.buy()
            elif self.choice == 3:
                self.stats()
            elif self.choice == 4:
                self.info()
            elif self.choice == 0:
                ans = False
            else:
                print('\nNot Valid Choice, Try Again!!')

obj = bookmymovie()
obj.menu()