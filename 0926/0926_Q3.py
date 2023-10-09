import re
def is_id_number():
    id=input("请输入你的身份证号：").strip()
    res=re.match("(^\d{15}$)|(^\d{17}([0-9]|x)$)",id)
    if res:
        print("身份证号合法")
    else:
        print("身份证号不合法")
is_id_number()