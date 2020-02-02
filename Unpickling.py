import pickle,Employee
with open('emp.dat','rb') as f:
    while True:
        try:
            obj=pickle.load(f)
            obj.Display()
        except EOFError:
            print('Unpickling of object is completed')
            break