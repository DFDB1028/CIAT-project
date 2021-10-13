game =  ["Duck", "Duck","Duck", "Duck","Duck", "Duck", "GOOSE!", "Duck", "Duck"]
response = ["No","No","No","No","No","No","RUN!","No","No"]
for x in game:
        for y in response:
                print (x,y)
                if x == "GOOSE!":
                        break

