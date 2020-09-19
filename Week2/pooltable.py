# Pool Table Management

from datetime import datetime

listOfTables = []

class PoolTable:
    def __init__(self, number):
        self.number = number 
        self.startTime = None
        self.endTime = None 
        self.timePlayed = None
        self.isOccupied = False 
    
    def check_out(self):
        self.startTime = datetime.now()
        self.isOccupied = True
        self.endTime = None

    def check_in(self):
        self.endTime = datetime.now()
        self.timePlayed = self.endTime - self.startTime
        self.isOccupied = False
        with open ("pool_table_records.txt", "a") as file_object:
            file_object.write(f"Table Number: {self.number},\n Start Time: {self.startTime},\n End Time: {self.endTime},\n Time Played: {self.timePlayed}\n\n")

def menu():
    print("~~~~~~ Pool Table Management App ~~~~~~\n")
  
    
    while True:
        choice = input("""
        Please select a number from the following options:
    
        1 - View status of tables.
        2 - Begin new game at table.
        3 - Close table.
        4 - Quit.
        
        Number: """)

        if choice == "1":
            view_tables()

        elif choice == "2":
            table = int(input("Which table would you like to play on? "))
            table_number = listOfTables[table - 1]
            if table_number.isOccupied == True:
                print("\nTable is already occupied.")
            else:
                table_number.check_out()



        elif choice == "3":
            table = int(input("Which table were you playing on? "))
            table_number = listOfTables[table - 1]
            table_number.check_in()
        
        elif choice == "4":
            break


def view_tables():
    for index in range(1, 13):
        pool_table = listOfTables[index - 1]
        if pool_table.isOccupied == True:
            print(f"\nTable Number: {pool_table.number} - OCCUPIED - Start Time: {pool_table.startTime}")

        else:
            print(f"\nTable Number: {pool_table.number} - NOT OCCUPIED")
    

def add_table():
    for tableNumber in range(1,13):
        poolTable = PoolTable(tableNumber)
        listOfTables.append(poolTable)

add_table()
menu()




