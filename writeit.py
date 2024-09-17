import csv
import sys

def main(args):
    mf = args[1]
    rf = args[2]
    wr = csv.writer(open("output.csv", 'w'), quoting=csv.QUOTE_ALL)
    spamreader = list(csv.reader(open(rf)))
    eggsreader = list(csv.reader(open(mf)))
    for egg in eggsreader:
        if(egg[2]=="Column1"):
            continue
        currentMessage = egg[2]
        currentTime = egg[3]
        currentMSG = egg[6]
        for row in spamreader:
            if(row[2]==currentMessage and int(row[6])>=int(currentTime)):
                row[8]=currentMSG
                print(row[8])
    
    for row in spamreader:
        wr.writerow(row)
        
    

if __name__=="__main__":
    main(sys.argv)