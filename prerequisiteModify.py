import itertools

def translate(string):

    string = string[:len(string)-1] # removes period

#seperates string into AND pieces
    if '; and ' in string:
        stringList = string.split('; and ')
    if ' and ' in string:
        stringList = string.split(' and ')
    else:
        stringList = string.split('; ')
#print(stringList)

#Seperates each individual AND piece into it's seperate OR pieces    
    for i in range(len(stringList)):
    
        if 'one of ' in stringList[i]:
            stringList[i] = stringList[i][7:]
            stringList[i] = stringList[i][:stringList[i].find(' or ')]+', '+stringList[i][stringList[i].find(' or ')+4:]
            stringList[i] = stringList[i].split(", ")
        #print(stringList[i])
        else:
            stringList[i] = stringList[i].split(" or ")


    for i in range(len(stringList)):
        for j in range(len(stringList[i])):
            if len(stringList[i][j])>3:
                name = stringList[i][j][:-4]
            else:
                stringList[i][j] =  name + ' ' + stringList[i][j]          
                            
    



    all_prereqs = list(itertools.product(*stringList))
    stringToGo = ''
    for i in all_prereqs:
        for j in range(len(i)-1):
            stringToGo += i[j] + ';'
        stringToGo += i[len(i)-1]+'|'
    stringToGo = stringToGo[:-1]
    return stringToGo
  

        
string = "Computer Science 355 and one of 319 or 331."
print(translate(string))
    
