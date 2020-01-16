file1=open("./PAM250.txt","r")
l1=[]
for line in file1:
    line=line.rstrip()
    line=line.split()
    l1.append(line)
file1.close()

file2= open("./BLOSUM62.txt", "r")
l2=[]
for line in file2:
    line=line.rstrip()
    line=line.split()
    l2.append(line)
file2.close()

def mk_dictionary(l):
    score_dictionary={}
    for i in range(len(l[0])):
        for j in range(1, len(l)):
            score_dictionary[l[0][i]+ l[j][0]]= int(l[i+1][j])
    return(score_dictionary)

PAM250= mk_dictionary(l1)
BLOSUM62= mk_dictionary(l2)

def scoring(s1, s2, dictionary):
    score=0
    for i in range(len(s1)):
        if s1[i]!="-" and s2[i]!="-":
            score+=dictionary[s1[i]+s2[i]]
        else:
            score-=2
    print(s1)
    print(s2)
    return(score)

file3=open("./alignments.fasta", "r") #Make a list of sublists containing each one 
sequences=[]
for line in file3:
    line=line.rstrip()
    if not line.startswith(">"):
        sequences.append(line)
file3.close()

for i in range(0, len(sequences), 2): #Read sequences 2 by 2 (first with second, third with fourth...
    print("Using PAM250", scoring(sequences[i], sequences[i+1], PAM250))
    print("Using BLOSUM62", scoring(sequences[i], sequences[i+1], BLOSUM62))


