import csv

def csv_(self, name, last_name, job_title, salary):
    self.name = name
    self.last_name = last_name
    self.job_title = job_title
    self.salary = salary
    with open('money.csv', 'a', newline='\n', encoding='UTF-8') as m:
        write_new = csv.writer(m)
        text = [self.name, self.last_name, self.job_title, self.salary]
        write_new.writerow(text)

def print_(employee_1, employee_2):
    print(employee_1.data_all())
    print(employee_2.data_all())
    employee_1.change_(change_name='Stas', change_last_name='Pikkuli', change_job_title='juni', change_salary=1300)
    print(employee_1.data_all())
    employee_1.sharges()
    employee_1.sharges_procent()
    employee_2.sharges()
    employee_2.sharges_procent()
    print(employee_1.comparison(employee_2.salary))

