
# Online Python - IDE, Editor, Compiler, Interpreter
n = int(input("Enter the initial number:"))
names = []
scores = []
for i in range(n):
    name = input("Enter the name of the student: ")
    score = int(input("Enter the score of the student: "))
    names.append(name)
    scores.append(scores)
 
print(scores)
records = [[i,j] for i in names for j in scores]
print (records)

b = [x for x in scores if x > min(scores)]
print (b)
c = min(b)
print(c)
        

    

d = [i for i,j in records if j == c]
print (d)
    
