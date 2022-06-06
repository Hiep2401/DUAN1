from sqlite3 import InterfaceError # Import thu vien can thiet
import select_device # ket noi den file ban dau
options = """ 
    Xin moi ban (Welcome to Netmiko)!
    1 - Xem Interface
    2 - Cau hinh Interface
    3 - Cau hinh Vlan
    4 - cau hinh Loopback
    5 - Thoat chuong trinh

    """
    # Cac tuy chon lay tu cac ham file select_device.py
while True:
    print(options)
    opt = input("Xin moi lua chon: \n")
    if opt == '1':
        select_device.Xem_Interface()
    elif opt == '2':
        select_device.Cauhinh_Interface()
    elif opt == '3':
        select_device.Cauhinh_Vlan()
    elif opt == '4':
        select_device.Cauhinh_Loopback()
    elif opt == '5':
        break
    else:
        print('Nhap lai: \n')
