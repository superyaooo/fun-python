sunday = [12,13,14]
monday = [22,23,24]
for item in zip(sunday,monday):
    print(item)
# returns:
# (12,22)
# (13,23)
# (14, 24)

a = [1,2,3]
b = ['one','two','three']
c = ['ONE','TWO','THREE','FOUR','FIVE']
for item in zip(a,b,c):
    print(item)
# returns:
# (1,'one','ONE')
# (2,'two','TWO')
# (3,'three','THREE')