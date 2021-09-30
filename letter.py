def mostcommonfirstletters(s):
    d=s.split(" ")
    count=0
    s1=""
    for i in range(0,len(d),1):
        s1=s1+d[i][0]
    count=s1.count(s1[0])
    for i in range(1,len(s1),1):
        ch=s1[i]
        if(s1.count(ch)>count):
            count=s1.count(ch)
            print(ch)
mostcommonfirstletters("do you have a voting plan for the election happening next month?")
