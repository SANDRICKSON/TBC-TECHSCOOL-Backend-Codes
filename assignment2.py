var1 = 57
var2 = "georgia"
var3 = 27
var4 = 26
var5 = 28
var6 = 25.0


if type(var1) == int:
    print(True)
else:
    print(False)

if type(var2) == str:
    if var2[0] == 'p':
        print(False)
    elif var2[0] == 'g':
        print(True)
    else:
        print(True)
elif type(var2) == int:
    print(False)
else:
    print(False)

if var3 > var4 and var4 < var5:
    print(True)
else:
    print(False)

if not type(var6) == float:
    print(False)
elif var6 / 5 == 5.0 or var6 / 2 == 10.0:
    print(True)
else:
    print(False)
