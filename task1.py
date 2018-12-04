from data import dataset

#   Написати функцію, що зберігає інформацію про улюблену страву користувача у певній країні
#   Викликати функцію


def addStudentSkill(student, company, skill):
    if student in dataset:

        if company in dataset[student]:
            print_list=dataset[student][company]
            print_list.add(skill)
        else:
            dataset[student][company]={skill}
    else:
        dataset[student]={company: {skill}}



print("Task 1")

#Додати нового студента та вміння у новій компанії
addStudentSkill("KB-13131313","bankaval","bepatient")

#Додати існуючому студенту нове вміння у новій компанії
addStudentSkill("KB-12121212","atb","smileeverytime")

#Додати існуючому студенту нове вміння в існуючій компанії
addStudentSkill("KB-12121212","privat24","be_patient")

print(dataset)

print("\n\n")
