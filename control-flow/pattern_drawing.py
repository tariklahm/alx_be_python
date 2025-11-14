rows =int(input("Enter the size of the pattern: "))

i=0
while i < rows :
    for j in range(1,rows+1):
        print(f"*",end="")
    print()
    i+=1