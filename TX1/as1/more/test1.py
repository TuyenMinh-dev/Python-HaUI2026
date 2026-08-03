"""
BAI TAP: Quan ly diem sinh vien theo LOP
Cau truc du lieu: DICT BOC LIST
    { ten_lop : [ {sinh_vien_1}, {sinh_vien_2}, ... ] }
    -> Key la ten lop, value la 1 LIST cac dict sinh vien cua lop do.
"""

import csv


# ============================================================
# YEU CAU 1: Doc du lieu tu file CSV -> to chuc thanh dict boc list
# ============================================================
def doc_du_lieu_tu_file(duong_dan):
    """Doc file CSV (lop,id,ten,diem_cc,diem_kt,diem_thi) -> tra ve dict boc list.
    Neu file khong ton tai, bao loi va tra ve dict rong de chuong trinh
    co the chuyen sang nhap tay thay the."""
    du_lieu = {}
    try:
        with open(duong_dan, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)   # tu dong doc dong dau tien lam ten cot
            for dong in reader:
                lop = dong["lop"]
                sv = {
                    "id": dong["id"],
                    "ten": dong["ten"],
                    "diem_cc": float(dong["diem_cc"]),
                    "diem_kt": float(dong["diem_kt"]),
                    "diem_thi": float(dong["diem_thi"]),
                }
                # Neu lop chua co trong dict thi tao list rong truoc
                if lop not in du_lieu:
                    du_lieu[lop] = []
                du_lieu[lop].append(sv)
        print(f"Da doc thanh cong du lieu tu file '{duong_dan}'.")
    except FileNotFoundError:
        print(f"Khong tim thay file '{duong_dan}'. Vui long kiem tra lai duong dan.")
    except (ValueError, KeyError) as loi:
        print(f"File co du lieu khong dung dinh dang: {loi}")
    return du_lieu


# ============================================================
# Nhap tay thay the (dung khi khong co file / muon them du lieu)
# ============================================================
def nhap_diem(nhan):
    """Nhap 1 diem so 0-10 tu ban phim, tu dong bat loi (yeu cau xu ly ngoai le)."""
    while True:
        try:
            diem = float(input(nhan))
            if diem < 0 or diem > 10:
                print("Diem phai nam trong khoang 0 - 10, nhap lai.")
                continue
            return diem
        except ValueError:
            print("Du lieu khong phai la so, nhap lai.")


def nhap_du_lieu_tay():
    """Nhap tay du lieu sinh vien theo tung lop, tra ve dict boc list."""
    du_lieu = {}
    so_lop = int(input("Nhap so luong lop: "))
    for _ in range(so_lop):
        ten_lop = input("\nNhap ten lop: ")
        so_sv = int(input(f"Nhap so sinh vien cua lop {ten_lop}: "))
        danh_sach_lop = []
        for i in range(so_sv):
            print(f"-- Sinh vien thu {i + 1} cua lop {ten_lop} --")
            sv = {
                "id": input("Ma SV: "),
                "ten": input("Ho ten: "),
                "diem_cc": nhap_diem("Diem chuyen can: "),
                "diem_kt": nhap_diem("Diem kiem tra: "),
                "diem_thi": nhap_diem("Diem thi: "),
            }
            danh_sach_lop.append(sv)
        du_lieu[ten_lop] = danh_sach_lop
    return du_lieu


# ============================================================
# YEU CAU 2: Tinh diem tong ket + xep loai (dung lai logic bai 1)
# ============================================================
def tinh_diem_tong_ket(sv):
    return round(0.1 * sv["diem_cc"] + 0.3 * sv["diem_kt"] + 0.6 * sv["diem_thi"], 2)


def xep_loai(diem_tk):
    if diem_tk >= 8.5:
        return "Gioi"
    elif diem_tk >= 7.0:
        return "Kha"
    elif diem_tk >= 5.5:
        return "Trung binh"
    else:
        return "Yeu"


def cap_nhat_toan_truong(du_lieu):
    """Duyet qua tung LOP (key), roi duyet qua tung SINH VIEN trong list (value)."""
    for ten_lop, danh_sach_sv in du_lieu.items():   # ten_lop: key, danh_sach_sv: value (list)
        for sv in danh_sach_sv:                      # duyet tiep vao trong list
            sv["diem_tk"] = tinh_diem_tong_ket(sv)
            sv["xep_loai"] = xep_loai(sv["diem_tk"])
    return du_lieu


# ============================================================
# YEU CAU 3: In danh sach sinh vien theo tung lop
# ============================================================
def in_theo_lop(du_lieu):
    for ten_lop, danh_sach_sv in du_lieu.items():
        print(f"\n=== Lop {ten_lop} ({len(danh_sach_sv)} sinh vien) ===")
        for sv in danh_sach_sv:
            print(f"  {sv['id']} - {sv['ten']:<20} | Tong ket: {sv['diem_tk']:.2f} | Xep loai: {sv['xep_loai']}")


# ============================================================
# YEU CAU 4: sorted() + lambda -> sap xep sinh vien TRONG TUNG LOP
# ============================================================
def sap_xep_tung_lop(du_lieu):
    """Tra ve dict boc list MOI, moi lop da duoc sap xep giam dan theo diem_tk."""
    du_lieu_da_sx = {}
    for ten_lop, danh_sach_sv in du_lieu.items():
        du_lieu_da_sx[ten_lop] = sorted(danh_sach_sv, key=lambda sv: sv["diem_tk"], reverse=True)
    return du_lieu_da_sx


