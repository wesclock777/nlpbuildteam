from __future__ import print_function

import csv

def lambda_handler(event):
    event = event.strip()
    if comparetxt(event,"help!"):
        print(xml("This format of the search is structured like so:\n \
        keyword:query"))
        return
    message = event
    message = message.split(":")
    print(len(message))
    if len(message) < 2:
        print(xml(error()))
        return
    query = message[1]
    keyword = message[0]
    query = query.strip()
    keyword = keyword.strip()
    for row in rows:
        if keyword in row['Keywords']:
            return parse(row, query)
    print(xml(error()))
    return

def error():
    return "Oops I did not understand that message, type help! to get information on the query format!"

def parse(row, query):
    print(row)
    text= "The "+row["Resource"]+" has no value for: "+query+"."
    if query in row:
        text = "Your query returned: "+row[query]+"."

    return xml(text)

def xml(text):
    print('<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message>'+text+'</Message></Response>')
    return

def comparetxt(text1, text2):
    return text1.upper()==text2.upper()

rows = [];

with open('data.csv', newline='') as csvfile:
    fields = ['Resource','Website','Email', 'Phone number', 'Office Location', 'Office Hours', 'Info']
    reader = csv.DictReader(csvfile, restkey='Keywords', fieldnames=fields, delimiter=',')
    for line in reader:
        rows.append(line)

applesauce = input("Thing you texted:")
lambda_handler(applesauce)
