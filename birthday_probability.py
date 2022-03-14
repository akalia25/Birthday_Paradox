#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:37:01 2019

@author: adityakalia
"""


def number_of_people():
    """
    To get the input of how many people are in the group
    @rtype: object
    @return: number_of_people
    """
    print("Hi there, for this simulation, we need to know how many people are in the room")

    while True:
        try:
            number_of_people = int(input("\nPlease enter the number of people in the room.\n"))
            break
        except ValueError:
            pass
        print("Incorrect input")
    return number_of_people


def factorial(value, number_of_people):
    """
    This function takes in the value to run the factorial on and the
    limit of the factorial
    @rtype: object
    @param value, number_of_people:
    @return: fact
    """
    fact = 1
    for i in range(1, number_of_people + 1):
        fact = value * fact
        value = value - 1
    return fact


def all_same_birthdays(number_of_people):
    """
    This function determines the probability that all people in the room share\
    the exact same birthday
    @rtype: object
    @param number_of_people:
    @return: prob
    """
    days_in_year = 365
    prob = ((1 / days_in_year) ** number_of_people)
    return prob


def one_birthday_as_you(number_of_people):
    """
    This function calculates the probability of how many people in the group
    share the same birthday as you, and only you
    @rtype: object
    @param number_of_people:
    @return: prob
    """
    days_in_year = 365
    prob = 1 - ((364 / days_in_year) ** number_of_people)
    return prob


def no_same_birthdays(number_of_people):
    """
    This function calculates the probability that no one shares the same
    birthday in the group
    @rtype: object
    @param number_of_people:
    @return: prob
    """
    days_in_year = 365
    prob = factorial(days_in_year, number_of_people) / \
           days_in_year ** number_of_people
    return prob


def two_same_birthdays(number_of_people):
    """
    This function calculates the probability that at least two people in the group
    share the same birthday, the original birthday paradox question.
    @rtype: object
    @param number_of_people:
    @return: prob
    """
    days_in_year = 365
    prob = (1 - factorial(days_in_year, number_of_people) / (days_in_year ** number_of_people))
    return prob


if __name__ == '__main__':
    num_people = number_of_people()
    all_same = all_same_birthdays(num_people)
    one_same_as_you = one_birthday_as_you(num_people)
    no_same = no_same_birthdays(num_people)
    two_same = two_same_birthdays(num_people)

    print("\nThe probability you all share the same birthday is {:.10%}".format(all_same))
    print("\nThe probability that none of you share the same birthday is {:.10%}".format(no_same))
    print("\nThe probability at least two of you in the group will share a same birthday is {:.10%}".format(two_same))
    print("\nThe probability that you as an individual share the same birthday with someone is {:.10%}".format(
        one_same_as_you))

