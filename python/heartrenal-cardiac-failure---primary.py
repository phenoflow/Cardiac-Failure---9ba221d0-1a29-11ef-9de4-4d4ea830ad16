# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2024.

import sys, csv, re

codes = [{"code":"G583.12","system":"readv2"},{"code":"G583.00","system":"readv2"},{"code":"SP11111","system":"readv2"},{"code":"9Or3.00","system":"readv2"},{"code":"9Or1.00","system":"readv2"},{"code":"8HHb.00","system":"readv2"},{"code":"G230.00","system":"readv2"},{"code":"G21z100","system":"readv2"},{"code":"9Or0.00","system":"readv2"},{"code":"8HTL.00","system":"readv2"},{"code":"9N2p.00","system":"readv2"},{"code":"8HTL000","system":"readv2"},{"code":"8CMK.00","system":"readv2"},{"code":"8HBE.00","system":"readv2"},{"code":"14A6.00","system":"readv2"},{"code":"1O1..00","system":"readv2"},{"code":"G583.11","system":"readv2"},{"code":"8CL3.00","system":"readv2"},{"code":"G5y4z00","system":"readv2"},{"code":"G58z.00","system":"readv2"},{"code":"679X.00","system":"readv2"},{"code":"67D4.00","system":"readv2"},{"code":"G210.00","system":"readv2"},{"code":"679W100","system":"readv2"},{"code":"G557100","system":"readv2"},{"code":"G582.00","system":"readv2"},{"code":"14AM.00","system":"readv2"},{"code":"1J60.00","system":"readv2"},{"code":"9hH0.00","system":"readv2"},{"code":"662T.00","system":"readv2"},{"code":"662p.00","system":"readv2"},{"code":"G58..00","system":"readv2"},{"code":"8H2S.00","system":"readv2"},{"code":"662W.00","system":"readv2"},{"code":"G211100","system":"readv2"},{"code":"G580000","system":"readv2"},{"code":"9N0k.00","system":"readv2"},{"code":"G210100","system":"readv2"},{"code":"9Or5.00","system":"readv2"},{"code":"G58z.11","system":"readv2"},{"code":"G580.00","system":"readv2"},{"code":"661M500","system":"readv2"},{"code":"G580.12","system":"readv2"},{"code":"8CMW800","system":"readv2"},{"code":"G580400","system":"readv2"},{"code":"I13.2","system":"readv2"},{"code":"I11.0","system":"readv2"},{"code":"I50","system":"readv2"},{"code":"I50.0","system":"readv2"},{"code":"I13.0","system":"readv2"},{"code":"I50.9","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiac-failure-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["heartrenal-cardiac-failure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["heartrenal-cardiac-failure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["heartrenal-cardiac-failure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
