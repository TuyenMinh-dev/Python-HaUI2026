import csv

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def doc_du_lieu_csv(filename):
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  

            for row in reader:
                try:
                    diem_chuyen_can = float(row[2])
                    diem_kiem_tra = float(row[3])
                    diem_thi = float(row[4])

                    students.append({
                        "ma_sv": row[0],
                        "ho_ten": row[1],
                        "diem_chuyen_can": diem_chuyen_can,
                        "diem_kiem_tra": diem_kiem_tra,
                        "diem_thi": diem_thi
                    })
                except ValueError:
                    print(f"Lỗi: dữ liệu điểm không hợp lệ ở sinh viên {row[1]}")
                except IndexError:
                    print("Lỗi: dòng dữ liệu thiếu cột")
    except FileNotFoundError:
        print("Lỗi: File không tồn tại.")
    return students

def tinh_diem_tong_ket(students):
    for sv in students:
        sv["diem_tong_ket"] = 0.1 * sv["diem_chuyen_can"] + 0.3 * sv["diem_kiem_tra"] + 0.6 * sv["diem_thi"]

def xep_loai_sinh_vien(students):
    for sv in students:
        sv["xep_loai"] = xep_loai(sv["diem_tong_ket"])

def tim_sv_max(students):
    if students:
        return max(students, key=lambda sv: sv["diem_tong_ket"])
    return None

def thong_ke(students):
    summary = {}
    for sv in students:
        loai = sv["xep_loai"]
        summary[loai] = summary.get(loai, 0) + 1
    return summary

def ghi_ket_qua(students, filename="result.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f_out:
        writer = csv.writer(f_out)
        writer.writerow(f"{'Mã SV':<10}{'Họ tên':<20}{'Điểm CC':<10}{'Điểm KT':<10}{'Điểm Thi':<10}{'Tổng kết':<12}{'Xếp loại':<10}")
        writer.writerow("-"*82)
        for sv in students:
            writer.writerow(f"{sv['ma_sv']:<10}{sv['ho_ten']:<20}{sv['diem_chuyen_can']:<10}{sv['diem_kiem_tra']:<10}{sv['diem_thi']:<10}{sv['diem_tong_ket']:<12.2f}{sv['xep_loai']:<10}")

def ghi_thong_ke(summary, filename="summary.txt"):
    with open(filename, "w", encoding="utf-8") as f_sum:
        f_sum.write("Thống kê số lượng sinh viên theo xếp loại:\n")
        for loai, so_luong in summary.items():
            f_sum.write(f"{loai}: {so_luong}\n")

def in_ket_qua(students):
    print(f"{'Mã SV':<10}{'Họ tên':<20}{'Điểm CC':<10}{'Điểm KT':<10}{'Điểm Thi':<10}{'Tổng kết':<12}{'Xếp loại':<10}")
    print("-"*82)
    for sv in students:
        print(f"{sv['ma_sv']:<10}{sv['ho_ten']:<20}{sv['diem_chuyen_can']:<10}{sv['diem_kiem_tra']:<10}{sv['diem_thi']:<10}{sv['diem_tong_ket']:<12.2f}{sv['xep_loai']:<10}")


def main():
    students = doc_du_lieu_csv("students.csv")
    if not students:
        return
    
    tinh_diem_tong_ket(students)
    xep_loai_sinh_vien(students)

    in_ket_qua(students)
    sv_max = tim_sv_max(students)
    if sv_max:
        print("Sinh viên có điểm tổng kết cao nhất:", sv_max["ho_ten"], sv_max["diem_tong_ket"])

    summary = thong_ke(students)

    ghi_ket_qua(students)
    ghi_thong_ke(summary)

if __name__ == "__main__":
    main()