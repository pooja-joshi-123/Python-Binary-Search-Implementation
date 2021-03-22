
#function to mergesort the list obtained by util.all_word_pairs()
def merge(data):
    #condition to check if the list is empty or only contains one element
    if len(data)<=1:
        res=data[:]
        return res
    else:
        #split the input list into two
        mid=len(data)//2 
        fst=merge(data[:mid])
        snd=merge(data[mid:])
        res=[]
        fi=si=0
        while fi<len(fst) and si<len(snd):
            if fst[fi]<snd[si]: #if an element from the first-half list is lesser, append it into the resultant list
                res.append(fst[fi])
                fi=fi+1
            else:
                res.append(snd[si]) #append the element of the second-half list into the resultant list
                si=si+1
        while fi<len(fst):
            res.append(fst[fi]) #append the rest of the elements of the first-half list
            fi=fi+1
        while si<len(snd):
            res.append(snd[si]) #append the rest of the elements of the second-half list
            si=si+1
    return res

#function to remove duplicate lists within the input list
def remove_dups(data):
    a=merge(data)
    res=[]
    if len(a)>1:
        fresh=a[0] #store first list into the variable fresh
        i=1
        #loop to compare the list in fresh with the other lists and generate resultant list without duplicates
        while i<len(a):
            if a[i]!=fresh:
                res.append(fresh)
                fresh=a[i]
            i=i+1
        res.append(fresh)
    return res

#function to return the search table
def make_table(data):
    a=merge(data) # calls function to mergesort the input list
    res=remove_dups(a) #calls function to remove duplicate lists
    i=0
    temp=[]
    fin=[]
    #loop to generate the search table
    while i<len(res):
        if i+1 != len(res): #condition to check if the lists contain a common first element
            if res[i][0] == res[i+1][0]: 
                temp.append(res[i][1]) #store the list of filenames in a list called temp
            else:
                temp.append(res[i][1]) 
                fin.append([res[i][0],temp]) #store the lists in the format [word,[filename]] in the final list
                temp=[]
        else: 
            if temp==[]:
                fin.append([res[i][0],[res[i][1]]])
            else:
                temp.append(res[i][1])
                fin.append([res[i][0],[res[i][1]]])
        i=i+1
    return fin
