txt = "welcome to the      jungle"
string = ""
x = txt.split(" ")
while "" in x:
    x.remove("")
x = x[::-1]

for i,c in enumerate(x):
    if i == 0:
        string = string + c
    else:
        string = string + " " + c
		
print(string)