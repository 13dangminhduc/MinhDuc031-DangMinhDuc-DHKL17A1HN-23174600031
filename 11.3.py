#list of animals
animals=['ant','bear','cat','dog','elephant','fish','goat','hippo']
print('list of animals',animals)
print("number of animals:",len(animals))
# tim kiem
kqtk=int(input("i want to find:\n"))
if kqtk in animals:
    print("there is ",kqtk,"in list of animals")
    print('there is not',kqtk,'in list of animals')