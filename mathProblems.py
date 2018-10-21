## 2018 - Sam Kenny

import random
import copy

## DOCSTRING: creates problems for A.

numberOfProblems = 25
difficultyLevel = 1 # number of digits involved in the problems

# Addition problems
add = []
for i in range(numberOfProblems):
    add1 = random.randint(0, 10**difficultyLevel - 1)
    add2 = random.randint(0, 10**difficultyLevel - 1)
    key = add1 + add2
    add.append([add1,add2,key])

# Subtraction problems
sub = []
for i in range(numberOfProblems):
    sub1 = random.randint(0, 10**difficultyLevel - 1)
    sub2 = random.randint(0, 10**difficultyLevel - 1)
    key = sub1 - sub2
    if key < 0:
        sub.append([sub2,sub1,-key])
    else:
        sub.append([sub1,sub2,key])

# Multiplication problems
mult = []
for i in range(numberOfProblems):
    mult1 = random.randint(0, 10**difficultyLevel - 1)
    mult2 = random.randint(0, 10**difficultyLevel - 1)
    key = mult1 * mult2
    mult.append([mult1,mult2,key])

# Division problems
div = []
for i in range(numberOfProblems):
    div1 = random.randint(0, 10**difficultyLevel - 1)
    div2 = random.randint(0, 10**difficultyLevel - 1)
    if div2 == 0:
        div2 += 1
    key = div1 // div2
    keyRemainder = div1 % div2
    div.append([div1,div2,key,keyRemainder])

# Populate template
with open('mathProblemsTemplate.tex','r') as f:
    templateText = f.readlines()

keyText = copy.copy(templateText)

k = 1
m = 1
for i, line in enumerate(copy.copy(templateText)):
    # Update addition problems
    if line == '\\section{Addition}\n':
        print(i)
        # Update assignment with problems
        templateText.insert(i+k,'\\begin{question}\n')
        k += 1
        templateText.insert(i+k,'\\begin{tasks}(4)\n')
        k += 1
        for j in add:
            templateText.insert(i+k,'\\task $' + str(j[0]) + '+' + str(j[1]) + '$\n')
            k += 1
            
        templateText.insert(i+k,'\\end{tasks}\n')
        k += 1
        templateText.insert(i+k,'\\end{question}\n')
        k += 1

        # Update key
        keyText.insert(i+m,'\\begin{question}\n')
        m += 1
        keyText.insert(i+m,'\\begin{tasks}(4)\n')
        m += 1
        for j in add:
            keyText.insert(i+m,'\\task $' + str(j[0]) + '+' + str(j[1]) + ' = ' + str(j[2]) + '$\n')
            m += 1
            break
        keyText.insert(i+m,'\\end{tasks}\n')
        m += 1
        keyText.insert(i+m,'\\end{question}\n')
        m += 1
    elif line == '\\section{Subtraction}\n':
        # Update subtraction problems
        subIndex = i
        templateText.insert(i+k,'\\begin{question}\n')
        k += 1
        templateText.insert(i+k,'\\begin{tasks}(4)\n')
        k += 1
        for j in sub:
            templateText.insert(i+k,'\\task $' + str(j[0]) + '-' + str(j[1]) + '$\n')
            k += 1
        templateText.insert(i+k,'\\end{tasks}\n')
        k += 1
        templateText.insert(i+k,'\\end{question}\n')
        k += 1
        
        keyText.insert(i+m,'\\begin{question}\n')
        m += 1
        keyText.insert(i+m,'\\begin{tasks}(4)\n')
        m += 1
        for j in sub:
            keyText.insert(i+m,'\\task $' + str(j[0]) + '-' + str(j[1]) + ' = ' + str(j[2]) + '$\n')
            m += 1
        keyText.insert(i+m,'\\end{tasks}\n')
        m += 1
        keyText.insert(i+m,'\\end{question}\n')
        m += 1
    elif line == '\\section{Multiplication}\n':
        # Update multiplication problems
        multIndex = i
        templateText.insert(i+k,'\\begin{question}\n')
        k += 1
        templateText.insert(i+k,'\\begin{tasks}(4)\n')
        k += 1
        for j in mult:
            templateText.insert(i+k,'\\task $' + str(j[0]) + ' \\times ' + str(j[1]) + '$\n')
            k += 1
        templateText.insert(i+k,'\\end{tasks}\n')
        k += 1
        templateText.insert(i+k,'\\end{question}\n')
        k += 1
        
        keyText.insert(i+m,'\\begin{question}\n')
        m += 1
        keyText.insert(i+m,'\\begin{tasks}(4)\n')
        m += 1
        for j in mult:
            keyText.insert(i+m,'\\task $' + str(j[0]) + ' \\times ' + str(j[1])+ ' = ' + str(j[2]) + '$\n')
            m += 1
        keyText.insert(i+m,'\\end{tasks}\n')
        m += 1
        keyText.insert(i+m,'\\end{question}\n')
        m += 1        
    elif line == '\\section{Division}\n':
        # update division problems
        divIndex = i
        templateText.insert(i+k,'\\begin{question}\n')
        k += 1
        templateText.insert(i+k,'\\begin{tasks}(4)\n')
        k += 1
        for j in div:
            templateText.insert(i+k,'\\task $' + str(j[0]) + ' \\div ' + str(j[1]) + '$\n')
            k += 1
        templateText.insert(i+k,'\\end{tasks}\n')
        k += 1
        templateText.insert(i+k,'\\end{question}\n')
        k += 1

        keyText.insert(i+m,'\\begin{question}\n')
        m += 1
        keyText.insert(i+m,'\\begin{tasks}(4)\n')
        m += 1
        for j in div:
            keyText.insert(i+m,'\\task $' + str(j[0]) + ' \\div ' + str(j[1])+ ' = ' + str(j[2]) + 'R' + str(j[3]) + '$\n')
            m += 1
        keyText.insert(i+m,'\\end{tasks}\n')
        m += 1
        keyText.insert(i+m,'\\end{question}\n')
        m += 1

with open("newmathProblems.tex",'w') as f:
    f.writelines(templateText)

with open("newmathProblemsKey.tex",'w') as f:
    f.writelines(keyText)
