import csv
import sys

def main(args):
    mf = args[1]
    rf = args[2]
    mf_searchingForCol = str(args[3])
    #^ name of column with messages in it
    mf_messageColInd = int(args[4])
    #^ ind of column with trial index (e.g. L100.1)
    mf_timeColInd = int(args[5])
    #^ ind of column with time value in it for message start
    mf_MSGColInd = int(args[6])
    #^ ind of column with messages in it, for writing
    #default: 2, 3, 6
    rf_messageColInd = int(args[7])
    #^ index of trial index (e.g. L100.1)
    rf_writeColInd = int(args[8])
    #^ blank col
    rf_timeCol = int(args[9])
    print(type(rf_timeCol))
    # default: 2, 8, 6
    wr = csv.writer(open("output.csv", 'w'), quoting=csv.QUOTE_ALL)
    spamreader = list(csv.reader(open(rf)))
    eggsreader = list(csv.reader(open(mf)))
    for egg in eggsreader:
        if(egg[int(mf_messageColInd)]==str(mf_searchingForCol)):
            continue
        currentMessage = egg[mf_messageColInd]
        currentTime = egg[mf_timeColInd]
        currentMSG = egg[mf_MSGColInd]
        for row in spamreader:
            print(row)
            if(row[rf_messageColInd]==currentMessage and int(row[rf_timeCol])>=int(currentTime)):
                row[rf_writeColInd]=currentMSG
                print(row[rf_writeColInd])
    
    for row in spamreader:
        wr.writerow(row)
        
    

if __name__=="__main__":
    main(sys.argv)