# ============================================================
# YEU CAU 5: Dictionary comprehension -> {ten_lop: diem_trung_binh}
# ============================================================
def diem_trung_binh_theo_lop(du_lieu):
    return {
        ten_lop: round(sum(sv["diem_tk"] for sv in danh_sach_sv) / len(danh_sach_sv), 2)
        for ten_lop, danh_sach_sv in du_lieu.items()
    }


# ============================================================
# YEU CAU 6: List comprehension -> lop co diem trung binh >= 6.5
# ============================================================
def loc_lop_dat(diem_tb_theo_lop):
    return [lop for lop, diem_tb in diem_tb_theo_lop.items() if diem_tb >= 6.5]


# ============================================================
# YEU CAU 7: Lop cao nhat + sinh vien cao nhat TOAN TRUONG
# ============================================================
def tim_lop_cao_nhat(diem_tb_theo_lop):
    # max tren dict: dung .items() de lay ca (key, value), so sanh theo value
    return max(diem_tb_theo_lop.items(), key=lambda cap: cap[1])


def tim_sinh_vien_cao_nhat_toan_truong(du_lieu):
    sv_cao_nhat = None
    for danh_sach_sv in du_lieu.values():      # chi can value (list), khong can ten lop
        for sv in danh_sach_sv:
            if sv_cao_nhat is None or sv["diem_tk"] > sv_cao_nhat["diem_tk"]:
                sv_cao_nhat = sv
    return sv_cao_nhat


# ============================================================
# YEU CAU 8: Thong ke xep loai TOAN TRUONG (gop tat ca cac lop)
# ============================================================
def thong_ke_toan_truong(du_lieu):
    thong_ke = {}
    for danh_sach_sv in du_lieu.values():
        for sv in danh_sach_sv:
            loai = sv["xep_loai"]
            thong_ke[loai] = thong_ke.get(loai, 0) + 1
    return thong_ke


# ============================================================
# YEU CAU 9 + 10: Ghi ket qua ra file (co xu ly ngoai le)
# ============================================================
def ghi_ket_qua_ra_file(du_lieu, diem_tb_theo_lop, thong_ke, duong_dan="ket_qua.txt"):
    try:
        with open(duong_dan, mode="w", encoding="utf-8") as f:
            f.write("BAO CAO KET QUA HOC TAP\n")
            f.write("=" * 50 + "\n")

            for ten_lop, danh_sach_sv in du_lieu.items():
                f.write(f"\nLop {ten_lop} (diem TB: {diem_tb_theo_lop[ten_lop]:.2f})\n")
                f.write("-" * 50 + "\n")
                for sv in danh_sach_sv:
                    f.write(f"{sv['id']} - {sv['ten']:<20} | Tong ket: {sv['diem_tk']:.2f} | {sv['xep_loai']}\n")

            f.write("\n" + "=" * 50 + "\n")
            f.write("THONG KE TOAN TRUONG\n")
            for loai, so_luong in thong_ke.items():
                f.write(f"  {loai}: {so_luong} sinh vien\n")

        print(f"Da ghi ket qua ra file '{duong_dan}' thanh cong.")
    except PermissionError:
        print(f"Khong co quyen ghi vao file '{duong_dan}'.")
    except OSError as loi:
        print(f"Loi khi ghi file: {loi}")


# ============================================================
# CHUONG TRINH CHINH
# ============================================================
def main():
    # Yeu cau 1: doc du lieu tu file, neu khong co thi cho nhap tay
    du_lieu = doc_du_lieu_tu_file("sinhvien.csv")
    if not du_lieu:   # dict rong (doc file that bai) -> chuyen sang nhap tay
        print("Chuyen sang che do nhap tay.")
        du_lieu = nhap_du_lieu_tay()

    # Yeu cau 2: cap nhat diem tong ket + xep loai
    du_lieu = cap_nhat_toan_truong(du_lieu)

    # Yeu cau 3: in theo tung lop
    in_theo_lop(du_lieu)

    # Yeu cau 4: sap xep giam dan trong tung lop
    du_lieu_sx = sap_xep_tung_lop(du_lieu)
    print("\n\n########## SAU KHI SAP XEP GIAM DAN TUNG LOP ##########")
    in_theo_lop(du_lieu_sx)

    # Yeu cau 5: diem trung binh theo lop (dict comprehension)
    diem_tb_theo_lop = diem_trung_binh_theo_lop(du_lieu)
    print(f"\nDiem trung binh theo lop: {diem_tb_theo_lop}")

    # Yeu cau 6: loc lop dat (list comprehension)
    lop_dat = loc_lop_dat(diem_tb_theo_lop)
    print(f"Cac lop co diem TB >= 6.5: {lop_dat}")

    # Yeu cau 7: lop cao nhat + sinh vien cao nhat toan truong
    ten_lop_cao_nhat, diem_lop_cao_nhat = tim_lop_cao_nhat(diem_tb_theo_lop)
    print(f"\nLop co diem TB cao nhat: {ten_lop_cao_nhat} ({diem_lop_cao_nhat:.2f})")

    sv_cao_nhat = tim_sinh_vien_cao_nhat_toan_truong(du_lieu)
    print(f"Sinh vien cao nhat toan truong: {sv_cao_nhat['id']} - {sv_cao_nhat['ten']} - {sv_cao_nhat['diem_tk']:.2f}")

    # Yeu cau 8: thong ke xep loai toan truong
    thong_ke = thong_ke_toan_truong(du_lieu)
    print(f"\nThong ke xep loai toan truong: {thong_ke}")

    # Yeu cau 9 + 10: ghi ket qua ra file (co xu ly ngoai le)
    ghi_ket_qua_ra_file(du_lieu, diem_tb_theo_lop, thong_ke, "ket_qua.txt")


if __name__ == "__main__":
    main()