from netmiko import ConnectHandler # Import thu vien Netmiko
import getpass # Import thu vien de bao mat

# Cac lenh in ra man hinh
print('\n Chao moi den voi Netmiko \n Vui long nhap thong tin \n')
ip_input = input('Nhap ip cua device can xem và cau hinh: ') 
user_name = input('Nhap username SSH vao: ')
pass_word = getpass.getpass('Nhap password SSH vao: \n')

# Khai bao thong tin thiet bi
device = {
        'device_type' : 'cisco_ios', # Loai thiet bi
        'ip' : ip_input, #dia chi ip host
        'username' : user_name, #username ssh
        'password' : pass_word, #password ssh
        'secret' : 'vnpro@321' #enable password
        }

con_nect = ConnectHandler(**device) # Ket noi den thiet bi
con_nect.find_prompt()

print('Ket noi thanh cong thiet bi')


# Ham dung de xem thong tin cong interface
def Xem_Interface():
    con_nect = ConnectHandler(**device)
    print(con_nect.send_command('show ip int brief'))


# Ham dung de cau hinh cac cong interface
def Cauhinh_Interface():
    con_nect = ConnectHandler(**device)
    con_nect.enable()
    dict_int = {}
    while True:
        end = input('Nhap Enter để tiếp tục hoặc end kết thúc. \n')
        if end != 'end':
            int = input('Nhap cong Interface: \t')
            ip_int = input('Nhap IP + Subnet mask: \t')
            dict_int.setdefault(int, ip_int)
        else:
            break
    for a in dict_int:
        int_ip = ["interface" +a, "no shut", "ip address "+dict_int[a], "exit"]
        print(con_nect.send_config_set(int_ip))

# Ham dung de cau hinh Vlan cho Switch
def Cauhinh_Vlan():
    con_nect = ConnectHandler(**device)
    con_nect.enable()
    dict_int = {}
    while True:
        end = input('Nhap Enter để tiếp tục hoặc end kết thúc. \n')
        if end != 'end':
            int = input('Nhap Vlan cần tạo: \t')
            ip_int = input('Nhap ten Vlan: \t')
            dict_int.setdefault(int, ip_int)
        else:
            break
    for a in dict_int:
        int_ip = [""+a, "name "+dict_int[a]]
        print(con_nect.send_config_set(int_ip))


# Ham dung de tao loopback
def Cauhinh_Loopback():
    con_nect = ConnectHandler(**device)
    con_nect.enable()
    dict_int = {}
    while True:
        end = input('Nhap Enter để tiếp tục hoặc end kết thúc. \n')
        if end != 'end':
            int = input('Nhap Loopback cần tạo: \t')
            ip_int = input('Nhap Ip + Subnet mask: \t')
            dict_int.setdefault(int, ip_int)
        else:
            break
    for a in dict_int:
        int_ip = ["interface " +a, "ip address "+dict_int[a], "exit"]
        print(con_nect.send_config_set(int_ip))
