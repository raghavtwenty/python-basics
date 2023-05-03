''' Q1.
If the cost price and selling price of an item is an input through keyboard, 
write a program to determine whether the seller has made profit or incurred loss. 
Also determine how much profit he made or loss he incurred. '''

# Date Created : 17-11-2021 | Date Edited : 17-11-2021

print('\nProfit & Loss Calculator.\n')
cost_price = float(input('Enter Cost Price Of The Object: '))
selling_price = float(input('Enter Selling Price Of The Object: '))

if cost_price > selling_price:
	print(f'\nThere Is A Loss By, {cost_price - selling_price} INR.')
elif selling_price > cost_price:
	print(f'\nThere Is Profit By, {selling_price - cost_price} INR.')
else:
	print(f'\nNeither Loss Nor Profit.')