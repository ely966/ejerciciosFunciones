#1. Design a method called factorial that receives a positive integer and returns the factorial. If the number is negative the method should return -1.
def factorial(num):
    if num == 0: #en el caso que sea cero
        return(1)
    elif num == 1:# en el caso que sea 1
        return(1)
    elif num < 0:
        return(-1)
    elif num == -0: # en el caso que sea un numero negativo
        return(1)
    else: #en el caso que sea un numero que no corresponde a los casos anteriores, es decir positivo
        resultado = num
        for i in range (1,num): 
            resultado=resultado*i
        return(resultado)
    
#2. Design a method called leapYear that returns 1 if the number that receives the method is a leap year. 
#In other case, the method returns -1. A year is a leap year if it is multiple of 4 but the year is not multiple of 100 and not multiple of 400.

def leapYear(anno):
    if anno ==0: #en el caso que anno es 0
        return(-1)
    elif anno < 0: #en el caso que anno es menor de cero
        return(1)
    elif anno % 4 == 0 and anno % 100 != 0 and anno %400 != 0: #que anno sea multiplo de 4, y no de 100 ni de 400. es decir es anno bisiesto
        return(1)
    else: #en caso contrario, que no sea multiplo de 4 y si sea multiplo de 100 y 400. no bisiesto
        return(-1)
    
#3. Design a method called daysInMonth that returns the integer number of days in the month and year that received as arguments. 
#You can use the method leapYear. 
#If the arguments are not valid the method should return -1

def daysInMonth(month,anno):
    if anno ==0: #en el caso que anno es 0
        return(-1)
    elif anno < 0: #en el caso que anno es menor de cero
        return(-1)
    elif month > 12 or month < 0:
        return(-1)
    elif month == 4 or month == 6 or month == 9 or month == 11: # si es abril, junio, septiembre o noviembre
            return 30
    elif month == 2: # si es febrero
        if anno % 4 == 0 and anno % 100 != 0 and anno %400 != 0: #Bisiesto. que anno sea multiplo de 4, y no de 100 ni de 400. es decir es anno bisiesto
            return 29 # si es febrero de un anno bisiesto
        else:
            return 28 # si es febrero de un anno no bisiesto
    
    else: # si es otro mes que no sea mensionado antes
        return(31)


#4. Design a method called dayOfWeek that receives three integer parameters: day, month and year. 
#The method should return a number between 0 and 6 that is the day in the week for that date. 
#You have to know the next algorithm:
  
def dayOfWeek(day,month,year):
    #este es el algoritmo que hay que realizar para que funcione y nos diga el dia de la semana
    a=int((14 - month) / 12)
    y= int(year -a)
    m = int(month + 12 * a - 2)
    d=int((day + y + int(y/4) - int(y/100) + int(y/400) + int((31*m)/12))%7) #para que no cuente los decimales, hay que ponet int(para que sean enteros) en todas las divisiones
    return d




#5. Design a method called myPower that receives one integer and one integer positive numbers as parameters and the method calculates the power of the first parameter raised the second number. 
#You only can use the multiplication. 
#If the parameters are not right (the second parameter is negative) the method should return -1. 
#Remember that any number raised 0 is 1.

def myPower(num1,num2): #introduzcamos ambos numeros
    multi=num1 #le doy el vlaor num1 l valor multi  para que no tener que añadir uno al for
    if num2 ==0: # si el segundo numero es cero
        return 1
    elif num1 < 0 and num2 ==0: #si el primero es negativo y el segundo es cero
        return 1
    elif num2 < 0: # si el segundo numero es negativo
        return -1
    else: # si no es ninguo de los casos anteriores
        for i in range (1,num2):
            multi=multi*num1 #multiplica por si mismo el numero de veces que sea el otro
            i=i
        return multi # regresa la multiplicacion


   
#6. Design a method called numberOfNumbers that receives one integer positive number as parameter. 
#The method should return the number of digits of the number that received by parameter. 
#If the parameter is not valid the method should return -1.


def numberOfNumbers(num):
    if num < 0: #si numero es negativo
        return -1
    elif num == 0:# si numero es cero
        return 1
    else:
        contar=len(str(num)) #convierto el numero en un string y cuento sus caracteres
        return contar
#     contar=0
#     for i in (str(num)):
#         i=i
#         contar=contar+1
#     print(contar)



#
#7. Design a method called isPrime that receives one integer positive number greater than 0 as parameter.
# The method should return 1 if the number is prime or 0 if the number is not prime. 
#If the parameter is not valid the method should return -1.

def isPrime(num):
    contar=0
    if num == 0 or num < 0: #si el numero introducido es negativo o es cero 
        return -1
    else:
        for i in range (1,num):
            if num%i ==0: #para saber cuantos divisores tiene
                contar=contar+1 #que sume si tiene un divisor y vaya sumando cada divisor
        
        if contar > 2: #comprobar s es primo o no
            return 0 # si tiene mas de dos divisores no e sprimo
        else:
            return 1
        

#8. Design a method called secondOrder that receives three integer number as parameters. 
#This parameters are the coefficients of the an equation of a second order (ax2+bx+c=0) and the method returns the numbers of the solutions. 
#If the parameters are not valid the method should return -1

def secondOrder(a,b,c):
    #b²-4ac
    soluciones=(b*b)-4*a*c #la operacion que se realiza para averiguar cuantas soluciones tiene la ecuacion
    if soluciones == 0: #si las soluciones es cero
        return 1
    elif soluciones > 0: # si las soluciones son mas de cero
        return 2
    else: # si als soluciones es menor de cero
        return 0

#9. Design a method called numberDivisorPrime that receives a positive number as a parameter. 
#The method should return the number of prime divisors of the parameter. 
#If the parameter is not valid the method should return -1.

def numberDivisorPrime(num):
    if num < 0 or num == 0: #si el numero es negativo o es cero
        return 0
    
    else:
        cuantosdivi=0 # para sumar cuantos divisores primos tiene num
        cuenta=0 #para comprobar cuantos divisores tiene los divisores de num
        for d in range (1,num): #que cuente los numeros hasta num.
            if num %d ==0: # comprobar que si uno de esos numeros(d) es divisor de num
                for i in range (1,d): # si es divisor comprobamos si es primo o no para ello miramos los numeros primeros sus divisores
                    if d%i == 0:# si tiene un divisor 
                        cuenta=cuenta+1 #que los vaya contando los divisores. 
                if cuenta < 3: #Si ese divisor tiene menos de 3 divisores es primo
                    cuantosdivi=cuantosdivi+1 #sumamos que numero num tiene un divisor primos y lso vamos sumando
        return cuantosdivi



#10. Design a method called friend that receives two positive number as parameters. 
#The method should return true if the number are friends and false in other case. 
#Two numbers are friends if the addition of all the divisors less the same number of the one number is equal to the second number and in the other case too. 
#If the parameters are not valid the method should return false.

def friend(num,num2):
    sumadivisor=0 #para sumar los divisores

    for d in range (1,num): #recorra numeros desde 1 al primer numero
        if num % d == 0: #comprobar si d es divisor o no
            sumadivisor= sumadivisor+d #si es divisor vamos sumandolos

    if sumadivisor == num2: #si la suma de los divisores del primer numero 
        sumadivisor=0

        for d in range (1,num2): 
            if num2 % d == 0: #comprobar si d es divisor o no
                sumadivisor= sumadivisor+d #si es divisor vamos sumandolos

        if sumadivisor == num: #si la suma de divisores del segundo numero es igual al primer numero
            return True
        else:
            return False
    else: #si la suma de los divisores del primer numero no es igual al segundo numero. No son amigos
        return False





    