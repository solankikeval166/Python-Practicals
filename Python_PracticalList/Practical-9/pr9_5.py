rows = 5

with open('triangle2.txt', 'w') as f:

    for i in range(1, rows+1):
        
        for j in range(rows-i):
            print(' ', end='', file=f)
        
        for k in range(2*i-1):
            print('*', end='', file=f)
        
        print('\n', end='', file=f)
        
print(f'The triangle was written to the file "triangle2.txt"')
