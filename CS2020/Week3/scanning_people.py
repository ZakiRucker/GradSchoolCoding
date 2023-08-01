#---------------------------------------------
# CS2020
#
# This illustrates how the scanning and filtering of
# a list of tuples are done.
# 
#
# Python 3.0
#
# Author: Thomas Otani
#
#---------------------------------------------

def averageAge(people):
    ageList = [age for (name, age, gender) in people]
    
    return sum(ageList) / len(ageList)


def averageAge2(people):
    ageList = map(lambda person: person[1], people)
 
    return sum(ageList) / len(people)
    
    
def averageAge3(people):
    totalAge = 0
    for (name, age, gender) in people:
        totalAge = totalAge + age
    
    return totalAge / len(people)


def femaleAvgAge(people):
    ageList = [age for (name, age, gender) in people if gender == "F"]
    
    return sum(ageList) / len(ageList)


def femaleAvgAge2(people):
    females = filter(lambda person: person[2] == "F", people)
    
    return averageAge(females)

def countAgeRange(people, minAge, maxAge):
    val = len([person for person in people if minAge <= person[1] and person[1] <= maxAge])
                            #Python uniquely allows the expression minAge <= person[1] <= maxAge
    return val

def countAgeRange2(people, minAge, maxAge):
    ageFilterList = list(filter(lambda person: minAge <= person[1] and person[1] <= maxAge, people))
                    #need to convert it to list so the len function an be applied
    return len(ageFilterList)

##---------- Sample Calls ----------------##
testPeopleList = [
                  ("john", 20, "M"), \
                  ("jack", 21, "M"), \
                  ("jill", 22, "F"), \
                  ("jane", 23, "F"), \
                  ("mick", 24, "M"), \
                  ("nick", 25, "M"), \
                  ("joey", 24, "M"), \
                  ("rick", 23, "M"), \
                  ("moen", 22, "F"), \
                  ("zoen", 21, "F"), \
                  ("roen", 20, "F"), \
                  ]

print(averageAge(testPeopleList))
print(averageAge2(testPeopleList))
print(averageAge3(testPeopleList))

print(femaleAvgAge(testPeopleList))
print(femaleAvgAge2(testPeopleList))

print(countAgeRange(testPeopleList, 22, 24))
print(countAgeRange2(testPeopleList, 22, 24))
    