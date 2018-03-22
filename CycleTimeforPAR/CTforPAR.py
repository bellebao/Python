# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:07:45 2018

@author: E435157
"""

import sys
import os
import string
#import win32com.client
import re
import datetime
f_output = r"C:\IOSystems\Agusta\FCR\PPC\CT_output.txt"
#--------------------------------CONSTANTS-------------------------------------
wdFormatText = 2

#--------------------------------GLOBALS---------------------------------------
TimeRaisedTemp = ''
TimeInworkTemp = ''
PAR_NoTemp= ''
CTtemp = ''
templine = []
InreviewTime = ''
CycleTime = {}
filenum = 0


def ParseFile(path):
    
    if os.path.isdir(path):
        filenum = len(os.listdir(path))
        for sub_dir in os.listdir(path):
            filename = os.path.join(path, sub_dir)
            ParseFile(filename)
    else:
        TraceParser(path)
    

def TraceParser(filename):
    
    global filenum
    #global CycleTime
    fileext = ""
    actionline = []
    actionflag = 0

    #filename = str.lower(filename)
    index = filename.rfind('.')
    
    if (index != -1):
        fileext = filename[index:]
    
    if (fileext in [".par", ".fcr", ".scn",".txt"]):
        
        filenum = filenum + 1    
        
        # get the filename without the directory
        abbrname = os.path.split(filename)[1]
        PAR_NoTemp = abbrname.split('.')[0]
        
        # start parsing the file
        parsefile = open(filename, 'r')
        keyword = "ACTION HISTORY"
        count = 0
        for (line) in parsefile.readlines():
            count = count +1
            if (keyword in line):
                actionflag = 1
            
            if(actionflag == 1):
                actionline.append(line)
                #print (actionline)
        if(actionflag == 1):        
            raisedTime = re.search(r"(\d{2}-(DEC|NOV|OCT|SEP|AUG|JUL|JUN|MAY|APR|MAR|FEB|JAN)-\d{4})", actionline[1]) 
            raisedTimeBeforFormat = raisedTime.group(0)
            raisedTimeFormat = transferdate(raisedTimeBeforFormat)
        #print (raisedTime.group(0))
        count = 0
        for line in actionline:     
            count = count +1
            if ("Actioned document from IMPLEMENTATION to REVIEW" in line) or ("Actioned document from IMPLEMENTATION to CLOSED" in line):
                #continue
                InreviewTime = re.search(r"(\d{2}-(DEC|NOV|OCT|SEP|AUG|JUL|JUN|MAY|APR|MAR|FEB|JAN)-\d{4})", actionline[count-3])
                #print (InreviewTime)
                InreviewTimeBeforFormat = InreviewTime.group(0)
                InreviewTimeFormat = transferdate(InreviewTimeBeforFormat)
                CT = calculateCT(raisedTimeFormat, InreviewTimeFormat)
                CycleTime.update({PAR_NoTemp:[raisedTimeBeforFormat,InreviewTimeBeforFormat,CT]})
                break


def calculateCT(raisedTimeFormat, InreviewTimeFormat):
    date1 =  raisedTimeFormat.split('-') 
    date2 =  InreviewTimeFormat.split('-') 
    d1 = datetime.datetime(int(date1[2]),int(date1[1]),int(date1[0]))
    d2 = datetime.datetime(int(date2[2]),int(date2[1]),int(date2[0]))
    return (d2-d1).days    

def transferdate(dateinStr):
    if "JAN" in dateinStr:
        dateinStr=dateinStr.replace('JAN','01')
        return dateinStr
    if "FEB" in dateinStr:
        dateinStr=dateinStr.replace('FEB','02')        
        return dateinStr
    if "MAR" in dateinStr:
        dateinStr=dateinStr.replace('MAR','03')        
        return dateinStr
    if "APR" in dateinStr:
        dateinStr=dateinStr.replace('APR','04')
        return dateinStr
    if "MAY" in dateinStr:
        dateinStr=dateinStr.replace('MAY','05')        
        return dateinStr
    if "JUN" in dateinStr:
        dateinStr=dateinStr.replace('JUN','06')        
        return dateinStr
    if "JUL" in dateinStr:
        dateinStr=dateinStr.replace('JUL','07')
        return dateinStr
    if "AUG" in dateinStr:
        dateinStr=dateinStr.replace('AUG','08')        
        return dateinStr
    if "SEP" in dateinStr:
        dateinStr=dateinStr.replace('SEP','09')        
        return dateinStr
    if "OCT" in dateinStr:
        dateinStr=dateinStr.replace('OCT','10')
        return dateinStr
    if "NOV" in dateinStr:
        dateinStr=dateinStr.replace('NOV','11')        
        return dateinStr
    if "DEC" in dateinStr:
        dateinStr=dateinStr.replace('DEC','12')        
        return dateinStr    
def cli():  
    global filenum
    path = "C:\IOSystems\Agusta\FCR"
    ParseFile(path)
    print (CycleTime)
    ff = open(f_output, 'w')
    ff.writelines( "%s\t%s\t%s\t%s\n" % ("PAR","RAISED Time","Review Time","Cycle Time") )
    for key in CycleTime:
        ff.writelines( "%s\t%s\t%s\t%s\n" % (key, CycleTime[key][0], CycleTime[key][1], CycleTime[key][2]) )
    ff.close()


if __name__ == "__main__":
    cli()        
        
        
        
        