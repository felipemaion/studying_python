people = [1,2,3,4,5,6,7]
task = ["A", "B"]


for _ in range(10):
    person_a = people.pop(0)
    people_b = [people.pop(0),people.pop(0)]
    current_task = {task[0]:person_a, task[1]:people_b}
    people.append(person_a)
    for person in people_b:
        people.append(person)
    print(current_task)
