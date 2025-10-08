a,b,c=map(int,input().split())
if a < (b+c) and b < (a+c) and c < (a+b):
    if a==b==c:
        print("Tam giác đều")
    elif a==b or b==c or a==c:
        print("Tam giác cân")   
    else:
        print("Tam giác thường")        
else:
    print("Không phải tam giác") 