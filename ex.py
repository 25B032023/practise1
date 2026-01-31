a=int (input())
b=int (input())
c=int(input())
if a>b and a>c:
    m=a
elif b>a and b>c:
    m=b
else:
    m=c
print(f"minimum equal to {m}")