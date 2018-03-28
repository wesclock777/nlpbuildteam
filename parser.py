import csv

def maximumoccurances(occurancemap):
    index = 0
    max = 0
    for i,num in enumerate(occurancemap):
        if num > max:
            max = num
            index = i
    return index

rows=[]
with open('data.csv', newline='') as csvfile:
    fields = ['Resource','Website','Email', 'Phone number', 'Office Location', 'Office Hours', 'Info']
    reader = csv.DictReader(csvfile, restkey='Keywords', fieldnames=fields, delimiter=',')
    for line in reader:
        rows.append(line)
keywords = input("put your keywords here: ")
keywords = keywords.split(" ")
if("AND" in keywords):
    keywords.remove("AND")

occurancemap = []
for i, row in enumerate(rows):
    occurances=0
    print(row['Keywords'])
    for savedkeyword in row['Keywords']:
        if savedkeyword in keywords:
            occurances+=1
        if len(savedkeyword.split("AND"))>1:
            savedkeywords = savedkeyword.split("AND") 
            for key in savedkeywords:
                key=key.strip()
                if(key in keywords):
                    occurances+=1
    occurancemap.append(occurances)

print(occurancemap[maximumoccurances(occurancemap)])
print((rows[maximumoccurances(occurancemap)])['Resource'])
