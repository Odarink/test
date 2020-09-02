def di_space(x:dict,namespace:str):
    """Функция возвращает значение по заданному 
    ключу из словаря. Для поиска необходимого namespace."""
    return x[namespace]

def di_search(path:dict, find:str):
    """ Поиск области видимости в общей структуре словарей 
    состовляющих области видимости именных полей. 
    Поиск в глубину (DFS)."""
    if find not in path:
        for i in path:
            return di_search(di_space(path,i),find)
    return di_space(path,find)
        
def di_get(path:dict,find:str,var:str,name = 'None'):
    """Функция для вывода области видимости введенного 
    обьекта по заданной области видимости."""      
    if find not in path:
        name = str(di_space(dict(path),var) if var in path else name)
        for i in path:
            return di_get(di_space(path,i),find,var,name)
    name = di_space(path,var) if var in path else name
    name = di_space(di_space(path,find),var) if var in di_space(path,find) else name
    return name
        
            

def res_di():
    """ Функция для определения области видимости обьектов,
 На вход поступает кол-во операций и операции обособленные
 вводом строки с клавиатуры.
 create - создание новой области видимости - var_nae внутри 
 namespace - nasp.
 add - обьявление обьекта - var_name в заданной области 
 видимости nasp.
 get - вывод области видимости вызываемого обьекта - var_name
 в заданной области видимости - nasp."""
    numbers = int(input())
    di_name = {'global':{}}
    for i in range(numbers):
        func, nasp, var_name = input().split()
        if func == 'create': 
            nasp,var_name = var_name,nasp
            di_search(di_name,nasp).update({var_name:{}})
        if func == 'add':
            di_search(di_name,nasp).update({var_name:nasp})
        if func == 'get':
            print(di_get(di_name,nasp,var_name,'None'))
    return di_name
        




a = res_di()
