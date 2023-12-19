
empdetails=[]


def addetails():
    empid=int(input("enter details id"))
    name=input("enter the name")
    age=int(input("enter the age"))
    job=input("enter the job")
    info={"ID":empid,"Name":name,"age":age,"job":job}
    
    
    # empdetails[empid]=info
    empdetails.append(info)
    print(f"employee id {empid} added ")

def printd():
     for emp_info in empdetails:
        print(f"Employee ID: {emp_info['ID']}, Name: {emp_info['Name']}, job: {emp_info['job']}")

def searchid():
    searchid=int(input("enter emp id to serch"))
    for i in empdetails:
        if i["ID"] == searchid:
          print(f"Employee ID: {i['ID']}, Name: {i['Name']}, job: {i['job']}")

    









while True:
    print("----options----")
    print("enter 1 for add etails")
    print("enter 2 for print etails")
    print("enter 3 for search etails")
    print("enter 4 delete  etails")
    
    userinput=input("enter here")
    
    if userinput=="1":
        addetails()
    elif userinput=="2":
        printd()
    elif userinput=="3":
        searchid()
    # elif userinput=="4":
    #     delete()
    else:
        print("invalid details pls try again")