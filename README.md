works on Windows x86 64bit processors, otherwise compile again with Python.

run the exe in the cmd line with arguments:

'''./writeit.exe messageFile recordFile'''

_writes to ./output.csv_

### Table format:

message file (csv): 

_The "TRIAL ID" column links the messages to their respective trials! make sure that the intended trial for the messages is written exactly the same in both tables._

HEADER |HEADER |TRIAL ID (THIS HEADER MUST BE LABELED EXACTLY: "Column1")|TIME|CURRENT MESSAGE
 --- | --- | --- | --- | ---
data|data|data|data|data
...|...|...|...|...

record file (csv) : 

__data in the "OUTPUT COLUMN" will be overwritten!!!__

header|header|TRIAL ID|header|header|header|TIME|header|OUTPUT COLUMN
 --- | --- | --- | --- | --- | --- | --- | --- | ---
data|data|data|data|data|data|data|data|data
...|...|...|...|...|...|...|...|...
