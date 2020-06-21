t = int(float(input()))

for i in range (t):
    
    r,c,k = map(int, input().split())

    #Approach 1:
    '''
    A cell (X,Y) can be visited if max(∣X−r∣,∣Y−c∣)<=K
    '''
    count = 0

    for x in range(1,9):
        for y in range(1,9):
            if max(abs(x-r), abs(y-c))<=k:
                count += 1

    print(count)

    #Approach 2:

    '''
    The possible cells king can visit will form a square (or rectangle, depending on where he is placed). The area of this figure is the answer.

    dx and dy are length of horizontal and vertical sides of rectangle

    The +1+1+1 in the formula is to account for the row/column the king is standing it.
    '''
    dx = min(c+k,8) - max(c-k,1) + 1
    dy = min(r+k,8) - max(r+k,8) + 1
    print (dx*dy)