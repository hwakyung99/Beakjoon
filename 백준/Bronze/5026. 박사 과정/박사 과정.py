n = int(input())
for _ in range(n):
    s = str(input())
    if(s.find('=') == -1):
        a, b = s.split('+')
        print(int(a) + int(b))
    else:
        print("skipped")
        
