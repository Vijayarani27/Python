# Dictionary Comprehension
list = [1,2,3]
dictionary = {key:key**2 for key in list }
print(dictionary)
listcomp =[key for key in dictionary.values()]
print(listcomp)


#Set comprehension ========================

print("\n")
list =[1, 2, 5, 2, 3, 1, 4, 5]
setcomp= {value**2 for value in set(list)}
print(setcomp)      


#Question 3 ============================
print("\n")
listOftuple = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

"""Dictionary with name and balance """
dictionary = {tuples[0]:tuples[1] for tuples in listOftuple if tuples[1]>=tuples[2] }
print(dictionary)

"""Set of all balances """
sets = {tuples[1] for tuples in listOftuple}
print(sets)

""" list of account holders """
lists = [tuples[0] for tuples in listOftuple]
print(lists)

""" dict of user and money each need to fulfill the min balance requirement  """
amount = {tuples[0]:tuples[2]-tuples[1] for tuples in listOftuple if tuples[1]<tuples[2]}
print(amount)

""" list of tuples with name and current balance if the balance is above 0 """
listOftuples = [(tuples[0],tuples[1]) for tuples in listOftuple if tuples[2]>0]
print(listOftuples) 


# Yesterday Bonus challenges =============================
print("\n")
dictionary = {"Maths":"Algebra","Car":"Ford","Fruit":"Apple"}
list =[key for key in dictionary if len(key)>4]
print(list)
