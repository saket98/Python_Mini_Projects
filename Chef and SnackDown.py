"""
Chef is interested in the history of SnackDown contests. He needs a program to verify if SnackDown was hosted in a given year.

SnackDown was hosted by CodeChef in the following years: 2010, 2015, 2016, 2017 and 2019

* Example Input *
2
2019
2018

* Example Output *
HOSTED
NOT HOSTED

"""

test_case = int(input())
for i in range(test_case):
    year = input()

    if year == '2010' or year == '2015' or year == '2016' or year == '2017' or year == '2019':
        print("HOSTED")

    else:
        print("NOT HOSTED")
