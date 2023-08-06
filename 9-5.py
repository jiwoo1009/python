import turtle as t
import random


name=["민용이가","재용이가","천송이가"]
noun=["사자를","자전거를","비행기를"]
verb=["산다","탄다","찬다"]
for a in range(10):
    name1=random.choice(name)
    noun1=random.choice(name)
    verb1=random.choice(verb)
    print(name1,noun1,verb1)
