def UserDetails():
    d={}
    f=open("Data/user_log.txt","r")
    text=f.readlines()
    
    
    for word in text:
        word=word.split()
        d[word[0]]=word[1]
    return d    