import pickle
def search():
    file=open("TRAIN.dat","rb")
    found=0
    try:
        while True:
            train=pickle.load(file)
            if train["To"]=="Delhi":
                print(train)
                found=1
    except EOFError:
        if found==0:
            print("Not found")
    file.close()
search()
