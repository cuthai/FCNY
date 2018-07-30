'''

'''
import pandas as pd
from xlwt import *
import pdb
import re

#File variables. Asks for the file date to look for the specific file. Files should be named in the same convention. File path may need to be updated if folder moves.
filepath = r'O:\Medical Informatics-General\2018 Physician Vouchers\Reveal\PV Text\Physician Voucher Text '
excelfilepath = r'O:\Medical Informatics-General\2018 Physician Vouchers\Reveal\PV Excel\Physician Voucher Excel '
filedate = str(input('What is the check date? ex: YYYYMMDD -> 20180504 | '))
fileext = '.txt'
excelfileext = '.xlsx'

#Opening text file and reading data inside
voucher = filepath + filedate + fileext
openvoucher = open(voucher)
strvoucher = pd.Series(openvoucher.read())

#Initiating an Excel workbook
#excel_pv = add_sheet()


#Extract Member ID aka F1
F1_list = []
F1_str = strvoucher.str.replace('Mbr ID #:','@')
F1_df = F1_str.str.extractall("[@](\S{1,2}\d{9,10})")
F1 = 0
for x in F1_df[0]:
	F1_list.append(x)
	F1 += 1

#Extract Provider NPI aka F2
F2_list = []
F2_str = strvoucher.str.replace('Prov NPI #:','@')
F2_df = F2_str.str.extractall("[@](\d{10})")
F2 = 0
for x in F2_df[0]:
	F2_list.append(x)
	F2 += 1

#Extract Patiant Account aka F3
F3_list = []
F3_str = strvoucher.str.replace('Pat Acct #:','@')
F3_df = F3_str.str.extractall("[@](\d{1,10})")
F3 = 0
for x in F3_df[0]:
	F3_list.append(x)
	F3 += 1

#Extract Claim Number aka F4
F4_list = []
F4_str = strvoucher.str.replace('Claim #:  ','@')
F4_df = F4_str.str.extractall("[@](\d{14})")
F4 = 0
for x in F4_df[0]:
	F4_list.append(x)
	F4 += 1

#Extract Member Name aka F5
F5_list = []
F5_str = strvoucher.str.replace('Member:   ','@')
F5_df = F5_str.str.extractall("[@]([\S{20} \S{20}])")
F5 = 0
for x in F5_df[0]:
	F5_list.append(x)
	F5 += 1

#Extract Provider Name aka F6
F6_list = []
F6_str = strvoucher.str.replace('Provider:','@')
F6_df = F6_str.str.extractall("[@](\S........................)")
F6 = 0
for x in F6_df[0]:
	F6_list.append(x)
	F6 += 1

#Extract Plan aka F7
F7_list = []
F7_str = strvoucher.str.replace('Product/Plan name:','@')
F7_df = F7_str.str.extractall("[@](\S....................................)")
F7 = 0
for x in F7_df[0]:
	F7_list.append(x)
	F7 += 1

#Extract POS aka F8
F8_list = []
F8_df = strvoucher.str.split()
F8 = 0
y = re.compile('\d\d')
for x in F8_df:
	if x == y:
		F8_list.append(x)
		F8 += 1

#Extract EOP aka F10
F10_list = []
F10_str = strvoucher.str.replace('\d\d/\d\d/\d\d......','@')
F10_df = F10_str.str.extractall("[@](.[\d|\S].....)")
F10 = 0
for x in F10_df[0]:
	F10_list.append(x)
	F10 += 1

#Extract Amount Paid aka F13
F13_list = []
F13_str = strvoucher.str.replace('                                                                          0.00          0.00          .....            0.00         ','@')
F13_df = F13_str.str.extractall("[@](....\d\d)")
F13 = 0
for x in F13_df[0]:
	F13_list.append(x)
	F13 += 1

pdb.set_trace()

#print(pd.DataFrame({'Member ID': F1_list, 'Provider NPI': F2_list, 'Patient Account': F3_list, 'Claim Number': F4_list, 'Member': F5_list, 'Provider': F6_list, 'Plan': F7_list, 'EOP': F10_list, 'Amt Paid': F13_list}))