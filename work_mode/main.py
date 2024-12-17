import calendar
import os
from openpyxl.styles import NamedStyle, Font, Alignment, PatternFill, Border, \
    Side
from xlsxwriter import Workbook

employees = [
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


# Получаем текущий год и месяц
year = 2024


# Получаем календарь для заданного месяца
def count_weekend_days(year, month):
    cal = calendar.monthcalendar(year, month)
    count = 0
    for week in cal:
        for day in week:
            if day != 0 and calendar.weekday(year, month, day) >= 5:
                count += 1
    return count

def work_rotation( employees:list):
    # weekend_days: list,
    weekend_team = []

    developers = [employee for employee in employees if
                  employee['role'] == "developer"]
    consultants = [employee for employee in employees if
                   employee['role'] == "consultant"]
    for month in range(12):

        weekend_days = count_weekend_days(year, month + 1)


        con = sorted(consultants, key=lambda x: x['priority'])

        for i in range(weekend_days):
            dev = min(developers, key=lambda x: x['priority'])
            ind = developers.index(dev)

            if (i + 2) ==len(con):
                print(con[-2]['name'],con[-2]['priority'])
                print(con[-1]['name'],con[-1]['priority'])
                print(f"{dev['name']=}")
                con[-2]['priority'] += 1
                con[-1]['priority'] += 1
                dev['priority'] += 1

            elif len(con[i % len(con): (i + 2) % len(con)]) > 1:
                for j in con[i % len(con): (i + 2) % len(con)]:
                    print(j['name'], j['priority'])
                    j['priority'] += 1
                print(f"{dev['name']=}")
                dev['priority'] += 1
            elif (i + 1)  == len(con):
                print(con[-1]['name'],con[-1]['priority'])
                print(con[0]['name'],con[0]['priority'])
                print(f"{dev['name']=}")
                con[-1]['priority'] += 1
                con[0]['priority'] += 1
                dev['priority'] += 1
            elif len(con[i % len(con): (i + 2) % len(con)]) == 0:
                for j in con[(i + 2) % len(con): (i - 1) % len(con)]:
                    print(j['name'], j['priority'])
                    j['priority'] += 1
                print(f"{dev['name']=}")
                dev['priority'] += 1

            developers[ind]['priority'] = dev['priority']
            print('-' * 5)


        weekend_team.extend(con)
        weekend_team.append(dev)

        consultants = sorted(con, key=lambda x: x['priority'])

        print('end month')
        print('-' * 5)

if __name__ == '__main__':
    work_rotation(employees=employees)