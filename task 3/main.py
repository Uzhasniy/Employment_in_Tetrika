#Сколько секунд ученик на занятии
def pupil_mass_add(i):
    pupil_mass = []
    n = 0
    while n < (len(tests[i]['data']['pupil'])):
        pupil_mass_start = tests[i]['data']['pupil'][n]
        while pupil_mass_start < tests[i]['data']['pupil'][n+1]:
            pupil_mass_start+=1

            #Ограничение длительностью занятия 
            if pupil_mass_start > tests[i]['data']['lesson'][0] and pupil_mass_start <= tests[i]['data']['lesson'][1]:
                pupil_mass.append(pupil_mass_start)
        n+=2
    return pupil_mass

#Сколько секунд преподаватель на занятии
def tutor_mass_add(i):
    tutor_mass = []
    n = 0
    while n < (len(tests[i]['data']['tutor'])):
        tutor_mass_start = tests[i]['data']['tutor'][n]
        while tutor_mass_start < tests[i]['data']['tutor'][n+1]:
            tutor_mass_start+=1

            #Ограничение длительностью занятия 
            if tutor_mass_start > tests[i]['data']['lesson'][0] and tutor_mass_start <= tests[i]['data']['lesson'][1]:
                tutor_mass.append(tutor_mass_start)
        n+=2
    return tutor_mass

def appearance(intervals,i):
    pupil_mass = pupil_mass_add(i)
    tutor_mass = tutor_mass_add(i)
    amount_pupil_tutor = []

    #Сравнение элементов
    for pupil in pupil_mass:
        for tutor in tutor_mass:
            if pupil == tutor:
                amount_pupil_tutor.append(pupil)

    #Проверка на уникальность элементов
    for amount in amount_pupil_tutor:
            if amount_pupil_tutor.count(amount) > 1:
                amount_pupil_tutor.remove(amount)


    print(len(amount_pupil_tutor))

    test_answer_data = len(amount_pupil_tutor)
    return test_answer_data
        

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'], i)
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
