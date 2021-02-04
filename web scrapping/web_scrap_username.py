import googlesearch as gs
def insta(username):
    instagram=gs.search("instagram "+username,"com","en",num=5,stop=5,pause=2.0)
    for insta in instagram:
        if username in insta:
            return "Instagram: "+insta
    return "Instagram: Not found"

def facebook(username):
    facebook=gs.search("facebook "+username,"com","en",num=5,stop=5,pause=2.0)
    for fb in facebook:
        if username in fb:
            return "Facebook: "+fb
    return "Facebook: Not found"

def main():
    username=input("username: ")
    print(insta(username))
    print(facebook(username))

while True:
    main()
