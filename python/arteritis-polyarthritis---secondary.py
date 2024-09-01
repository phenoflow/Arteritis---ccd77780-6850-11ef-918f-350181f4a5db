# phekb, 2024.

import sys, csv, re

codes = [{"code":"1570609","system":"ICD10CM"},{"code":"35208811","system":"ICD10CM"},{"code":"35208813","system":"ICD10CM"},{"code":"35208815","system":"ICD10CM"},{"code":"1570609","system":"ICD10CM"},{"code":"35208811","system":"ICD10CM"},{"code":"35208813","system":"ICD10CM"},{"code":"35208815","system":"ICD10CM"},{"code":"44819728","system":"ICD10CM"},{"code":"44830096","system":"ICD10CM"},{"code":"44819728","system":"ICD10CM"},{"code":"44830096","system":"ICD10CM"},{"code":"320749","system":"ICD10CM"},{"code":"40481092","system":"ICD10CM"},{"code":"4056348","system":"ICD10CM"},{"code":"4067424","system":"ICD10CM"},{"code":"4101891","system":"ICD10CM"},{"code":"4111856","system":"ICD10CM"},{"code":"4113582","system":"ICD10CM"},{"code":"4220130","system":"ICD10CM"},{"code":"4343931","system":"ICD10CM"},{"code":"4343932","system":"ICD10CM"},{"code":"4344168","system":"ICD10CM"},{"code":"4344489","system":"ICD10CM"},{"code":"4344490","system":"ICD10CM"},{"code":"4347062","system":"ICD10CM"},{"code":"4067424","system":"ICD10CM"},{"code":"320749","system":"ICD10CM"},{"code":"4101891","system":"ICD10CM"},{"code":"4111856","system":"ICD10CM"},{"code":"4056348","system":"ICD10CM"},{"code":"4343931","system":"ICD10CM"},{"code":"4347062","system":"ICD10CM"},{"code":"4343932","system":"ICD10CM"},{"code":"4344489","system":"ICD10CM"},{"code":"4344490","system":"ICD10CM"},{"code":"4344168","system":"ICD10CM"},{"code":"4113582","system":"ICD10CM"},{"code":"4220130","system":"ICD10CM"},{"code":"40481092","system":"ICD10CM"},{"code":"1570609","system":"ICD10CM"},{"code":"35208811","system":"ICD10CM"},{"code":"35208813","system":"ICD10CM"},{"code":"35208815","system":"ICD10CM"},{"code":"1570609","system":"ICD10CM"},{"code":"35208811","system":"ICD10CM"},{"code":"35208813","system":"ICD10CM"},{"code":"35208815","system":"ICD10CM"},{"code":"44819728","system":"ICD10CM"},{"code":"44830096","system":"ICD10CM"},{"code":"44819728","system":"ICD10CM"},{"code":"44830096","system":"ICD10CM"},{"code":"320749","system":"ICD10CM"},{"code":"40481092","system":"ICD10CM"},{"code":"4056348","system":"ICD10CM"},{"code":"4067424","system":"ICD10CM"},{"code":"4101891","system":"ICD10CM"},{"code":"4111856","system":"ICD10CM"},{"code":"4113582","system":"ICD10CM"},{"code":"4220130","system":"ICD10CM"},{"code":"4343931","system":"ICD10CM"},{"code":"4343932","system":"ICD10CM"},{"code":"4344168","system":"ICD10CM"},{"code":"4344489","system":"ICD10CM"},{"code":"4344490","system":"ICD10CM"},{"code":"4347062","system":"ICD10CM"},{"code":"4067424","system":"ICD10CM"},{"code":"320749","system":"ICD10CM"},{"code":"4101891","system":"ICD10CM"},{"code":"4111856","system":"ICD10CM"},{"code":"4056348","system":"ICD10CM"},{"code":"4343931","system":"ICD10CM"},{"code":"4347062","system":"ICD10CM"},{"code":"4343932","system":"ICD10CM"},{"code":"4344489","system":"ICD10CM"},{"code":"4344490","system":"ICD10CM"},{"code":"4344168","system":"ICD10CM"},{"code":"4113582","system":"ICD10CM"},{"code":"4220130","system":"ICD10CM"},{"code":"40481092","system":"ICD10CM"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('arteritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["arteritis-polyarthritis---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["arteritis-polyarthritis---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["arteritis-polyarthritis---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
