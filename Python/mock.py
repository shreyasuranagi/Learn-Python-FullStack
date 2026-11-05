s=input('enter:')
add=0
for ch in s:
    if '0'<=ch<='9':
        add=add+int(ch)
print(add)
