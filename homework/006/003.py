# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

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

names=input('Имена сотрудников, через запятую: ').split(',')
#names=["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

print(employeeDic(names))

    