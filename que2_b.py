

def max_salary_employee(lst):
    max = 0
    res = {}
    for item in lst:
        if(item["salary"] > max):
            max = item["salary"]
            res = item
    return res