import json
import random

#------------------functions---------------------#

def f(x):
    x["paired"] = False
    return x 

def g(x):
    x["visitedArr"] = []
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
            output = output.replace("#TABLE#", str(table_count))
            table_count += 1
        elif(i%2==1):
            output = output.replace("##PARTICIPANT3##", pairings[i][0])
            output = output.replace("##PARTICIPANT4##", pairings[i][1])

        i+=1
    return output

def removeIndex(objects, n):

    toRemove = objects[int(n)]

    del objects[int(n)]

    newData = json.dumps(objects, indent=4)

    print(newData)

    with open('participants.json', 'w') as file:
        file.write(newData)
    file.close

    return objects

def resetVisitedArr(objects):
    resetArr = [g(x) for x in objects]

    newData = json.dumps(resetArr, indent=4)

    with open('participants.json', 'w') as file:
        file.write(newData)
    file.close

    return resetArr


def writeFile(string):
    with open('output.txt', 'w') as file:
        file.write(output)
    file.close

def addPerson(names, name):
    names.append(name)

    newData = json.dumps(names, indent=4)

    with open('participants.json', 'w') as file:
        file.write(newData)
    file.close

def shuffle(list):
    for i in range(0, len(list)):
        rand = random.randint(1,len(list)-1)
        x = list[rand]
        list[rand] = list[i]
        list[i] = x   
    return list     

#------------------script---------------------#

with open("participants.json", "r") as file:
    data = json.load(file)
file.close

for item in data:
    item["visitedArr"] = []
    item["paired"] = False

data = resetVisitedArr(data)

breaker = ""
while(breaker != "4"):
    breaker = input("1) generate HTML\n2) Add Participant\n3) Remove Participant\n4) end\n>")
    match breaker:
        case "1":
            data = shuffle(data)
            pairings = createPairings(data)
            for item in pairings:
                print(item[0], item[1])
            for item in data:
                print(item)
            output = createHtml(pairings)
            with open('output.txt', 'w') as file:
                writeFile(output)
            file.close
        case "2":
            newPerson = {}
            newPerson["name"] = input("First and last name: ")
            newPerson["department"] = input("department: ")
            newPerson["visitedArr"] = []
            newPerson["paired"] = False
            addPerson(data, newPerson)

        case "3":
            count = 0
            for item in data:
                print(count, ": ", item["name"])
                count+=1
            index = input("which name should be removed: ")
            removeIndex(data, index)
        case "4":
            break
