#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

# What i did understand from the question is :

# Every students receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade

# Sam, a professor at the university and likes to round each student's grade according to these rules:
# if the diff between the grade and the next multiple of 5 is less than 3. round the grade up to next multiple of 5
# if the value is grade is less than 38, no rounding occurs ad the result will still be a failing grade

# Examples:
# grade = 84 round to 85 (85 - 84 is less than 3)
# grade = 29  do not round (result is less than 38)
# grade = 57  do not round (60 - 57 is 3 or higher)


def gradingStudents(grades):
    # my code answer
    # I created a result list 
    res = []
    #
    for grade in grades:
        # if the grade is more or equal to 38
        if grade>=38:
            # modulus of 5
            mod5 = grade % 5
            
            # if modulus of 5 is more or equal to 3 
            if mod5>=3:
                # this part i really dont understand
                grade+= (5 - mod5)
        # add to the result
        res.append(grade)
    # return to the result
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()




            