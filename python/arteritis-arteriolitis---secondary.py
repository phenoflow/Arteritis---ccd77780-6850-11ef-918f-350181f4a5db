# phekb, 2024.

import sys, csv, re

codes = [{"code":"35207835","system":"ICD10CM"},{"code":"35207839","system":"ICD10CM"},{"code":"35207874","system":"ICD10CM"},{"code":"35208820","system":"ICD10CM"},{"code":"35208821","system":"ICD10CM"},{"code":"35207835","system":"ICD10CM"},{"code":"35207839","system":"ICD10CM"},{"code":"35207874","system":"ICD10CM"},{"code":"35208820","system":"ICD10CM"},{"code":"35208821","system":"ICD10CM"},{"code":"44830091","system":"ICD10CM"},{"code":"44832400","system":"ICD10CM"},{"code":"44833584","system":"ICD10CM"},{"code":"44830091","system":"ICD10CM"},{"code":"44833584","system":"ICD10CM"},{"code":"44832400","system":"ICD10CM"},{"code":"314659","system":"ICD10CM"},{"code":"314963","system":"ICD10CM"},{"code":"36716136","system":"ICD10CM"},{"code":"380747","system":"ICD10CM"},{"code":"4010874","system":"ICD10CM"},{"code":"4045751","system":"ICD10CM"},{"code":"4048214","system":"ICD10CM"},{"code":"4048789","system":"ICD10CM"},{"code":"4088222","system":"ICD10CM"},{"code":"4230338","system":"ICD10CM"},{"code":"4253161","system":"ICD10CM"},{"code":"4269880","system":"ICD10CM"},{"code":"4270883","system":"ICD10CM"},{"code":"4290976","system":"ICD10CM"},{"code":"4343935","system":"ICD10CM"},{"code":"4347064","system":"ICD10CM"},{"code":"45766200","system":"ICD10CM"},{"code":"4230338","system":"ICD10CM"},{"code":"4010874","system":"ICD10CM"},{"code":"380747","system":"ICD10CM"},{"code":"314659","system":"ICD10CM"},{"code":"4048214","system":"ICD10CM"},{"code":"4088222","system":"ICD10CM"},{"code":"4048789","system":"ICD10CM"},{"code":"4045751","system":"ICD10CM"},{"code":"4343935","system":"ICD10CM"},{"code":"4347064","system":"ICD10CM"},{"code":"4269880","system":"ICD10CM"},{"code":"4270883","system":"ICD10CM"},{"code":"4290976","system":"ICD10CM"},{"code":"4253161","system":"ICD10CM"},{"code":"314963","system":"ICD10CM"},{"code":"45766200","system":"ICD10CM"},{"code":"36716136","system":"ICD10CM"},{"code":"35207835","system":"ICD10CM"},{"code":"35207839","system":"ICD10CM"},{"code":"35207874","system":"ICD10CM"},{"code":"35208820","system":"ICD10CM"},{"code":"35208821","system":"ICD10CM"},{"code":"35207835","system":"ICD10CM"},{"code":"35207839","system":"ICD10CM"},{"code":"35207874","system":"ICD10CM"},{"code":"35208820","system":"ICD10CM"},{"code":"35208821","system":"ICD10CM"},{"code":"44830091","system":"ICD10CM"},{"code":"44832400","system":"ICD10CM"},{"code":"44833584","system":"ICD10CM"},{"code":"44830091","system":"ICD10CM"},{"code":"44833584","system":"ICD10CM"},{"code":"44832400","system":"ICD10CM"},{"code":"314659","system":"ICD10CM"},{"code":"314963","system":"ICD10CM"},{"code":"36716136","system":"ICD10CM"},{"code":"380747","system":"ICD10CM"},{"code":"4010874","system":"ICD10CM"},{"code":"4045751","system":"ICD10CM"},{"code":"4048214","system":"ICD10CM"},{"code":"4048789","system":"ICD10CM"},{"code":"4088222","system":"ICD10CM"},{"code":"4230338","system":"ICD10CM"},{"code":"4253161","system":"ICD10CM"},{"code":"4269880","system":"ICD10CM"},{"code":"4270883","system":"ICD10CM"},{"code":"4290976","system":"ICD10CM"},{"code":"4343935","system":"ICD10CM"},{"code":"4347064","system":"ICD10CM"},{"code":"45766200","system":"ICD10CM"},{"code":"4230338","system":"ICD10CM"},{"code":"4010874","system":"ICD10CM"},{"code":"380747","system":"ICD10CM"},{"code":"314659","system":"ICD10CM"},{"code":"4048214","system":"ICD10CM"},{"code":"4088222","system":"ICD10CM"},{"code":"4048789","system":"ICD10CM"},{"code":"4045751","system":"ICD10CM"},{"code":"4343935","system":"ICD10CM"},{"code":"4347064","system":"ICD10CM"},{"code":"4269880","system":"ICD10CM"},{"code":"4270883","system":"ICD10CM"},{"code":"4290976","system":"ICD10CM"},{"code":"4253161","system":"ICD10CM"},{"code":"314963","system":"ICD10CM"},{"code":"45766200","system":"ICD10CM"},{"code":"36716136","system":"ICD10CM"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('arteritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["arteritis-arteriolitis---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["arteritis-arteriolitis---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["arteritis-arteriolitis---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
