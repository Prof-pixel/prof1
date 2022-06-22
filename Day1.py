num1 = 17
print(num1)
num2 = 65.4
print(num2)
firstname = 'Austine'
print(firstname)
secondname = 'Onovo'
print(secondname)
X = True
print(X)
word = 'we\'re brothers from the other side of the town'
# Backward slash denotes the escape character
print(word)
word2 = ' variable name cannot start with a number\nvariable cannot have a space\nvariable naming cannot have any special character'
print(word2)
print('\n')
word3 = """variable name cannot start with a number
variable cannot have a space
variable naming cannot have any special character
"""
print(word3)

#string concatenation
print('Hello' + ' ' + 'World') # joining of string and string
print('Hello', firstname)
print(firstname,secondname)
#string formatting
score1 = 75
score2 = 90
score3 = 85

# declaring a variable
report = 'Prince pass mark in math is {}, {} in english and {} in physics'
print(report.format(score1,score2,score3))
print('\n')
print(f'Prince pass mark in math is {score1}, {score2} in english and {score3} in physics')
word1 = 'school'
word2 = 'SCHOOL'
word3 = 'python is fun'
word4 = '   infor@gmail.com'

print(word1.upper())
print(word2.lower())
print(word3.title())
print(word3.capitalize())
print(word3.split())
print(word4.strip())
      
