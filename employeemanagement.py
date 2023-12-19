employee=[]

def addemployee():
    name=input("enter your name")
    age=int(input("enter your age"))
    job=input("enter your job position")
    
    emp={
        'name':name,
        'age':age,
        'job':job
    }
    employee.append(emp)
    print(f"employee {name} added successfully")
    
    
    
def displayemp():
    print("---the employee details are-----")
    for i in employee:
         
          print(f"name: {i['name']}, age :{i['age']} job :{i['job']}")
          

def searchemp():
    search_name=input("enter the user name")
    
    for i in employee:
        
        if i['name'].lower() == search_name.lower():
            print("details fetched successfully")
            print(f"name: {i['name']}, age :{i['age']} job :{i['job']}")
        else:
            print("not found") 
            
def delemp():
    
    search_del=input("enter ur name to delete")
    
    for i in employee:
        
        if i['name'].lower() == search_del.lower():
            
            employee.remove(i)
            
        else:
            
            print("not found")


while True:
    print("enter 1 to add employee details ")
    print("enter 2 to Display employee details ")
    print("enter 3 to Search employee  ")
    print("enter 4 to delete employee details ")
    print("enter 5 to exit ")

    value=input("enter the key here :")
    
    if value=='1':
        addemployee()
    elif value=='2':
        displayemp()
    elif value=='3':
        searchemp()
    elif value=='4':
        delemp()
    elif value=='5':
        print("have a nice day")
        break
    else:
        print("you have enterd wrong input pls try again")