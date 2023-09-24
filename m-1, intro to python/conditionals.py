# in , not, not in , is , is not
# >, <, >= ,<=, ==, !==


a=4
boss=False
if a>5:
    print('5 er besi')
    print('koto bshi k jne')
elif a>3:
    print('olpo boro')
elif a==2:
    print('2 er shoman')
else:
    print('choto choto')

# if boss is True:
#     print('lunch er por asen')
# else:
#     print('boss kaj hye jbe')
if boss is not True:
    print('lunch er por asen')
else:
    print('boss kaj hye jbe')

coin='head'
if coin == 'tail':
    print('batting')
    if 5>2 or boss != True:
        print('do something')
        if 8%2==0 and 5%2==1:
            print('even')