import googlesearch as gs
while True:
    query=input("enter keywords:")
    s=gs.search("https://www.youtube.com/results?search_query="+query.replace(" ","+"),"com","en",num=10,stop=10,pause=2.0)
    for i in s:
        if i.startswith("https://www.youtube.com/watch?v="):
            print(i)
            break
