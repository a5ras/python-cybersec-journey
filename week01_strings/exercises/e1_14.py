""" 
Given 2024-03-15 10:23:41 ERROR Failed login from 10.0.0.5 ,
print the : 
date, time, level, and message separately. 
Hint: split(" ", 3) limits how many splits happen. 
Expected: 
four labelled lines, message = Failed login from 10.0.0.5
"""
def log_line_splitter(log):
    date , time, level, message = log.split(" ",3)
    return date , time, level, message
date , time, level, message = log_line_splitter("2024-03-15 10:23:41 ERROR Failed login from 10.0.0.5")
print(f"Date = {date}\nTime = {time}\nLevel = {level}\nMessage = {message}")
