import pickle,Employee
n=int(input("Enter number of employee: "))
f=open('emp.dat','wb')
for emp in range(n):
    eno=int(input("Enter Employee Number: "))
    ename=(input("Enter Employee Name: "))
    esal=float(input("Enter Employee Salary: "))
    eaddr=(input("Enter Employee Address: "))
    emp=Employee.Employee(eno,ename,esal,eaddr)
    pickle.dump(emp,f)
print("pickling of a object is completed")
f.close()