'''Write a Python program to find the highest 3 values in a dictionary'''

d={'a':32,'b':45,'c':12,'d':89}

values=list(d.values())

values.sort(reverse=True)

print(values[:3])
