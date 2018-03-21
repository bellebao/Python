# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:49:49 2018

@author: E435157
"""
import re
from datetime import datetime

test_date = '1     23-JAN-2017 23:28:18                      Mike Diaz 6-4547'


# date
mat = re.search(r"(\d{2}-(DEC|NOV|JAN)-\d{4})",test_date)
print (mat.group(0))

