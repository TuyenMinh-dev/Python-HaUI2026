def dsach():
    ds_sv = [
        {"id": "SV01", "ten": "Nguyen Van A", "diem_cc": 8.0, "diem_kt":8.5, "diem_thi":9.0},
        {"id": "SV02", "ten": "Nguyen Van B", "diem_cc": 8.1, "diem_kt":5, "diem_thi":10.0},
        {"id": "SV03", "ten": "Nguyen Van B", "diem_cc": 8.2, "diem_kt":7, "diem_thi":6.0},
        {"id": "SV04", "ten": "Nguyen Van C", "diem_cc": 8.5, "diem_kt":8, "diem_thi":4.0},
        {"id": "SV05", "ten": "Nguyen Van E", "diem_cc": 8.9, "diem_kt":5.8, "diem_thi":3.0},
    ]
    return ds_sv

def nhap_dl():
    danh_sach = []
    while True:
        try:
            n = int(input("Nhap so luong sinh vien muon them vao danh sach: "))
            if n > 0:
                break;
            print("Vui long nhap so lon 0")
        except ValueError:
            print("Vui long nhap vao mot so")
    for i in range(n):
        print(f"Nhap thong tin cho sinh vien thu {i+1} : ")
        ma_sv = input("Ma sinh vien: ")
        ten = input("Ten sinh vien: ")
        cc = nhap_diem("Nhap diem chuyen can: ")
        kt = nhap_diem("Nhap diem kiem tra: ")
        thi = nhap_diem("Nhap diem thi: ")
        danh_sach.append(
            {
                "id": ma_sv,
                "ten": ten,
                "diem_cc": cc,
                "diem_kt": kt,
                "diem_thi": thi,
            }
        )
    return danh_sach
    
def tinh_diem_tk(sv):
    return 0.1 * sv["diem_cc"] + 0.3 * sv["diem_kt"] + 0.6 * sv["diem_thi"]

def xep_loai(diem_tk):
    if diem_tk >= 8.5 and diem_tk <=10:
        return "Gioi"
    elif diem_tk >= 7.0:
        return "Kha"
    elif diem_tk >= 5.5:
        return "Trung binh"
    else:
        return "Yeu"

def cap_nhat(ds_sv):
        for sv in ds_sv:
           sv["diem_tk"] = round(tinh_diem_tk(sv),2)
           sv["xep_loai"] = xep_loai(sv["diem_tk"])
        return ds_sv

def hien_thi_list(ds_sv,tieu_de):
    print(f"\n {tieu_de}")
    for sv in ds_sv:
        print(f"{sv['id']} - {sv['ten']} | Tong ket: {sv['diem_tk']:.2f} | Xep loai: {sv['xep_loai']}")

def hien_thi_dict(ds,tieu_de):
    print(f"\n {tieu_de}")
    for ma, diem in ds.items():
        print(f"Ma sv:  {ma} | Tong ket: {diem}")

def sx_giam_dan(ds_sv):
    return sorted(ds_sv, key= lambda sv : sv["diem_tk"], reverse=True)

def nhap_diem(tieu_de_nhap):
    while True:
        try:
            a = float(input(tieu_de_nhap))
            if a >= 0 and a <= 10:
                break;
            print("Diem phai nam trong khoang tu 0 den 10")
        except ValueError:
            print("Vui long nhap vao mot so")    

    return a
    

def tao_list(ds_sv):
    return [sv for sv in ds_sv if sv["diem_tk"] >=5.5 ]

def tao_dict(ds_sv):
    return {sv["id"]: sv["diem_tk"] for sv in ds_sv}

def tim_max(ds_sv):
    return max(ds_sv, key= lambda sv:sv["diem_tk"])

def thong_ke_xep_loai(ds_sv):
    thong_ke = {}
    for sv in ds_sv:
        loai = sv["xep_loai"]
        thong_ke[loai] = thong_ke.get(loai,0) + 1
    return thong_ke

def main():
    danh_sach = nhap_dl()
    danh_sach = cap_nhat(danh_sach)

    hien_thi_list(danh_sach,"Thong tin sinh vien sau khi cap nhap nhu sau: ")

    danh_sach = sx_giam_dan(danh_sach)
    hien_thi_list(danh_sach,"Sap xep theo diem tong ket giam dan: ")

    list_tm = tao_list(danh_sach)
    hien_thi_list(list_tm,"Danh sach sinh vien co diem tk >= 5.5 la: ")

    dict_tm = tao_dict(danh_sach)
    hien_thi_dict(dict_tm,"Tu dien chua cac sinh vien tmyc: ")

    thong_ke = thong_ke_xep_loai(danh_sach)
    print(f"\n Thong tin slg sinh vien theo xep loai: {thong_ke}")



if __name__ == "__main__":
    main()  



