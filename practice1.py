#演習7

a = float(input())
b = float(input())
c = float(input())
d = float(input())

if(b<d):
    y_max = d
else:
    y_max = b

daikei = ((a + c) * y_max)/2
sankaku = daikei - c*d/2 - a*b/2
print(sankaku)