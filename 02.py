from collections import deque

def clean(s):
    s = s.strip().casefold()
    return ''.join(s.split())

def palindrom(d):
    n = len(d) // 2 
    p = True
    for i in range(n - 1):
        left = d.popleft()
        right = d.pop()
        p = True if left == right else False
        if not p:
            break
    return p

while True:
    inp = input('Enter string or q to exit: ')
    if inp == 'q': 
        break
    d = deque(clean(inp))
    print('Input string isa palindrom: ', palindrom(d))
    
    

