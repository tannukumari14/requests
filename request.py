import os
# print(dir(os))
print(os.getcwd())
import requests
import json
#### get help us to take data from the url
meraki_data = requests.get("https://api.merakilearn.org/courses")
data = meraki_data.json()
### dump data in json file
with open("meraki_data.json","w") as f:
    json.dump(data,f,indent=4)
def func():
    serial_no1=1                                
    for i in range(len(data)):
        print(serial_no1,data[i]["name"],data[i]["id"])
        serial_no1=serial_no1+1
func()
## load data in json file
def func_hi():
    i=0
    for k,v in data[i].items():
        if k=="name":
            print(i+1,v,":",data[i]["id"])
    choose_cource=int(input("which course do you want select: "))
    choose_cource1=choose_cource-1
    print(data[choose_cource1]["name"])
    id_data=data[choose_cource1]["id"]
func_hi()

def fun():
    previous_next=input("if you want  go next type N,if you want to go previous type P:   ")
    if previous_next=="P":
        serial_number = 1
        for i in data:
            print(serial_number,":-",i["name"], i["id"])
            serial_number=serial_number+1
    elif previous_next=="N":
        i=0
        while i<len(data):
            i=i+1
        print(data)
fun()
def my_func():
    js_var=int(input("enter the course:"))
    print(data[js_var-1]["name"])
    id_var=data[js_var-1]["id"]
    var_1=requests.get("http://api.merakilearn.org/courses/"+str(id_var)+"/exercises")
    k_m=var_1.json()
    with open("khushbu.no1.json","w")as f:
        file_1=json.dump(k_m,f,indent=4)
    serial_no=1
    list_1=[]
    list_2=[]
    for j in k_m['course']['exercises']:
        if j ['parent_exercise_id']==None:
            print(serial_no,j["name"])
            print("  ",serial_no,j['slug'])
            serial_no+=1
            list_1.append(j)
            list_2.append(j)
            continue
        if j['parent_exercise_id']==j['id']:
            print(serial_no,j["name"])
            serial_no+=1
            list_1.append(j)
        for s in k_m['course']['exercises']:
            if j['parent_exercise_id']!=j["id"]:
                # print(ser_var,j[name])
                serial_no+=1
                list_2.append(s)
                break
    with open ("question.json","w")as f:
        json.dump(data,f,indent=3)
        js_var=int(input("enter the course:"))
        print(data[js_var-1]["name"])
        id_var=data[js_var-1]["id"]
        var_1=requests.get("http://api.merakilearn.org/courses/"+str(id_var)+"/exercises")
        k_m=var_1.json()

## dumps name data
topic=input("enter the previce or next (p/n):")
if topic=="p":
    ser_var=1
    for i in data:
        print(ser_var,i["name"],i["id"])
        ser_var+=1
    js_var=int(input("enter the course:"))
    print(data[js_var-1]["name"])
    id_var=data[js_var-1]["id"]
    var_1=requests.get("http://api.merakilearn.org/courses/"+str(id_var)+"/exercises")
    data=var_1.json()
    with open("tanu.no1.json","w")as f:
        fle_1=json.dump(var_1,f,indent=4)
        serial_no=1
        list_1=[]
        list_2=[]
    for j in var_1['course']['exercises']:
        if j ['parent_exercise_id']==None:
            print(serial_no,j["name"])
            print(" ",serial_no,j['slug'])
            serial_no+=1
            list_1.append(j)
            list_2.append(j)
            continue
        if j['parent_exercise_id']==j['id']:
            print(ser_var,j["name"])
            serial_no+=1
            list_1.append(j)
        for s in var_1['course']['exercises']:
            if j['parent_exercise_id']!=j["id"]:
                print(ser_var,j["name"])
                serial_no+=1
            list_2.append(s)
            break