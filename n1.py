employee_data = {
    'employee1': {
        'name': 'Alice',
        'age': 28,
        'position': 'Software Engineer'
    },
    'employee2': {
        'name': 'Bob',
        'age': 35,
        'position': 'Data Scientist'
    },
    'employee3': {
        'name': 'Charlie',
        'age': 42,
        'position': 'Product Manager'
    }
}

name=input("enter ur namr")
age=int(input("enter ur age"))
position=input("enter ur postion")

newdata={
    'name':name,
    'age':age,
    'position':position
}
employee_data['employee4']=newdata
print(employee_data)







