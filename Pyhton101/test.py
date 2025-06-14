'''students = [ 
("Alice", 85), 
("Bob", 72), 
("Charlie", 95), 
("Diana", 60), 
("Ethan", 45) 
] 

# TODO: Loop through each student and assign a grade 
# Use if-elif-else statements based on the grading scale 
# Example output: 
# Alice scored 85 and got a grade of B 

for name, score in students: 
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else: 
        grade = "F"
    print(f"{name} scored {score} and got a grade of {grade}")
    
n = "Mira"
age = 16
favorite_subject = "Math"

print(f"{n} is {age} years old and her favorite subject is {favorite_subject}") '''

#for i in reversed(range(10,21)):
#    print(str(i) + "," , end=" ")

'''row = 6
colume = 6
for i in range(row):
    print("*" * colume)'''
    
    
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, end=" ")
    print()