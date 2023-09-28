balane = 3000

def buy(item, price):
    # you cannot modify global variable in local scope but using global keyword you can modify that
    print('balance inside in the function', balane)


buy('sunglass', 1000)