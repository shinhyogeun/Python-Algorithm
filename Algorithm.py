# code up 59번
"""a= int(input())
print("%d" %~a)"""

# code up 60번
#a,b = map(int,input().split())
#print(a&b)

#code up 61번
#a,b = map(int,input().split())
#print(a|b)

#code up 62번
#a,b = map(int,input().split())
#print(a^b)

#code up 63번
#a,b,c = map(int,input().split())
#print("%d" %((a if a<b else b) if (a if a<b else b)<c else c))

#code up 64번
'''a = list(map(int,input().split()))
for i in range(3) :
    if a[i]%2 == 0 :
        print("even")
    else :
        print("odd")'''

#code up 67번
'''a = list(map(int,input().split()))
for i in range(3) :
    if a[i]%2 == 0 :
        if a[i] < 0 :
            print("minus")
        else :
            print("plus")
        print("even")
    else :
        if a[i] < 0 :
            print("minus")
        else :
            print("plus")
        print("odd")'''

#code up 68번

"""a = int(input())

if 100>=a>=90:
    print("A")
elif 89>=a>=70:
    print("B")
elif 69>=a>=40:
    print("C")
elif 39>=a>=0:
    print("D")"""

#code up 69번

"""a = input()

if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else :
    print("what?")"""

#code up 70번

'''a = int(input())
if a in [12,1,2]:
    print("winter")
elif a in [3,4,5]:
    print("spring")
elif a in [6,7,8]:
    print("summer")
elif a in [9,10,11]:
    print("fall")'''

#code up 71번
'''a = map(int,input().split())
for i in a:
    if i == 0:
        break
    print(i)'''

#code up 72번
'''a = int(input())
b = list(map(int,input().split()))

for i in range(a):
    print(b[i])'''

#code up 73번

'''b = list(map(int,input().split()))
for i in b:
    if i == 0:
        break
    print(i)'''

#code up 74번

'''a = int(input())

for i in range(a):
    print(a)
    a -= 1'''

#code up 74번

'''a = int(input())

for i in range(a):
    a -= 1
    print(a)'''

#code up 75번

'''a = input()
b = ""
for i in range(ord(a)-96):
    b = b + chr(97+i) + " "
    if i == ord(a)-97:
        print(b)'''

#code up 77번

'''a = int(input())
for i in range(a+1):
    print(i)'''

#code up 78번

'''a = int(input())
b = 0
for i in range(1,a+1):
    if i % 2 == 0 :
        b = b + i
print(b)'''

#code up 79번

'''a = input().split()

for i in a:
    print(i)
    if i == "q":
        break'''

#code up 80번

'''a = int(input())
b = 0
i = 0
while b < a:
    i += 1
    b = b + i
print(i)'''

#code up 81번

'''a,b = map(int,input().split())
for i in range(a):
    for j in range(b):
        print(i+1, j+1)'''

#code up 82번

'''a = input()
b = int(a,16)
for i in range(1,16):
    print("%c*%X=%X" %(a,i,b*i))'''

#code up 83번

'''a = int(input())
x = [3,6,9]
answer = ""
for i in range(a):
    if i+1 in x:
        answer = answer + "X" + " "
    else:
        answer = answer + str(i+1) + " "
print(answer)'''

#code up 84번

'''a,b,c = list(map(int,input().split()))
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
print(a*b*c)'''

#code up 85번

'''h,b,c,s = list(map(int,input().split()))
result = (h*b*c*s)/(2**23)
print("%.1f MB" %result)'''

#code up 86번
'''w,h,b = list(map(int,input().split()))
result = w*h*b / 2**23
print("%.2f MB" %result)'''

#code up 87번
'''a = int(input())
b = 0
i = 0
while b < a:
    i += 1
    b = b + i
print(b)'''

#code up 88번
'''a = int(input())
result = ""
for i in range(1,a+1):
    if i%3 != 0:
        result = result + "%d " %i
print(result)'''

#code up 89번

'''a,b,c = list(map(int,input().split()))
print(a+(c-1)*b)'''

#code up 90번

'''a,b,c = list(map(int,input().split()))
print(a*(b**(c-1)))'''

#code up 91번

'''a,b,c,d = list(map(int,input().split()))
i = 0
def make_it_real(s):
    global i
    i = i + 1
    if i == d:
        print(s)
        return
    s = (s*b)+c
    make_it_real(s)
make_it_real(a)'''

#code up 92번

