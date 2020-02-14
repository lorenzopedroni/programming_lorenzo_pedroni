'''Author: Lorenzo Pedroni
Date: 14/02/2020'''

import input_data

BLOSUM52= input_data.BLOSUM52

seq1= input_data.seq1
seq2= input_data.seq2

def matrices (s1, s2, s_scheme, gap):
    M= len(s1) +1
    N= len(s2) +1 #we add one dimensione more to initialize the matrix

    s_matrix=[[0]*N for x in range(M)] #scoring matrix filled with zeros
    t_matrix=[[0]*N for x in range(M)] #traceback matrix filled with zeros

    #the s1 defines the rows, the s2 the columns
    #we now fill first row and first column with gaps

    for i in range(len(s_matrix[0])): #first row
        s_matrix[0][i]= i*gap
    for i in range(len(s_matrix)): #first column
        s_matrix[i][0]= i*gap

    #now we can start the iteration process to fill both the matrices

    for i in range(1, M):
        for j in range(1, N):
            sL= s_matrix[i][j-1] + gap #left
            sU= s_matrix[i-1][j] + gap #up
            sD= s_matrix[i-1][j-1] + s_scheme[s1[i-1] + s2[j-1]] #diagonal
            p= max(sL, sU, sD)
            s_matrix[i][j]= p #we fill the matrix with the max of the 3 scores

            #meanwhile we fill the traceback matrix too

            if p==sL:
                t_matrix[i][j]= "l"
            elif p==sU:
                t_matrix[i][j]= "u"
            else:
                t_matrix[i][j]= "d"
    
    return[s_matrix, t_matrix]

a= matrices(seq1, seq2, BLOSUM52, -2)

scoring_matrix= a[0]
traceback_matrix= a[1]

def traceback(M, s1, s2, score):
    al1="" #we define two strings to save the sequences while retrieving the alignment
    al2=""
    i= len(s1) #we start from the bottom right corner
    j= len(s2)

    while i!=0 or j!=0: #we want to reach the top left corner (0,0) and exit the loop
        if M[i][j]== "l":
            al1 += "-"
            al2 += s2[j-1]
            j-=1
        elif M[i][j]== "u":
            al1+=s1[i-1]
            al2+="-"
            i-=1
        elif M[i][j]=="d":
            al1+= s1[i-1]
            al2+= s2[j-1]
            i-=1
            j-=1
    al1= al1[::-1]
    al2= al2[::-1]
    print(al1)
    print(al2)
    print("The score is: ", score)

#Now we can apply the function to our data

traceback(traceback_matrix, seq1, seq2, scoring_matrix[-1][-1])
