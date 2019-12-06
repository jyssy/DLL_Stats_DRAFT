# Statistics for Cataloging/Metadata Department (run monthly)
# Thank you Matt Zimmerman & Kim Kelmor
# Uses data from an OLE Report (item records and bib data)

import sys
import os
import csv
import operator

# replace the name with the actual csv file name or change the name to 'Cataloging_stats.csv'
file_name = "Cataloging_Stats.csv"
f = open(file_name, encoding='utf-8')
csv_file = csv.reader(f)
eighth_column = [] # empty list to store seventh column values
for line in csv_file:
    eighth_column.append(line[6])

# removes empty lines, puts in required header file, strips out old header file
dataList=[s for s in eighth_column if s.strip()]
dataList.insert(0, 'iniCOD')
#dataList.remove('Item note')

# make the list object into a set object
dataSet=set(dataList)
# this init_code.csv segment was from an older version (but still here in case...jal) This version skips a step from the older version.
# with open('init_code.csv', 'r') as init_file:
# stat_reader = init_file.read().split('\n')

team = dict(jal='Jesse Lambertson ', psm='Pat Sayre-McCoy ', mcd='Melanie Dial ', den='Daryl Nelson ', jrs='Julie Stauffer ', naa='Nissy ', dmd='Dora Davis ', ini='Initial_header ')
codes = dict(PMO=' Print Monograph Original ', PML=' Print Monograph LC copy ', PMC=' Print Monograph OCLC copy ', COD=' Code_header ',
                 PMR=' Print Monograph OCLC Revised ', PMB=' Print Monograph Rare Book cataloging ', PPC=' Print PCC Original ',
                 PCU=' Print PCC Upgrade ', PSO=' Print Serial Original ',
                 PSL=' Print Serial LC copy ', PSC=' Print Serial OCLC copy ', PSR=' Print Serial OCLC Revised ',
                 MWL=' Monograph WLAW ', WMO=' Web monograph Original ', WML=' Web Monograph LC Copy ',
                 WMC=' Web monograph OCLC copy ', WMR=' Revised web monograph ', WSO=' Web Serial Original ',
                 WSL=' Web Serial LC copy ', WSC=' Web Serial OCLC ', WSR=' Web Serial Revised ',
                 IOR=' Integrating Original Resource ', ICR=' Integrating OCLC Resource ', ILR=' Integrating LC Resource ', NNA=' New NACO Contribution ',
                 RNA=' Print Serial Enrich ', NSA=' New Series contribution ', RSA=' Revised Series contribution ',
                 RMB=' Revised Monograph Bibliographic ', RSB=' Revised Serial Bibliographic ', RIB=' Revised Integrating Bibliographic ',
                 DVO=' DVD Original ', DVC=' DVD OCLC copy ', DVL=' DVD LC Copy ',
                 ADD=' Added volume (added copy) ')

# Loop through the set.
# Count number of occurrences of each set element in the list
# Includes PCC BibCO (lambertson). NACO is, by necessity, collected separately.

with open('interim.csv', 'w', newline='') as unsorted:
    # writer = csv.writer(stats_output, delimiter=':')
    writer = csv.writer(unsorted, delimiter=':')

    for stat in dataSet:

            name_stat = team[stat[:3]]
            code_stat = codes[stat[-3:]]
            statCount =dataList.count(stat)

#        '''Using 'write' in the csv module to output the necessary
#            info. '''

            if stat != 'iniCOD':

                writer.writerow([name_stat, code_stat, str(statCount)])

            else:

                print('all good')

            # print(name + ': ' + code + ': ' + str(statCount))

# sort the data and save it to a new csv
data = csv.reader(open('interim.csv'),delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort
      # now write the sorte result into new CSV file
with open("stats_out.csv", 'w', newline='') as final:
    fileWriter = csv.writer(final, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)

print('complete, yay!')

