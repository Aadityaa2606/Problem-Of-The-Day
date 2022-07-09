fav = list(input(''))
n = int(input())
books=[]
for i in range(n):
    books.append(input())

tempbook = books.copy()

for i in books:
    for j in fav:
        if j not in i:
            tempbook.remove(i)

if len(tempbook) == 0:
    print('No such book')
else:
    for i in tempbook:
        print(i)
