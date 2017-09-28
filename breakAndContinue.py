# break and continue used in for and while loops

# will print 1 2 3 4
for i in range(1,11):
    if i == 5:
        break
    print(i)

# will print 1 2 3 4 6 7 8 9 10
for i in range(1,11):
    if i == 5:
        continue
    print(i)
     
