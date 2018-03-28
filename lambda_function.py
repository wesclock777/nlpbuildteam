from __future__ import print_function

import csv

def lambda_handler(event,context):
    rows=[]
    with open('data.csv', newline='') as csvfile:
        fields = ['Resource','Website','Email', 'Phone number', 'Office Location', 'Office Hours', 'Info']
        reader = csv.DictReader(csvfile, restkey='Keywords', fieldnames=fields, delimiter=',')
        for line in reader:
            rows.append(line)
    message = urldecode(event['Body'])
    print(message)
    if comparetxt(message,"help!"):
        return (xml("This format of the search is structured like so:\n\nkeyword:query \n\ntext query! to list query terms"))
    if comparetxt(message,"query!"):
        return (xml("Query terms include: ['Resource','Website','Email', 'Phone number', 'Office Location', 'Office Hours', 'Info']"))
    message = message.split(":")
    if len(message) < 2:
        return (xml(error()))
    query = message[1].title()
    keyword = message[0].lower()
    query = query.strip()
    keyword = keyword.strip()
    for row in rows:
        if keyword in row['Keywords']:
            return parse(row, query)
    return (xml(error()))

def urldecode(url):
    from urllib.parse import unquote
    url = url.replace('+','%20')
    url = unquote(url)
    return url

def error():
    return "Oops I did not understand that message, type help! to get information on the query format!"

def parse(row, query):
    text= "The "+row["Resource"]+" has no value for: "+query+"."
    if query in row:
        text = "Your query returned: "+row[query]+"."
    return xml(text)

def xml(text):
    return('<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message>'+text+'</Message></Response>')

def comparetxt(text1, text2):
    return text1.upper()==text2.upper()
