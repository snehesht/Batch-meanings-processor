import sys

def main():
    inname = open('GRE 333 Wordlist.txt','r')
    outname = open('Opt GRE 333.txt','w')
    for i in range(666):
        line = inname.readline()
        if i % 2 == 0:
            outname.write(line)
    inname.close()
    outname.close()


if __name__=="__main__":
    main()