#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:37:01 2019

@author: adityakalia
"""

def factorial(value,number_of_people):
    fact = 1
    for i in range(1,number_of_people+1):
        fact = value * fact
        value = value - 1
    return fact


def number_of_people():
    print("Hi there, for this simulation, we need to know how many people are in the room")

    while True:
        try:
            number_of_people = int(input("\n Please enter the number of people in the room.\n"))
            break
        except ValueError:
            pass
        print("Incorrect input")
    return number_of_people


def all_same_birthdays(number_of_people):
    """
This function determines the probability that all people in the room share\
the exact same birthday
    @return:
    @param number_of_people:
    @return:
    """
    days_in_year = 365
    prob = ((1/days_in_year)**number_of_people)*100
    return prob


def no_same_birthdays(number_of_people):
    days_in_year = 365
    prob = 1 - ((1/days_in_year)**number_of_people)*100
    return prob


def two_same_birthdays(number_of_people):
    days_in_year = 365
    prob = (1 - factorial(days_in_year)/(days_in_year**number_of_people))*100


def main():
    number_of_people = number_of_people()


if __name__ == '__main__':
    main()
