import random

# 银行的库
names = {}
'''
{
    "张三":{address:"沙河北大桥桥底下",money:546,account:1a5sdf1af},
    "张三":{address:"沙河北大桥桥底下",money:546}
}
'''

# 开户行名称
bankName = "中国工商银行昌平支行"
# 欢迎页面的模板
welcome = '''
    -----------------------------------------
    -     欢迎来到中国工商银行账户管理系统     -
    -----------------------------------------
    -   1.开户                               -
    -   2.存钱                               -
    -   3.取钱                               -
    -   4.转账                               -
    -   5.查询                               -
    -   6.Bye!                               -
    ------------------------------------------
'''


def getRandom():
    li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0, len(li) - 1)]
        string = string + ch
    return string


# 银行的开户逻辑
def bank_addUser(account, username, password, money, country, province, street, door):
    # 1.判断是否已满
    if len(names) >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    if username in names:
        return 2
    # 3.开户
    names[username] = {
        "account": account,
        "username": username,
        "password": password,
        "money": money,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "bank_name": bank_name
    }
    return 1


# 开户操作
def addUser():
    username = input("请输入您的姓名：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的账户余额："))  # "123"  123
    print("下面请输入您的个人地址信息：")
    country = input("请输入您的国籍：")
    province = input("请输入您的省份：")
    street = input("请输入您的居住街道：")
    door = input("请输入您的门牌号：")
    account = getRandom()
    status = bank_addUser(account, username, password, money, country, province, street, door)
    if status == 1:
        print("恭喜开户成功！以下是您的个人信息：")
        info = '''
            ----------个人信息 【工商银行】--------
            用户名：%s,
            密码：%s,
            账号：%s,
            余额：%s,
            国家：%s,
            省份：%s,
            街道:%s,
            门牌号：%s
            开户行名称：%s
            ------------------------------------
        '''
        print(info % (username, password, account, money, country, province, street, door, bank_name))

    elif status == 2:
        print("对不起，您的账户已存在！请勿重复开户！")
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")


# 入口程序
while True:
    print(welcome)
    chose = input("请输入您的业务编号：")
    if chose == '1':
        addUser()
    elif chose == '2':
        pass
    elif chose == '3':
        pass
    elif chose == '4':
        pass
    elif chose == '5':
        pass
    elif chose == '6':

        break
    else:
        print("输入非法！别瞎弄！")
