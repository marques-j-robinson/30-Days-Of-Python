empty = ()
siblings = ('Shelby', 'Jeff', 'Olive')
sisters = ('Shelby', 'Olive')
brothers = ('Jeff', 'Sam')
siblings = sisters + brothers

print(f'I have {len(siblings)} siblings')

siblings = siblings + ('Tom', 'Beth')

family_members = siblings

siblings, parents = family_members[:len(family_members)-2], family_members[len(family_members)-2:]
print(siblings)
print(parents)

fruits = ('apples', 'orages', 'banana')
vegitables = ('grapes', 'kale', 'broccoli')
animal_products = ('beef', 'chicken', 'pork')

food_stuff_tp = fruits + vegitables + animal_products
food_stuff_lt = list(food_stuff_tp)

mid = len(food_stuff_tp)//2
food_stuff_tp = food_stuff_tp[:mid] + food_stuff_tp[mid+1:]

print(food_stuff_lt)
food_stuff_lt = food_stuff_lt[3:]
food_stuff_lt = food_stuff_lt[:len(food_stuff_lt)-3]
print(food_stuff_lt)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')