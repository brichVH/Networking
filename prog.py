import json
import random

#------------------functions---------------------#

def f(x):
    x["paired"] = False
    return x 


def createPairings(names):
    dict = [f(x) for x in names]

    pairings = []
    for item in dict:
        count = 0
        rand = random.randint(1,len(dict)-1)
        while(not item["paired"]):
            count+=1
            if((not dict[rand]["name"] in item["visitedArr"]) and dict[rand]["department"] != item["department"] and not dict[rand]["paired"]):
                item["paired"] = True
                dict[rand]["paired"] = True
                pairings.append((item["name"], dict[rand]["name"]))
                item["visitedArr"].append(dict[rand]["name"])
                dict[rand]["visitedArr"].append(item["name"])
            elif(count>100):
                pairings.append((item["name"], ""))
                item["paired"] = True
            else:
                if(rand < len(dict)-1):
                    rand += 1
                else:
                    rand = 0
    return pairings

def createHtml(pairings):
    output = ""
    table_count = 1
    count = 0

    i=0
    while(i<len(pairings)):
        if(i%2==0):
            output += "<header>Table " + str(table_count) + "</header>"
            html_content = '''

            <table>
                <thead>
                <tr>
                    <th> Table #TABLE# - Group 1</th>
                </tr>
                <tr>
                    <td>##PARTICIPANT1##</td>
                </tr>
                <tr>
                    <td>##PARTICIPANT2##</td>
                </tr>
            </table>

            <div>&nbsp;</div>

            <table>
                <thead>
                <tr>
                    <th>Table #TABLE# - Group 2</th>
                </tr>
                <tr>
                    <td>##PARTICIPANT3##</td>
                </tr>
                <tr>
                    <td>##PARTICIPANT4##</td>
                </tr>
            </table>

            <div>&nbsp;</div>
            '''
            output += html_content
            output = output.replace("##PARTICIPANT1##", pairings[i][0])
            output = output.replace("##PARTICIPANT2##", pairings[i][1])
            if(i == (len(pairings)-1)):
                output = output.replace("##PARTICIPANT3##", "")
                output = output.replace("##PARTICIPANT4##", "")
            table_count += 1
        elif(i%2==1):
            output = output.replace("##PARTICIPANT3##", pairings[i][0])
            output = output.replace("##PARTICIPANT4##", pairings[i][1])

        output = output.replace("#TABLE#", str(table_count))
        i+=1
    return output

def removeIndex(objects, n):
    del objects[n]
    return objects

def writeFile(string):
    with open('output.txt', 'w') as file:
        file.write(output)

def addPerson(names, name):
    names.append(name)

def shuffle(list):
    for i in range(0, len(list)):
        rand = random.randint(1,len(list)-1)
        x = list[rand]
        list[rand] = list[i]
        list[i] = x   
    return list     

#------------------script---------------------#
        
x = [1,2,3,4,5]

x = shuffle(x)

for item in x:
    print(item)

with open("participants.json", "r") as file:
    data = json.load(file)

for item in data:
    item["visitedArr"] = []
    item["paired"] = False

breaker = ""
while(breaker != "4"):
    breaker = input("1) generate HTML\n2)Add Participant\n3)Remove Participant\n4)end\n>")
    match breaker:
        case "1":
            data = shuffle(data)
            pairings = createPairings(data)
            for item in pairings:
                print(item[0], item[1])
            for item in data:
                print(item)
            output = createHtml(pairings)
            writeFile(output)
        case "2":
            newPerson = {}
            newPerson["name"] = input("First and last name: ")
            newPerson["department"] = input("department: ")
            newPerson["visitedArr"] = []
            newPerson["paired"] = False
            data.append(newPerson)
        case "3":
            for idx, item in pairings:
                print(idx, item[0], item[1])
            index = input("which name should be removed")
            removeIndex(data, index)
        case "4":
            break
