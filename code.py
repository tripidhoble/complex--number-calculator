# --------------
import pandas as pd
import numpy as np
import math


#Code starts here

#Task 1:
class complex_numbers():
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if         self.imag >= 0 else "-", abs(self.imag))

#Task 2:
    def __add__(self,other):
        result_real = self.real + other.real
        result_imag = self.imag + other.imag
        return complex_numbers(result_real,result_imag)

    def __sub__(self,other):
        result_real = self.real - other.real
        result_imag = self.imag - other.imag
        return complex_numbers(result_real,result_imag)

    def __mul__(self,other):
        result_real = (self.real * other.real) -  (self.imag * other.imag)
        result_imag = (self.imag * other.real) +  (self.real * other.imag)
        return complex_numbers(result_real,result_imag)
# Task 3:
    def __truediv__(self,other):
        result_real = ((self.real * other.real) +  (self.imag * other.imag))/(((other.real)**2) + ((other.imag)**2))
        result_imag = ((self.imag * other.real) -  (self.real * other.imag))/(((other.real)**2) + ((other.imag)**2))
        return complex_numbers(result_real,result_imag)
    
    def absolute(self):
        return (math.sqrt((self.real)**2 + (self.imag)**2))

    def argument(self):
        return math.degrees(math.atan((self.imag) / (self.real)))

    def conjugate(self):
        return complex_numbers(self.real,self.imag*(-1))

comp_1 = complex_numbers(3,5)
print("comp_1: ",comp_1)

comp_2 = complex_numbers(4,4)
print("comp_2: ",comp_2)

comp_sum = comp_1 + comp_2
print("comp_sum: ",comp_sum)

comp_diff = comp_1 - comp_2
print("comp_diff: ",comp_diff)

comp_prod = comp_1 * comp_2
print("comp_prod: ",comp_prod)

comp_quot = comp_1 / comp_2
print("comp_quot: ",comp_quot)

comp_abs = comp_1.absolute()
print("comp_abs: ",comp_abs)

comp_arg = comp_1.argument()
print("comp_arg: ",comp_arg) 

comp_conj = comp_1.conjugate()
print("comp_conj: ",comp_conj)








