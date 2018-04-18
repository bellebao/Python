# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:09:46 2018

@author: Belle Bao
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:07:45 2018

Note: Calculate a cycle time by the PAR status. The end time is inwork/close,
the initial time is raised. CT is the time buffer between them.

@author: Belle Bao
"""

import re
import os
#import win32com.client

from openpyxl.workbook import Workbook


f_result_file = r"C:\IOSystems\A300\PAR\PAR_Analysis\Results.xlsx"  # output file for CT
path = "C:\IOSystems\A300\PAR\PAR_Analysis\Par"   # input file where have FCR
#--------------------------------CONSTANTS-------------------------------------
wdFormatText = 2

#--------------------------------GLOBALS---------------------------------------

PAR_NoTemp= ''
CTtemp = ''
templine = []
Functionslist = {}
filenum = 0
ICDVersionlist=[]

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
    count = 0
    Functionline = []

    
    
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
        keyword = "C_AIRBUS:"
        count = 0
        for (line) in parsefile.readlines():            
            if (keyword in line):
                count = count +1
                line=line.strip('\n')
                Functionline.append(line)
                
                ICDversion = re.search(r"(C_AIRBUS:\w{0,4}.A-DOC;\d{1,2})", line) 
                
                ICDVersionlist.append(ICDversion.group(0))
                #print (Functionline)
        
        Functionslist.update({PAR_NoTemp:Functionline})


def cli():  
    global filenum

    ParseFile(path)
    #print (Functionslist)

    wb = Workbook()
    ###############################################
    ws1 = wb.active
    ws1.title = "FunctionList"
    
    wsheader = ["PAR No.", "functions versions"]
    ws1.append(wsheader)
    for key in Functionslist.keys():
        row = [key]
        row.extend(Functionslist.get(key))
        ws1.append(row)
        
    ws2 = wb.create_sheet()
    ws2.title = "VersionList"
    
    wsheader = ["Version"]
    ws2.append(wsheader)
    for key in ICDVersionlist:
        row = [key]
        ws2.append(row)
        
    print ("-->Saving File: "+f_result_file)
    wb.save(f_result_file)          
    print ("-->Done!")

if __name__ == "__main__":
    cli()        
        
        
        
        