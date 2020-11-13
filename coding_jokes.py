import pyjokes

def joke():
    print(pyjokes.get_joke())

def main():
    while True:
        joke()
        choice=input("Do you want to hear another joke?(y/n)")
        if choice in ["y","Y","yes","YES","Yes"]:
            continue
        else:
            break

if __name__=="__main__":
    main()
