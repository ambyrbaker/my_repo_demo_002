cart = ["apples", "bananas", "cherries"]
print(cart)
cart.append("donuts")
cart.append("milk")
cart.append("eggs")
print(cart)

cart.remove("cherries")
cart.pop(1) # takes an index place if we don't know the name
print(cart)
cart.pop()

cart.append("bananas")
cart.append("bananas")
print(cart)
cart.sort()
print(cart)

fruit = cart[0:3]
print(fruit)

count = cart.count("bananas")
print(count)

squares = []
for i in range(1,10):
    squares.append(i*i)
print(squares)

# use list comprehension to iterate thru shopping cart
new_cart = [x for x in cart if x.startswith("b")] #faster than a for loop
print(new_cart)

inventory = [0]*10
inventory = [4] = 100
print(inventory)

# creating a set
book_genres={} # creates a dictionary
book_genres.add("science fiction")
book_genres.add("mystery")
print(book_genres)
aset=set() # creates an empty set

lst = [1,1,1,2,2,3,3,4,4,5,5] # way to get rid of duplicates is to convert list to set
unique=set(lst)
print(unique)

#dictionary is the same as hashmap in java
fav_snacks = {'Ambyr' : 'chocolate', 'Kathleen' : 'pizza', 'Steve' : 'chips'}
steve = fav_snacks["Steve"]
print(steve)

for key in fav_snacks:
    print(fav_snacks[key])
for key, value in fav_snacks.items():
    print(key, value)

    print("hello world")
