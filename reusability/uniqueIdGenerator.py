"""
Code to generate unique id based on time
Input = 2018-10-06 12:19:59.832369
Output= 20181006121959832369X

What is X in Output ?
In rare cases if there are more than one id required in milliseconds
then code should automatically append 1-99 in output

"""

import datetime
print(datetime.datetime.now())

#Code