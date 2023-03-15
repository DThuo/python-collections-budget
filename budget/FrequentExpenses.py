import Expense  #do no use from to avoid error
import collections
import matplotlib.pyplot as plt

#variable expences and read spending data
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

# creating a list of spending categories
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)


#Count categories with a counter collection

spending_counter = collections.Counter(spending_categories)
print(spending_counter)

#get the top 5 categories

top5 = spending_counter.most_common(5)

print(top5)


#Convert the Dictionary to 2 Lists using zip()

categories, count = zip(*top5)
print(categories)
print(count)


#Plot the Top 5 Most Common Categories

fig, ax = plt.subplots()     #initialize fig

ax.bar(categories, count)     #create bar chart

ax.set_title('# of Purchases by Category')  # adding title

ax.bar(categories, count, color=['red', 'black', 'black', 'black', 'black']) #change bar color 

#display the graph

plt.show()








