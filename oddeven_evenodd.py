# program to check the given num is in seqyence of even odd or odd even#
n=int(input())#12345
while(n!=0):
    r=n%10#5
    n=n//10#1234
    break
if r%2==0:#5%2!=0
    s="even"
else:
    s="odd"#s=odd
while (n!=0):#n=1234
    r=n%10#4
    n=n//10#123
    if(s=="even" and(r%2==1)):
        s="odd"
    elif(s=="odd" and (r%2==0)):#s=odd and 4%2==0 so even
        s="even"
    else:
        print("not a waveform")
        break
else:
    print("waveform")
