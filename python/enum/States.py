# from enum import Enum

# States = ['SUCCESS', 'PENDING', 'MALFORMED', 'FAILURE']

# print(States)
# print('SUCCESS' in States)

# table_headers = ["ID", "RUN_DATE", "STATUS"]


import datetime

expected_tables = [[], [['ID', 'Date_to_run', 'Status'],
                        ['1', '03/08/1901', ''],
                        ['2', '03/08/2020', ''],
                        ['3', '03/08/2021', '']]]
table_header = ['ID', 'Date_to_run', 'Status']
#print([['ID', 'Date_to_run', 'Status']] in expected_table)


for table in expected_tables:
    # look for the table header
    if ((len(table) < 1) or (table[0] != table_header)):
        continue
    index = 0
    for row in table:
        print(f"{index}: " + str(row))
        index += 1

expected_dicts = [[], [{'ID': '1',
                        'Date_to_run': '03/08/1901',
                        'Status': ''},
                       {'ID': '2',
                        'Date_to_run': '03/08/2020',
                        'Status': ''},
                       {'ID': '3',
                        'Date_to_run': '03/08/2021',
                        'Status': ''}]]

for table in expected_dicts:
    index = 0
    for row in table:
        print(f"{index}: {row}")
        index += 1


def is_valid_future_date(date_str, date_now) -> str:
    """
    >>> is_valid_future_date(date_str="bad", date_now="02/02/2020")
    'MALFORMED: bad'

    >>> is_valid_future_date(date_str="2/2/2", date_now="02/02/2020")
    'MALFORMED: 2/2/2'

    >>> is_valid_future_date(date_str="02/02/2020", date_now="02/02/2020")
    ''

    >>> is_valid_future_date(date_str="02/22/2020", date_now="02/02/2020")
    'MALFORMED: Date is in the future 02/22/2020'
    """
    result = ""
    try:
        run_date = datetime.datetime.strptime(date_str, '%m/%d/%Y').date()
        now_date = datetime.datetime.strptime(date_now, '%m/%d/%Y').date()
        if (run_date > now_date):
            result = f"MALFORMED: Date is in the future {date_str}"

    except ValueError:
        result = f"MALFORMED: {date_str}"
    return result
