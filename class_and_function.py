class Developer:
  def __init__(emp, name, age):
    emp.name = name
    emp.age = age

  def func(emp):
        print("Fresher Developers in NF : " + emp.name)

p1 = Developer("Sandeep", 22)
p1.func()