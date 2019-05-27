class Person:
    def __init__(self, name):
        self.name = name
        print(self.name)
p = Person('Jayden')
p = Person('Melvis')
p = Person('Elvis')
p = Person('Sandra')
p = Person('Lynn')
p = Person('Cecilia')
Address_book = {
    'Jayden':'jaydenmartin@gmail.com',
    'Melvis':'melvismay@hotmail.com',
    'Elvis' :'elvisjohn@gmail.com',
    'Sandra':'sandrajey@gmail.com',
    'Lynn':'lynnellen@gmail.com',
    'Cecilia':'ceciliawambui026@gmail.com'}
del Address_book['Melvis']
for name, address in Address_book.items():
    print('Contact {0} at {1}'.format(name, address))
Address_book['Mark'] = 'markmaina@gmail.com'

if 'Mark' in Address_book:
    print("\n Mark's address is",Address_book['Mark'])

import pickle
Address_bookfile = 'Address_book.data'
f = open(Address_bookfile,'wb')
pickle.dump(Address_book,f)
f.close()





