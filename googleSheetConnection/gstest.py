import time
from tokenize import group
import gspread

sa= gspread.service_account(filename="service_account_key.json") #service account connection
sh= sa.open("PolygonBotTest") #to open sheet
wks = sh.worksheet("Sheet1") #to add worksheet

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

next_row= next_available_row(wks)
input_range= 'A{}'.format(next_row) +':' + 'F{}'.format(next_row)
print(input_range)

wks.clear()

# wks.update('A3:A7',[['HELLO','TEST','3','4','5','6']])
# wks.update(input_range, [['HELLO','HELLO','this is good','2','3','3']])
# msgid=89
# groupid = -1001716786012
# replytext= 'ok22'
# cell= wks.findall(str(msgid))
# length= len(cell)
# print(length)
# i= int()
# name= 'a22'
# while i<length:
#     row= cell[i].row
#     if wks.acell('D{}'.format(row)).value == str(groupid) and wks.acell('E{}'.format(row)).value == str(msgid):
#         wks.update('G{}'.format(row), str(replytext))
#         wks.update('H{}'.format(row),str(name))

#         print('msg sent')
#         break
#     i=i+1
# print(i)
