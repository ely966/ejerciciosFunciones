
import unittest
import ejercicios
# from Crypto.SelfTest import SelfTestError



class Test(unittest.TestCase):

    def testData(self):
        self.assert_(ejercicios.factorial(1) == 1)
        self.assert_(ejercicios.factorial(0) == 1)
        self.assert_(ejercicios.factorial(5) == 120)
        self.assert_(ejercicios.factorial(-55) == -1)
        self.assert_(ejercicios.factorial(-0) == 1)
         
        self.assert_(ejercicios.leapYear(2021) ==-1)
        self.assert_(ejercicios.leapYear(2022) ==-1)
        self.assert_(ejercicios.leapYear(0) ==-1)
        self.assert_(ejercicios.leapYear(-2020) ==1)
        self.assert_(ejercicios.leapYear(2024) ==1)
        
        self.assert_(ejercicios.daysInMonth(2,2021) == 28 )
        self.assert_(ejercicios.daysInMonth(24,2022) == -1 )
        self.assert_(ejercicios.daysInMonth(2,-2020) == -1)
        self.assert_(ejercicios.daysInMonth(1,2023) == 31)
        self.assert_(ejercicios.daysInMonth(2,2023) == 28)
        self.assert_(ejercicios.daysInMonth(3,2023) == 31)
        self.assert_(ejercicios.daysInMonth(2,2020) == 29)
        self.assert_(ejercicios.daysInMonth(4,2023) == 30)
        self.assert_(ejercicios.daysInMonth(5,2023) == 31)
        self.assert_(ejercicios.daysInMonth(6,2023) == 30)
        self.assert_(ejercicios.daysInMonth(7,2023) == 31)
        self.assert_(ejercicios.daysInMonth(8,2023) == 31)
        self.assert_(ejercicios.daysInMonth(9,2023) == 30)
        self.assert_(ejercicios.daysInMonth(10,2023) == 31)
         
        self.assert_(ejercicios.dayOfWeek(29,10,2019) == 2)
        self.assert_(ejercicios.dayOfWeek(2,2,2020) == 0)
        self.assert_(ejercicios.dayOfWeek(30,10,2019) == 3)
        self.assert_(ejercicios.dayOfWeek(2,11,2019) == 6)
        self.assert_(ejercicios.dayOfWeek(3,11,2019) == 0)
        self.assert_(ejercicios.dayOfWeek(4,11,2019) == 1)
#         
        self.assert_(ejercicios.myPower(29,0)==1)
        self.assert_(ejercicios.myPower(-12,0)==1)
        self.assert_(ejercicios.myPower(-2,2)== 4)
        self.assert_(ejercicios.myPower(-2,3)== -8)
        self.assert_(ejercicios.myPower(3,-3)== -1)
        self.assert_(ejercicios.myPower(2,8)==256)
        
        self.assert_(ejercicios.numberOfNumbers(29)==2)
        self.assert_(ejercicios.numberOfNumbers(-12)==-1)
        self.assert_(ejercicios.numberOfNumbers(2)==1)
        self.assert_(ejercicios.numberOfNumbers(201)==3)
        self.assert_(ejercicios.numberOfNumbers(0), 1)
        self.assert_(ejercicios.numberOfNumbers(29874)==5)

        self.assert_(ejercicios.isPrime(29)==1)
        self.assert_(ejercicios.isPrime(-12)==-1)
        self.assert_(ejercicios.isPrime(2)==1)
        self.assert_(ejercicios.isPrime(201)==0)
        self.assert_(ejercicios.isPrime(0)==-1)
        self.assert_(ejercicios.isPrime(100)==0)
        self.assert_(ejercicios.isPrime(4)==0)
# 
        self.assert_(ejercicios.secondOrder(1,-5,6) == 2)
        self.assert_(ejercicios.secondOrder(2,-7,3) == 2)
        self.assert_(ejercicios.secondOrder(1,-2,1) == 1)
        self.assert_(ejercicios.secondOrder(1,1,1) == 0)
#         
        self.assert_(ejercicios.numberDivisorPrime(8)== 2)
        self.assert_(ejercicios.numberDivisorPrime(-8)== 0)
        self.assert_(ejercicios.numberDivisorPrime(0)== 0)
        self.assert_(ejercicios.numberDivisorPrime(21)== 3)
#             
        self.assert_(ejercicios.friend(220,284) == True)
        self.assert_(ejercicios.friend(8,-2) == False)
        self.assert_(ejercicios.friend(-8,8) == False)
        self.assert_(ejercicios.friend(6,6) == True)
        self.assert_(ejercicios.friend(21,21) == False)
#         
#                 
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()