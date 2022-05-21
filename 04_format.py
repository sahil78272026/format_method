# format method were used before python 3.6 , in 3.6 f string got introduced
name = "Sahil"
place = "Ghaziabad"
work = "Gurgaon"

# same as s2 = f"My name is {name} and i live in {place}"
s2 = "My name is {} and i live in {}".format(name,place) # arguments will pass in a sequencial way if endex not given
s3 = "My name is {1} and i live in {0} and i work in {2}".format(name,place,work) # we can give index and interchange the arguments placement


print(s2)
print(s3)