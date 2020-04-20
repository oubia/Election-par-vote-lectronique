import random 
def inscription():
    print("***Welcome to the sign in section****")
    f=open("listes_electorale.txt","a")
    nom=(str(input("Enter your name :"))).upper()
    prenom=(str(input("Enter your firstname :"))).upper()
    while(nom == "" )or(prenom == ""):
        nom=input("Enter your name :")
        prenom=input("Enter your firstname :") 
    L=[]
    L.append(nom)
    L.append(prenom)
    f=open("listes_electorale.txt","r+")
    n=0
    for liste in f:
        n+=1
    print(n)
    while n<1000:
        if n<=9:
            login="E00"+str(n)
            break
        if n<=99 and n>=10:
            login="E0"+str(n)
            break
        if n>99:
            login="E"+str(n)

    pw,nu="",""
    for i in range (4):
        a=(random.choice("ABCDEFGHIJKLMNOPQRSTUVW"))
        pw+=a
    pw=pw+"@"
    for j in range (4):
        b=(random.randint(0,9))
        nu=nu+str(b)
    pw=pw+nu   
    L.insert(0,login)
    L.append(pw)
    print("***Successful Registration***")
    print("Your informatin ARE :")
    print(" Login : ",login)
    print(" Password : ",pw)
    f.write(str(L)+'\n')    
    f.close 
# ======================================================================================================
def __test__():
    with open("listes_electorale.txt",'r+') as f:
        L=[]
        L=f.readlines()
        a=str(input("wirte your code"))
        b=str(input("wirte your password"))
    for i in range (len(L)):
                if a and b in L[i]:
                    return True 
    return False          
def virification():
    with open("listes_electorale.txt",'r+') as f:
        L=[]
        L=f.readlines()
#         print(L)      
#         __test__()
        if __test__()!=True:
                c=(str(input("are you sur that you already sign up??? (Y/N):"))).upper()
                if c == "Y":
                    __test__()
                    exit()
                    
                elif c == "N":
                    print("please sign up ")
                    inscription()
                    exit()     
        exit()
# ----------------------------------
def liste():
    j=open("liste_condidat.txt","r+")
    for linge in j:
        print(linge)
    j.close 
# -----------------------------------------------------------------------    
import pickle 
def __cree_votes():
        a1="C1"
        a2="C2"
        a3="C3"
        a4="C4"
        vote={"C1":[],"C2":[],"C3":[],"C4":[]}
        with open("list_votes.txt","ab") as fic:
            my_pikler=pickle.Pickler(fic)
            my_pikler.dump(vote)
# ===========================================================
def votes():
    __cree_votes()
    a1="C1"
    a2="C2"
    a3="C3"
    a4="C4"
    virification()
    P=["C1","C2","C3","C4"]
    liste()
    a=(str(input("wirte your choise"))).upper()
    
    while a not in P:
        b=input("invalid please wirte your choise")
        a=str(b)
        a=a.upper()
    con=(str(input("confirme your choise (Y/N)"))).upper()
    
    while(con != "Y"and con !="N") :
        con=(str(input("confirme your choise (Y/N)"))).upper()
    if con == "N":
        choise=input("wirte your choise")
        con=(str(input("confirme your choise (Y/N)"))).upper()
    
    elif con =="Y":
        with open('list_votes.txt', 'rb') as file:
            mon_dipickler=pickle.Unpickler(file)
            vote=mon_dipickler.load()
            if a1 == a:
                vote["C1"].append(1)
            elif a2 == a:
                vote["C2"].append(1)
            elif a3 == a:
                vote["C3"].append(1)
            elif a4 == a:
                vote["C4"].append(1)
            with open('list_votes.txt', 'wb') as file:
                mon_pickler = pickle.Pickler(file)
                mon_pickler.dump(vote)
            print("your choise is comfirmed")
# ========================================================================
import pickle
def statistique():
    print("****Results are: ****\n")
    with open('list_votes.txt','rb') as fi:
            mon_dipickler=pickle.Unpickler(fi)
            vote=mon_dipickler.load()
            c1=int(str(len(vote['C1'])))
            c2=int(str(len(vote['C2'])))
            c3=int(str(len(vote['C3'])))
            c4=int(str(len(vote['C4'])))
            p=c1+c2+c3+c4

    with open('listes_electorale.txt','r') as f:
        co=0
        for ligne in f:
            co=co+1
    print("Number of votes :",p,"/",co)
    print("C1 --> YAHYA KHARBANE ",c1,"votes","(",(c1/co)*100,"%)")
    print("C2 --> MOHCINE OUCHEN",c2,"votes","(",(c2/co)*100,"%)")
    print("C3 --> FATIMA EL JAMILI",c3,"votes","(",(c3/co)*100,"%)")
    print("C4 --> blanc",c4,"votes","(",(c4/co)*100,"%)")
            
statistique()

# =====================================================================
def afiche():
    print("===== Election 2020 =======")
    with open('list_votes.txt','rb') as fi:
            mon_dipickler=pickle.Unpickler(fi)
            vote=mon_dipickler.load()
            c1=int(str(len(vote['C1'])))
            c2=int(str(len(vote['C2'])))
            c3=int(str(len(vote['C3'])))
            c4=int(str(len(vote['C4'])))
            p=c1+c2+c3+c4

    with open('listes_electorale.txt','r') as f:
        co=0
        for ligne in f:
            co=co+1
    print("Now",p," personnes  voted (On",co,")")
    print("-----------------------------------------\n \t 1 : Inscription\n \t 2 : Liste codes --> candidat\n \t 3 : Vote\n \t 4 : Statistices\n \t 5 : Exit\n-----------------------------------------")
# ===============================================================

def prancipal():
    afiche()
    a=str(input("enter your choise :\n"))
    l=["1","2","3","4","5"]
    while(a not in l):
        a=str(input("enter your choise :\n"))
    if a=="1":
        inscription()
        afiche()
        a=str(input("enter your choise :\n"))
        l=["1","2","3","4","5"]
        while(a not in l):
            a=str(input("enter your choise :\n"))
    if a=="2":
        liste()
        afiche()
        a=str(input("enter your choise :\n"))
        l=["1","2","3","4","5"]
        while(a not in l):
            a=str(input("enter your choise :\n"))
    if a=="3":
        votes()
        afiche()
        a=str(input("enter your choise :\n"))
        l=["1","2","3","4","5"]
        while(a not in l):
            a=str(input("enter your choise :\n"))
    if a=="4":
        statistique()
        afiche()
        a=str(input("enter your choise :\n"))
        l=["1","2","3","4","5"]
        while(a not in l):
            a=str(input("enter your choise :\n"))
    if a=="5":
        l=["1","2","3","4","5"]
        while(a not in l):
            a=str(input("enter your choise :\n"))
        exit()
prancipal()