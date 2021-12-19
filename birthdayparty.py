events = [ { "alien sarees" :  [ { "sliksarres" : ["A1" ,"A2" ] }]}]

for shopping in events:
    print(shopping)
    for i,v in shopping.items():
           print( i ,v )
           if "sliksarres" in v[0] :
               print(" found it " ,v[0]["sliksarres"])

            

memcount = 10
buffet= [ {"biryani":25 , "Eggs": 25  , "chickenpiece": 50}, {"icecream":25 , "jamon":25} ]
def havedinner( person ,i ):
    '''
    buffet[i]["biryani"] =buffet[i]["biryani"]-1
    buffet[i]["Eggs"] =buffet[i]["Eggs"]-1
    buffet[i]["chickenpiece"] =buffet[i]["chickenpiece"]-2

    buffet[i+1]["icecream"] =buffet[i+1]["icecream"]-1
    buffet[i+1]["jamon"] =buffet[i+1]["jamon"]-1
    '''
    for i in buffet:
        if "biryani" in  i:
            i["biryani"] = i["biryani"]-1
            i["Eggs"] = i["Eggs"]-1
            i["chickenpiece"] = i["chickenpiece"]-1
        elif "icecream" in i:
            i["icecream"] =i["icecream"]-1
            i["jamon"] =i["jamon"]-1
   
    print("hno of people had food ",buffet)
    
def  Birthdayparty( relatives:dict )->list:
     if isinstance( relatives , dict) == False:
         raise TypeError("invalid type")
     if len(relatives)>10:
         raise ValueError("no food")
     gft=[]
     for come ,gift in relatives.items():
        if come :
            havedinner( come ,0 )
        if gift == None:
            continue 
        else:
            gft.append(gift)
     #print("total gifts",  gft)
     return gft
     #return "thanking u for coming"       


#Birthdayparty( {"ramesh" : "chcolates","suresh":"pen","rajesh":"diary","suma":None,"seetha":None } )
ret = Birthdayparty( {"ramesh" : "chcolates","suresh":"pen","rajesh":"diary","suma":None,"seetha":None } )
if type(ret) is list:
    #print("return value ",ret)
