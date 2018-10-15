# A brief description of the project
# 10/1/18
# CTI-110 P5HW1 - Prime Numbers
# Brandon Jones

def is_prime(number):
  evenDivision=0
  if number<=1:
      return False
  for currentnumber in range( 1, number+1):
      if number%currentnumber==0:
          evenDivision=evenDivision+1
      if evenDivision>2:
          return True
          
  

def main():
    number=int(input('Please enter a number'))
    if is_prime(number):
        print('number is prime')
    else:
        print('number isnt prime')
main()



