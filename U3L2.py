num = int(input('How many items are you entering? '))
items = []
for i in range(num):
  item = input('Item: ')
  items.append(item)
print('You have entered the following of',num,'items:')
print(items)
