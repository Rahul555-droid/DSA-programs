"""
def drawline(ticklength, ticklabel=""):
# ”””Draw one line with given tick length (followed by optional label).”””
    line="-"*ticklength
    if ticklabel:
        line += "" + ticklabel
        print(line)
def drawinterval(centerlength):
#”””Draw tick interval based upon a central tick length.”””
    if centerlength > 0: # stop when length drops to 0
        drawinterval(centerlength-1) # recursively draw top ticks
        drawline(centerlength) # draw center tick
        drawinterval(centerlength-1) # recursively draw bottom ticks

def drawruler(numinches, majorlength):
    #”””Draw English ruler with given number of inches, major tick length.”””
    drawline(majorlength,0) # draw inch 0 line
    for j in range(1,1+numinches):
        drawinterval(majorlength-1) # draw interior ticks for inch
        drawline(majorlength,str(j)) # draw inch j line and label

drawruler(5,10)
"""

data=[]
for i in range(0,1000000):
    data.append(i)

##linear search
def lins(data,target):
    for i in range(0,len(data)-1):
        if data[i]==target:
            break

    if data[i]!=target:
        print("element not found")
        return
    
    return i



##BINARY SEARCH
def bins(data,target):
    return _bins(data,low=0,high=len(data)-1,target1=target)

def _bins(data,low,high,target1):

    if low>high:
        print("INVALID")
        return 
    
    else:
        mid=(low+high)//2
        if data[mid]==target1:
            return mid
        
        elif data[mid] > target1:
            return _bins(data,low=mid+1,high=high,target1=target1)

        else:
            return _bins(data,low=low,high=mid-1,target1=target1)

            
        





print("LINEAR SEARCH STARTED")
print(lins(data,322222))
print("BINARY SEARCH STARTED")
print(bins(data,322222))
