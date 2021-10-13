joke = ["Why did the chicken cross the road"]
why1 ="\n To reach the roosters on the other side"
why2 ="\n to drop an egg"
why3 ="\n just cause"
why_who =[why1 ,why2 ,why3]
for x in joke:
    for y in why_who:
        print(x,y)
    if y == "just cause":
        print ("really")

