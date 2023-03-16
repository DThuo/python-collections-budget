import Expense 


#Create the BudgetList class and constructor
class BudgetList:
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []



#define the append method

def append (self, item):
    if self.sum_expenses + item < self.budget:
        self.expenses.append(item)
        self.sum_expenses += item
    else:
        self.overanges.append(item)
        self.sum_overanges += item

#Define the __len__() method  
def __len__(self):
    return self.expenses.__len__ + self.overanges.__len__


#Define the main function

def main():
    myBudgetList = BudgetList #main
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)

    print('The count of all expenses: ' + str(len(myBudgetList)))  #Print the Length of myBudgetList


if __name__ == "__maina__":
    main()