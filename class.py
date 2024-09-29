class Myclass: 
    a,b,c = 1,2,3 

Myclass.a 

print(Myclass.a)
mc1 = Myclass()

mc1.a = "ahoj" ## todle už je potomek 

print(mc1.a)

Myclass.a = "svete"

mc2 = Myclass()
print(mc2.a) 