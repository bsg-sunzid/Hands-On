# It produces a sequence of values when iterated over. More useful when we want to produce a large sequences of values
# here we donot use return, use the yield statement which is used to produce a value from the generator

def generator(n):
    value = 0
    while value < n:
        yield value

        value +=1

for value in generator(4):
    print(value)



