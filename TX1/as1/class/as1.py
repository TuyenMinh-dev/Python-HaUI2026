def nhap():
    my_dict = {}
    
    while True:
        try:
            n = int(input("Nhap so luong mat hang (n): "))
            if n > 0:
                break
            print("Vui long nhap so lon hon 0!")
        except ValueError:
            print("Loi: Vui long chi nhap so nguyen!")

    for i in range(n):
        ma = input(f"Nhap ma hang thu {i + 1}: ").strip()
        
        while True:
            try:
                slg = int(input(f"Nhap so luong cua mat hang co ma '{ma}': "))
                if slg >= 0:
                    break
                print(f"So luong cua '{ma}' khong duoc am!")
            except ValueError:
                print(f"Loi: Vui long chi nhap so nguyen cho so luong cua '{ma}'!")
                
        my_dict[ma] = slg
    return my_dict

def dict2():
    nha_cc = {
        "001": "ABC",
        "002": "XYZ",
        "003": "JQK",
    }    
    return nha_cc

def hien_thi(d, tieu_de):
    print(f"\n{tieu_de}")
    for ma, value in d.items():
        print(f"-> Mã hàng: {ma:<6} | Giá trị: {value}")

def check_update(d):
    target_code = "H001"
    if target_code in d:
        d[target_code] = 200
        print(f"Da tim thay hang hoa co ma la '{target_code}', cap nhat thanh cong so luong thanh 200.")
    else:
        while True:
            try:
                new_slg = int(input(f"\nKhong tim thay '{target_code}'. Nhap so luong cho ma hang nay: "))
                if new_slg >= 0:
                    break
                print("So luong khong duoc am!")
            except ValueError:
                print("Loi: Vui long chi nhap so nguyen!")
                
        d[target_code] = new_slg
        print(f"Da bo sung du lieu cho ma hang '{target_code}' voi so luong {new_slg}.")
    return d

def delete_items(d):
    ma_xoa = [ma for ma, sl in d.items() if sl == 0]
    for ma in ma_xoa:
        del d[ma]
    if ma_xoa:
        print(f"\n[Thong bao] Da xoa cac ma hang co so luong bang 0: {', '.join(ma_xoa)}")
    else:
        print("\n[Thong bao] Khong co ma hang nao co so luong bang 0 de xoa.")
    return d

def change_to_list(d):
    ds_ma = list(d.keys())
    ds_slg = list(d.values())
    return ds_ma, ds_slg

def in_phan_tu(list1, list2):
    limit_ma = len(list1)
    limit_slg = len(list2)
    
    if limit_ma >= 3:
        print(f"\n3 phan tu dau cua list ma hang la: {list1[:3]}")
    else:
        print(f"\nKhong du phan tu de in 3 phan tu dau cho list ma hang (Hien co: {limit_ma})")

    if limit_slg >= 3:
        print(f"3 phan tu cuoi cua list so luong la: {list2[-3:]}")
    else:
        print(f"Khong du phan tu de in 3 phan tu cuoi cho list so luong (Hien co: {limit_slg})") 

def main():
    tu_dien_1 = nhap()

    tu_dien_2 = dict2()
    hien_thi(tu_dien_2, "--- TU DIEN 2 (Nha cung cap) ---")

    tu_dien_1 = check_update(tu_dien_1)
    hien_thi(tu_dien_1, "--- TU DIEN 1 (Sau khi cap nhat H001) ---")

    tu_dien_1 = delete_items(tu_dien_1)
    hien_thi(tu_dien_1, "--- TU DIEN 1 (Sau khi xoa hang hoa co sl = 0) ---")

    ds_ma, ds_slg = change_to_list(tu_dien_1)
    in_phan_tu(ds_ma, ds_slg)

if __name__ == "__main__":
    main()