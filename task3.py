class Person:
    peopleCount = 0

    def __init__(self, name, bestDist):
        self.name = name
        self.bestDist = bestDist
        Person.peopleCount += 1

    def __del__(self):
        Person.peopleCount -= 1

contestants = []
print('Введите данные в формате {ИМЯ,РЕЗ1,РЕЗ2,РЕЗ3}, "q"/пустая строка для выхода')
while True:
    n = input()
    if n == "q" or n == "":
        break
    n = n.split(",")
    maxDist = float(n[1])
    for i in n[1:]:
        if float(i) > maxDist:
            maxDist = float(i)
    contestants.append(Person(n[0],maxDist))

for contestant in contestants: 
    print(contestant.name,contestant.bestDist)