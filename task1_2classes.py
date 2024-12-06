class Person:

    def __init__(self, name, grades:list):
        self.name = name
        self.grades = grades

    def averageGrade(self):
        gradeSum = 0
        for grade in self.grades:
            gradeSum += float(grade)
        return gradeSum / len(self.grades)

class Group:

    def __init__(self, number, students:list):
        self.number = number
        self.students = students

    def addStudent(self,newStudent):
        self.students.append(newStudent)

    def groupAvg(self):
        grAvg = 0
        for st in self.students:
            grAvg += st.averageGrade()
        return grAvg / len(self.students)

groups = {

}

print("--> !!!Пустая строка для выхода!!! <--")
print("ГРУП,ИМЯ,ОЦ1,ОЦ2,...")
while True:

    n = input()
    if n == "":  # exit mainloop
        break
    n = n.split(",")
    doNotAdd_Flag = False
    try:
        tmp = n[2]
        for i in n[2:]:
            i = float(i)
    except:
        doNotAdd_Flag = True
        print("Not Added (Syntax error!)")

    if not doNotAdd_Flag:
        try:
            groups[n[0]].addStudent(Person(n[1],n[2:]))
            print("Added to existing group")
        except KeyError:
            groups[n[0]] = Group(n[0],[])
            groups[n[0]].addStudent(Person(n[1],n[2:]))
            print("Created new group and Added")


output = []
for group in groups:
    gr = groups[group]
    output.append([gr.number,gr.groupAvg(),len(gr.students)])

i = 0 ### Bubble Sort
while True:
    noSwap = True
    for j in range(0,len(output)-1):
        if output[j][1] < output[j+1][1]:
            output[j],output[j+1] = output[j+1],output[j]
            noSwap = False
    i += 1
    if noSwap:
        break

print("Group: Average; Number of students")
for entry in output:
    print(f"{entry[0]}: {entry[1]}; {entry[2]}")
