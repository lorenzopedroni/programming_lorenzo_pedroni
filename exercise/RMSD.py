File1=open("./model1.pdb","r")

L1=[]
for line in File1:
    line=line.rstrip()
    if "CA" in line:
        L=line.split()
        L1.append((L[6:9]))
File1.close()

File2=open("./model2.pdb", "r")
L2=[]
for line in File2:
    line=line.rstrip()
    if "CA" in line:
        L=line.split()
        L2.append((L[5:8]))
File2.close()

def converter(Lista):
    L=[]
    for i in Lista:
        a=float(i[0])
        b=float(i[1])
        c=float(i[2])
        L.append((a,b,c))
    return(L)
L1=(converter(L1))
L2=(converter(L2))

def RMSD(list1, list2):
    Di=0
    for i in range(len(list1)):
        d=((list1[i][0]-list2[i][0])**2 + (list1[i][1]-list2[i][1])**2 + (list1[i][2]-list2[i][2])**2)
        Di+=d
    return((Di/len(list1))**(1/2))
print(RMSD(L1, L2))
