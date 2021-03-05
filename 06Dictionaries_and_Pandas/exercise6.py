#Dictinary of dictinaries 
europe = { 'spain': {'capital': 'madrid','poplution':46.77},
            'france':{'capital':'paris','population':66.03},
            'germany':{'capital':'berlin','population':80.62},
            'norway':{'capital':'oslo','population':5.084} }

#print out the capital of France
print(europe['france']['capital'])

#Create sub-dictionary data
deta={'capital':'rome','population':'59.83'}

#Add data to Europe under key 'italy'
europe['italy']=deta

#print europe 
print(europe)