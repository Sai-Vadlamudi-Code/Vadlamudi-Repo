#Printing pattern programs
     * 
    * * 
   * * * 
  * * * * 
 * * * * *
n=eval(input('enter the number of rows:'))
for i in range(1,n+1):
    print(' '*(n-i),'* '*i)
--------------------------------------------
# a right angled triangle pattern  
   *
   * *
   * * *
   * * * *
   * * * * *
   * * * * * *
   * * * * * * *
n = int(input("Enter number of rows:"))
for i in range(1,n+1):
print("* " * i)
