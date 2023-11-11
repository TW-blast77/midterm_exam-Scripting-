import json
def triangle_zhonxin(A, B, C) -> tuple:
    """
    計算一個三角形的重心
    Args:
        A(tuples): the coordinate of A point
        B(tuples): the coordinate of B point
        C(tuples): the coordinate of C point
    Return: 重心座標
    """
    X = (int(A[0]) + int(B[0]) + int(C[0])) / 3
    Y = (int(A[1]) + int(B[1]) + int(C[1])) / 3
    X = round(X)
    Y = round(Y)

    return (int(X), int(Y))
def read_json(file_name: str) -> dict:
    """
    讀取json檔案回傳一個字典

    Args:
        file_name (str): Json檔案的名子

    Returns:
        dict: 包含json的檔案(字典的格式)
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)
    

def print_json(data:dict) -> None :
    """
    讀取dictionary檔案，並輸出至螢幕上

    Args:
        data (dict): 型態為dict

    Returns:
        print: json.dumps(dict檔案,以鍵排序是True(默認是False),
        ensure_ascii全部以ASCII的型態解析並設定False(默認是True),
        indent是一個字符串(比如"\\t")設定為4,
        separators是(item_separator, key_separator)的元組可取出(',',': ")(默認None)。)
    """
    print(json.dumps(data,sort_keys=True,ensure_ascii=False,indent=4, separators=(',', ': ')))


def process_data(data: dict, discount: float) -> None :
    """
    將讀取的字典中每個菜品的價格打discount折數

    Args:
        data(dictionary) : 型態為dict, discount(打折數):型態為float 

    """
    for categories in data["categories"]:
        for item in categories["items"]:
            item_price = item["price"]
            item_price = round(item_price * discount)
            item["price"] = item_price

def write_json(data: dict, file_name: str) -> None :
    """
    將讀入的字典轉為檔案

    Args:
        data (dictionary): 字典檔案，型態為 dict
        file_name (str): 輸出 JSON 檔名，型態為 str

    """
    with open(file_name, 'w', encoding='utf-8') as json_file :
        json.dump(data, json_file, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
