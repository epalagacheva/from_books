n = 100
sum = int (n * (n+1)/2)
print (sum)

for nuber in range(10, 20 ,5):
    
    print (nuber)

max=5
number=0
while number<max:
    number +=1
    print (number)
    
command = ''

#while command.lower() != 'quit':
 #   command = input('>')
  #  print(f"Echo: {command}")

for x in range (5):
    for y in range (5):
        if y>1:
            break
        print (f"({x},{y})")

#print("-- Type quit to exit")
#while True:
#    color= input ("What is you fav color:")
#    if color.lower() == 'quit':
#        break

hh = int(input ("Enter your number"))
print (hh)

while True:
    hh=input ("Enter your number:")
    if int(hh) < 0:
        break
print (hh)

if int(hh) < 0:
    sum  +=  int(hh)
    print (sum)

    
     
