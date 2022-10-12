# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# out

# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']}, 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}

def employeeDic(names):
    names.sort()
    preKeys=[i[0] for i in names]
    keys=[]
    for i in range(len(preKeys)):
        if not preKeys[i] in keys:
            keys.append(preKeys[i])
    dic={}
    for i in range(len(keys)):
        dic[keys[i]]=[]
    for key in range(len(keys)):
        for name in range(len(names)):
            if names[name][0]==keys[key]:
                dic[keys[key]].append(names[name])
    return dic

def employeeDicToDic(namesSurnames):
    for i in range(len(namesSurnames)):
        namesSurnames[i]=namesSurnames[i].split()
    preKeys=[]
    for i in range(len(namesSurnames)):
        preKeys.append(namesSurnames[i][1][0])
    preKeys.sort()
    sKeys=[]
    for i in range(len(preKeys)):
            if not preKeys[i] in sKeys:
                sKeys.append(preKeys[i])
    dic={}
    for i in range(len(sKeys)):
        dic[sKeys[i]]=[]
    for key in range(len(sKeys)):
        for nameSurname in range(len(namesSurnames)):
            if namesSurnames[nameSurname][1][0]==sKeys[key]:
                dic[sKeys[key]].append((" ".join(namesSurnames[nameSurname])))
    for i in dic:
        dic[i]=employeeDic(dic[i])
    return(dic)

namesSurnames=["Иван Сергеев", "Инна Серова", "Петр Алексеев","Илья Иванов", "Анна Савельева", "Юнона Ветрякова","Борис Аркадьев", "Антон Серов", "Павел Анисимов"]

print(employeeDicToDic(namesSurnames))