n=int(input("enter the decimal number: "))
hex_val=''
while n:
    rem=n%16
    if rem<=9:
        hex_val+=chr(48+rem)
    else:
        hex_val+=chr(55+rem)
    n=n//16
print(hex_val[::-1])
        
      
