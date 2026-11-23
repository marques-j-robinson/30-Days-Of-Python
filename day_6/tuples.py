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