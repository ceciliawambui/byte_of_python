print('Simple Assignment')
shoplist=['apple','mango','carrot','banana']
mylist=shoplist#mylist is just another name pointing to the same object!

del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
#notice that both shoplist and mylist both print the same without#
#the 'apple' confirming that they point to the same object#

print('Copy by making a full slice')
mylist = shoplist[:]
del mylist[0]

print('shoplist is',shoplist)
print('mylist is', mylist)
#notice that now the lists are different#