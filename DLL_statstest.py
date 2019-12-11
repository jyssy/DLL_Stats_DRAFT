# Statistics for Cataloging/Metadata Department (run monthly)
# Thanks to the folks

import sys
import os
import csv

with open('init_code.csv', 'r') as init_file:
    stat_reader = init_file.read().split('\n')
    while True: # Attempting to scratch the empty lines from the source data
        try:
            stat_reader.remove('')
        except ValueError:
            break

    # Moving the data into the required hashable form (to get unique values)
    dataSet = set(stat_reader)

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
    # June 10, 2019, we decided to add a PCC code to the dicetaionary - instead of keeping the bibCo stats separately (jal)

    with open('stats_out.csv', 'w', newline='') as stats_output:
    # writer = csv.writer(stats_output, delimiter=':')
        writer = csv.writer(stats_output, delimiter=':')

        for stat in dataSet:
            statCount = stat_reader.count(stat)
            name_stat = team[stat[:3]]
            code_stat = codes[stat[-3:]]

            '''Using 'write' in the csv module to output the necessary
            info. Ths data is still not alphabetized - but that will come eventually as I learn python'''

            if stat != 'iniCOD':

                writer.writerow([name_stat, code_stat, str(statCount)])

            else:

                print('all good')

                # print(name + ': ' + code + ': ' + str(statCount))
