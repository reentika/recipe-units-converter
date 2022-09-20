#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 4, 2022

@author: reentika
"""
# introduction
print("What would you like to convert? \n The options are:\n ml to tsp OR tsp to ml \n lbs to kg OR kg to lbs \n inch to cm OR cm to inch \n *****Please enter only 'ml', 'tsp', 'lbs', 'kg', 'inch', or 'cm'")
unitA = input("Which unit do you want to convert from? ").lower()
unitB = input("Which unit do you want to convert it to? ").lower()
value = float(input("Enter the value of the first unit: "))

unit_options = ["ml", "tsp", "lbs", "kg", "cm", "inch"]
multiplying_numbers = [0.20, 4.92, 0.45, 2.20, 0.39, 2.54]


index = 0
# ml and tsp
if unitA == (unit_options[index]):
   answer = round(value*multiplying_numbers[index], 2)
   print(str(answer) + " teaspoons.")
   
elif unitA == (unit_options[index + 1]):
   answer = round(value*multiplying_numbers[index + 1], 2)
   print(str(answer) + " millileters.")
   
# lbs and kg
elif unitA == (unit_options[index + 2]):
   answer = round(value*multiplying_numbers[index + 2], 2)
   print(str(answer) + " kilograms.")
   
elif unitA == (unit_options[index + 3]):
   answer = round(value*multiplying_numbers[index + 3], 2)
   print(str(answer) + " pounds.")
   
# cm and inches
elif unitA == (unit_options[index + 4]):
   answer = round(value*multiplying_numbers[index + 4], 2)
   print(str(answer) + " inches.")

elif unitA == (unit_options[index + 5]):
   answer = round(value*multiplying_numbers[index + 5], 2)
   print(str(answer) + " centimeters.")
