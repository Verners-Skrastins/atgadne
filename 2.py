#datu izvade termināli
#1.veids f-string izmantošana (sākot ar python 3.6)
vards = "Anna"
vecums = 30
print(f"Mani sauc {vards} un man ir {vecums} gadi")
#2. veids - format
zinama_virkne = "Mani sauc {} un man ir {} gadi"
print(zinama_virkne.format(vards, vecums))
#3. veids %operatoru
zinama_virkne = "Mani sauc %s un man ir %d gadi" %(vards, vecums)
print(zinama_virkne)

