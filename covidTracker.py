import sys



def main():
    if(len(sys.argv) == 3):
        f1 = open(str(sys.argv[2]), "r")
        print(sys.argv[1])
        print(sys.argv[2])
    if(len(sys.argv) == 5):
        f1 = open(str(sys.argv[2]))
        f2 = open(str(sys.argv[4]))
        print(sys.argv[1])
        print(sys.argv[2])
        print(sys.argv[3])
        print(sys.argv[4])
    data1 = f1.read()
    data2 = f2.read()
    print(data1)
    print(data2)
    print(f1)


if __name__== '__main__':
    main()
