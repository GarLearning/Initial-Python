name = str(input('type your name: ')).lower()
if name == 'gabriel':
    print('\033[7;40mohh, your name s handsome!!\033[m')
elif name == 'maria' or name == 'sara' or name == 'alice':
    print('\033[1;36myour name s petty, and very popular in brasil\033[m')
elif name in 'evelynn riven morgana lux':
    print('\033[34mlmfao, your your name s from legue of legends\033[m')
else:
    print('\033[31myour name s very normal!\033[m')
print('\033[4;33mhave a good day, {}!!!\033[m'.format(name))