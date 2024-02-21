import csv

def sequencer(lst):   
    result = [] 
    off_peak = [i for i in lst if i['shape']=='Off-peak']
    off_peak_sequence = min(i['sequence'] for i in off_peak)
    result.extend([i for i in off_peak if i['sequence']==off_peak_sequence])
    
    peak_wd = [i for i in lst if i['shape']=='PeakWD']
    peak_wd_sequence = min(i['sequence'] for i in peak_wd)
    result.extend([i for i in peak_wd if i['sequence']==peak_wd_sequence])
    
    peak_we = [i for i in lst if i['shape']=='PeakWE']    
    peak_we_sequence = min(i['sequence'] for i in peak_we)
    result.extend([i for i in peak_we if i['sequence']==peak_we_sequence])
    
    return result
    
with open('HB_NORTH_CRR.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(len(data))

res = []
for year in range(2019,2027):
    for months in range(1,13):
        lst =[]
        for i in data:
            month = ('0'+str(months))[-2:]
            date = f'{year}-{month}-01'
            if i['fordate'] == date:
                lst.append(i)
        if lst:
            sequenced = sequencer(lst)
            res.extend(sequenced)
        
        
with open("answer.csv", "w", encoding="utf-8") as f:
    fieldnames = ["iso", "refdate", "fordate", "sequence",'node','shape','price']
    dictwriter = csv.DictWriter(f, fieldnames=fieldnames)
    dictwriter.writeheader()
    for i in res:
        dictwriter.writerow(
            {
                "iso": i["iso"],
                "refdate": i["refdate"],
                "fordate": i["fordate"],
                "sequence": i["sequence"],
                "node": i["node"],
                'shape': i["shape"],
                'price': i["price"],
                
            }
        )
