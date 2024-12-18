import pandas as pd

EMPLOYEES = [
    {'id': 8960,
     'name': "Alice",
     'role': "developer",
     'priority': 0,
     },
    {'id': 3436,
     'name': "David",
     'role': "developer",
     'priority': 0,
     },
    {'id': 3689,
     'name': "Serge",
     'role': "developer",
     'priority': 0,
     },
    {'id': 8548,
     'name': "Kiril",
     'role': "developer",
     'priority': 0,
     },
    {'id': 3789,
     'name': "Vlad",
     'role': "developer",
     'priority': 0,
     },
    {'id': 9678,
     'name': "Alex",
     'role': "developer",
     'priority': 0,
     },

    {'id': 1111,
     'name': "Bob",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 2222,
     'name': "Charlie",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 3333,
     'name': "Eve",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 4444,
     'name': "Astolfo",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 5555,
     'name': "Bee",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 7777,
     'name': "Tobi",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 8888,
     'name': "Arthur",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 9999,
     'name': "Coco",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 1010,
     'name': "Ryuu",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 1212,
     'name': "Osamu",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 1313,
     'name': "Noburu",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 1414,
     'name': "Hikaru",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 1515,
     'name': "Tanjiro",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 1616,
     'name': "Spike",
     'role': "consultant",
     'priority': 0,
     },
    {'id': 1717,
     'name': "Kazuha",
     'role': "consultant",
     'priority': 0,
     },
]

MONTH_NAME = [
    'январь', 'февраль', 'март',
    'апрель', 'май', 'июнь',
    'июль', 'август', 'сентябрь',
    'октябрь', 'ноябрь', 'декабрь',
]


def work_rotation(employees: list):
    weekend_team = []

    developers = [employee for employee in employees if
                  employee['role'] == "developer"]
    consultants = [employee for employee in employees if
                   employee['role'] == "consultant"]

    data = pd.read_excel(
        'C:/Users/LapinVMi/PycharmProjects/hakaton/hakaton/work_mode/excel_files/prazdnik.xlsx')

    df = pd.DataFrame(data)

    for i in range(12):
        for j in range(len(df[i + 1])):
            if str(df[i + 1][j]).strip() == 'NaT':
                df[i + 1].pop(j)

    for month in range(12):

        weekend_days = df[month + 1]
        count = len(weekend_days)

        print(MONTH_NAME[month])

        con = sorted(consultants, key=lambda x: x['priority'])

        for i in range(count):
            dev = min(developers, key=lambda x: x['priority'])
            ind = developers.index(dev)

            work_days = []
            work_day = str(weekend_days[i])
            work_days.append(work_day)
            print(work_day)
            if (i + 2) == len(con):

                print(con[-2]['id'], con[-2]['name'], con[-2]['priority'])
                print(con[-1]['id'], con[-1]['name'], con[-1]['priority'])
                print(f"{dev['name']=}")
                work_days.extend(
                    [dev['name'], con[-2]['name'], con[-1]['name']])
                con[-2]['priority'] += 1
                con[-1]['priority'] += 1
                dev['priority'] += 1

            elif len(con[i % len(con): (i + 2) % len(con)]) > 1:
                work_days.extend([dev['name']])
                for j in con[i % len(con): (i + 2) % len(con)]:
                    print(j['id'], j['name'], j['priority'])
                    work_days.extend([j['name']])
                    j['priority'] += 1
                print(f"{dev['name']=}")
                dev['priority'] += 1

            elif (i + 1) == len(con):
                print(con[-1]['id'], con[-1]['name'], con[-1]['priority'])
                print(con[0]['id'], con[0]['name'], con[0]['priority'])
                print(f"{dev['name']=}")
                con[-1]['priority'] += 1
                con[0]['priority'] += 1
                dev['priority'] += 1
                work_days.extend(
                    [dev['name'], con[-1]['name'], con[0]['name']])

            elif len(con[i % len(con): (i + 2) % len(con)]) == 0:
                work_days.extend([dev['name']])
                for j in con[(i + 2) % len(con): (i - 1) % len(con)]:
                    print(j['id'], j['name'], j['priority'])
                    work_days.extend([j['name']])
                    j['priority'] += 1
                print(f"{dev['name']=}")
                dev['priority'] += 1

            developers[ind]['priority'] = dev['priority']
            print('-' * 5)

            # print(work_days)
            weekend_team.append(work_days)

        consultants = sorted(con, key=lambda x: x['priority'])

        print('end month')
        print('-' * 5)

    # print(weekend_team)
    pd.DataFrame(weekend_team).to_excel('excel_files/ex-4.xlsx', index=False)


if __name__ == '__main__':
    work_rotation(employees=EMPLOYEES)