'''a,b,c = list(map(int,input().split()))
day = 1
while day%a != 0 or day%b != 0 or day%c != 0:
    day += 1
print(day)'''

#code up 93번

'''a = ""
c = int(input())
b = list(map(int,input().split()))
for i in range(1,24):
     a = a + str(b.count(i)) + " "
print(a)'''

#code up 94번

'''a = ""
c = int(input())
b = list(map(int,input().split()))
for i in range(1,c+1):
     a = a + str(b[-i]) + " "
print(a)'''

#code up 95번

'''a = int(input())
b = list(map(int,input().split()))
b.sort()
print(b[0])'''

#code up 96번
'''a = int(input())
result = [[0]*19 for i in range(19)]
b = [[0]*2 for i in range(a)]
c = 1
f = 0
result2 = ""
while c <= a :
    b[c-1] = list(map(int,input().split()))
    b[c-1] = [b[c-1][0]-1,b[c-1][1]-1]
    result[b[c-1][0]][b[c-1][1]] = 1
    c = c + 1
for i in range(19):
    for j in range(19):
        result2 = result2 + str(result[i][j]) + " "
    print(result2)
    result2 = "" '''

#code up 97번

'''a = [[0]*19 for i in range(19)]
for i in range(19):
    b = list(map(int,input().split()))
    a[i] = b
b = int(input())
i = 0
result2 = ""
while i < b:
    c = list(map(int,input().split()))
    row = c[0]
    col = c[1]
    for j in range(19):
        if a[row-1][j] == 0:
            a[row-1][j] = 1
        elif a[row-1][j] == 1:
            a[row-1][j] = 0
    for j in range(19):
        if a[j][col-1] == 0:
            a[j][col-1] = 1
        elif a[j][col-1] == 1:
            a[j][col-1] = 0
    i += 1
for k in range(19):
    for h in range(19):
        result2 = result2 + str(a[k][h]) + " "
    print(result2)
    result2 = "" '''

# code up 98번

'''a, b = map(int,input().split())
c = [[0]*b for r in range(a)]
d = int(input())
i = 0
result2 = ""
while i < d:
    i += 1
    barlength,isThatRow,startXpoint,startYpoint = list(map(int,input().split()))
    if isThatRow == 0:
        for asd in range(barlength):
            c[startXpoint-1][startYpoint-1+asd] = 1
    else:
        for asd in range(barlength):
            c[startXpoint-1+asd][startYpoint-1] = 1
for k in range(a):
    for j in range(b):
        result2 = result2 + str(c[k][j]) + " "
    print(result2)
    result2 = "" '''

# code up 99번
'''miro = [[0]*10 for _ in range(10)]
whereIsAnt = [1,1]
for i in range(10):
    a = list(map(int,input().split()))
    miro[i] = a
result2 = ""

if miro[whereIsAnt[0]][whereIsAnt[1]] == 2 :
    miro[whereIsAnt[0]][whereIsAnt[1]] = 9
    trigger = False
else :
    miro[whereIsAnt[0]][whereIsAnt[1]] = 9
    trigger = True

while trigger:
    if miro[whereIsAnt[0]][whereIsAnt[1]+1] == 0:
        if miro[whereIsAnt[0]][whereIsAnt[1]+1] != 2:
            miro[whereIsAnt[0]][whereIsAnt[1]+1] = 9
        elif miro[whereIsAnt[0]][whereIsAnt[1]+1] == 2:
            miro[whereIsAnt[0]][whereIsAnt[1] + 1] = 9
            trigger = False
        whereIsAnt = [whereIsAnt[0],whereIsAnt[1]+1]
    elif miro[whereIsAnt[0]][whereIsAnt[1]+1] == 1:
        if miro[whereIsAnt[0]+1][whereIsAnt[1]] == 1:
            trigger = False
        elif miro[whereIsAnt[0]+1][whereIsAnt[1]] == 0:
            miro[whereIsAnt[0]+1][whereIsAnt[1]] = 9
        elif miro[whereIsAnt[0]+1][whereIsAnt[1]] == 2:
            miro[whereIsAnt[0]+1][whereIsAnt[1]] = 9
            trigger = False
        whereIsAnt = [whereIsAnt[0]+1, whereIsAnt[1]]
    elif miro[whereIsAnt[0]][whereIsAnt[1]+1] == 2:
        miro[whereIsAnt[0]][whereIsAnt[1] + 1] = 9
        trigger = False
for k in range(10):
    for j in range(10):
        result2 = result2 + str(miro[k][j]) + " "
    print(result2)
    result2 = "" '''