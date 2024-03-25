import json
import random

with open("participants.json", "r") as file:
    data = json.load(file)

for item in data:
    item["visitedArr"] = {}
    item["paired"] = False

def createPairings(names):
    dict = names

    print(type(dict))

    pairings = []
    for item in dict:
        rand = random.randint(1,len(dict)-1)
        while(not item["paired"]):
            if((not dict[rand]["name"] in item["visitedArr"]) and dict[rand]["department"] != item["department"] and not dict[rand]["paired"]):
                item["paired"] = True
                dict[rand]["paired"] = True
                pairings.append((item["name"], dict[rand]["name"]))
            else:
                if(rand < len(dict)-1):
                    rand += 1
                else:
                    rand = 0
    return pairings

pairings = createPairings(data)

#create pairings
output = ""
table_count = 1
count = 0

for item in pairings:
    print(item[0], item[1])

for i in range (0, len(pairings)-2, 2):
    output += "<header>Table" + str(table_count) + "</header>"
    html_content = '''

    <table>
        <thead>
        <tr>
            <th>Name</th>
        </tr>
        <tr>
            <td>##PARTICIPANT1##</td>
        </tr>
        <tr>
            <td>##PARTICIPANT2##</td>
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
    html_content = html_content.replace("##PARTICIPANT1##", pairings[i][0])
    html_content = html_content.replace("##PARTICIPANT2##", pairings[i][1])
    html_content = html_content.replace("##PARTICIPANT3##", pairings[i+1][0])
    html_content = html_content.replace("##PARTICIPANT4##", pairings[i+1][1])
    output += html_content
    table_count +=1

with open('output.txt', 'w') as file:
    # Write the string to the file
    file.write(output)


print("Blakeblake".replace("Blake", "fishclear"))