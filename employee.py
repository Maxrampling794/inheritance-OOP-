class employee:
    def __init__(self, name, job_title, year_of_exp, salary):
        self.name = name
        self.job_title = job_title
        self.year_of_exp = year_of_exp
        self.salary = salary
    
    def new_job_title(self, job_title):
        print ("your current job title is: ", job_title)
        job_title = input("enter your new job title: ")
    
    def new_salary(self, salary):
        print ("your current yearly salary is: ", salary)
        salary = salary * 1.2
        print ("your new yearly salary is: ", salary)

    def new_year_of_exp(self, year_of_exp):
        year_of_exp = year_of_exp + 1
        print ("you now have ", year_of_exp, "years of experience")
    
    def calc_hourly_rate(self, salary):
        salary = salary / 8760 
        print ("your hourly rate is ", salary)

class employer(employee):
    def __init__(self, name, job_title, year_of_exp, salary, bonus):
        super().__init__(self, name, job_title, year_of_exp, salary)
        self.bonus = bonus

    

        

        
