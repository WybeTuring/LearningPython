# My first experience with object oriented programming in python
class worker:
    """docstring for ."""
    def __init__(self, name, pay): # Initialises the class, by first of all creating a new object called self
        self.name = name; #self in this case acts like a place holder for the other variables, a safe enough aprch
        self.pay = pay;
    def lastName(self):
        return self.name.split(" ")[-1];
    def giveRise(self, percent):
        return self.pay + self.pay*(percent/100);
workers = [];
# Creating a table of 10 workers in a loop
for i in range(10):
    identity = []
    identity.append("Worker" + str(i));
    identity.append(str(100*i));
    workers.append(identity);
for k in workers:
    print("The {0} worker earns {1}".format(k[0], k[1]))
print("{0.2f} dogs came along mate".format(16536.7899))
