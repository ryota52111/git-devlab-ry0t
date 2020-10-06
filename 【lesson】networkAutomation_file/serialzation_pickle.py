import pickle
friends1 = {"Dan": [20, "London", 3234342], "Maria":[25 ,"Madrid", 43525222]}
friends2 = {"Andrei": [20, "London", 3234342], "Nina":[25 ,"Madrid", 43525222]}
friends = (friends1, friends2)

with open("friends.dat", "wb") as f:
    pickle.dump(friends, f)


with open("friends.dat","rb") as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)