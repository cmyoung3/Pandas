import pandas as pd

grades_dict = {'Wally': [87, 96, 70],
                'Eva': [100, 87, 90],
                'Sam': [94, 77, 90],
                'Katie': [100, 81, 82],
                'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']

#.T inverts the rows and columns 'T' stands for transpose
print(grades)

#print(grades['Eva'])

#print(grades.Sam)

#using the loc and iloc methodds

print(grades.loc['Test2'])

print(grades.iloc[1])
#should give the same result

#when using loc method, the upper bound is included
print(grades.loc['Test1':'Test3'])

#when using the iloc method, the upper bound is NOT included
#print(grades.iloc[0:3])

#For non-consectuive rows
#print(grades.loc[['Test1','Test3']])
#print(grades.iloc[[0,2]])
#because its easier to keep things straight, most people use loc

#View only Eva's and Katie's grades for Test1 and Test2

print(grades.loc[['Test1', 'Test2'],['Eva', 'Katie']])
print(grades.loc[:'Test2',['Eva', 'Katie']])

#View only Sam's Thru Bob's grades for test1 and test3
print(grades.loc[['Test1', 'Test3'], 'Sam':'Bob'])

grades_A = grades[grades>=90]
print(grades_A)

# create a dataframe for everyone with a B grade
#use & for and in bitwise
grades_B = [(grades>=80) & (grades < 90)]

# dataframe for everyone with A or B
#use '|' for or in bitwise
grades_A_or_B = [(grades>= 90) | (grades>= 80)]

print(grades_A_or_B)

pd.set_option('precision', 2)

print(grades.describe())

print(grades.sort_index(ascending=False))

print(grades.sort_index(axis=1))
#sorts column indexs alaphabetically if you wanted it to be reverse alphabetical, simply add ',ascending=False'

print(grades.sort_values(by='Test1', axis=1, ascending=False))

print(grades.T.sort_values(by='Test1', ascending=False))

print(grades.loc['Test1'].sort_values(ascending=False))

