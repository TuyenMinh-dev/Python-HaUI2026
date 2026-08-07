import csv
import os

REQUIRED_COLUMNS = {
    "ma_sv",
    "ho_ten",
    "diem_chuyen_can",
    "diem_kiem_tra",
    "diem_thi"
}

INPUT_FILE = "students.csv"
RESULT_FILE = "result.csv"
SUMMARY_FILE =  "summary.txt"


def ktra_file(input_file):
    if not os.path.exists(input_file):
        return False
    return True


def kiem_tra_thieu_du_lieu(row):
    for column in REQUIRED_COLUMNS:
        value = row.get(column)
        if value is None or value.strip() == "":
            return True
    return False


def tinh_tong_ket(a,b,c):
    return 0.1*a + 0.3*b + 0.6*c

def xep_loai(d):
    if d >= 8.5:
        return "Gioi"
    elif d >= 7.0:
        return "Kha"
    elif d >= 6.0:
        return "Trung_binh"
    else:
        return "Yeu"


def doc_ds(input_file):
    students = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f) # tra ra mot list dict
        # .fieldnames: danh sach ten cot
        if reader.fieldnames is None:
            raise ValueError("File CSV khong co tieu de")

        actual_columns = set(reader.fieldnames)
        missing_columns = REQUIRED_COLUMNS - actual_columns # phep tru giua 2 set de lay ra cac cot bi thieu

        if missing_columns:
            raise ValueError("File CSV thieu cac cot: " + ", ".join(sorted(missing_columns)))

        # filenames laf 1 nen ta bat dau tu 2
        for line_num, row in enumerate(reader, start= 2):
            try:
                if kiem_tra_thieu_du_lieu(row):
                    raise ValueError("Dong thieu du lieu")

                diem_chuyen_can = float(row["diem_chuyen_can"])
                diem_kiem_tra = float(row["diem_kiem_tra"])
                diem_thi = float(row["diem_thi"])

                if not (
                    0 <= diem_chuyen_can <= 10
                    and 0 <= diem_kiem_tra <= 10
                    and 0 <= diem_thi <= 10 
                ):
                    raise ValueError("Diem nam ngoai vung cho phep")
                
                diem_tong_ket = tinh_tong_ket(diem_chuyen_can, diem_kiem_tra, diem_thi)

                student = {
                    "ma_sv": row["ma_sv"].strip(),
                    "ho_ten": row["ho_ten"].strip(),
                    "diem_chuyen_can": diem_chuyen_can,
                    "diem_kiem_tra": diem_kiem_tra,
                    "diem_thi": diem_thi,
                    "diem_tong_ket": round(diem_tong_ket, 2),
                    "xep_loai": xep_loai(diem_tong_ket)
                }

                students.append(student)
            except ValueError as error:
                print(f"Bo qua dong {line_num}: {error}")

    return students


def tim_sv_diem_cao(students):
    if not students: 
        return[]

    diem_max = max(student["diem_tong_ket"] for student in students)

    return [
        student["ho_ten"]
        for student in students if student["diem_tong_ket"] == diem_max
    ]


def thong_ke_xep_loai(students):
    summeray = {
        "Gioi": 0,
        "Kha": 0,
        "Trung_binh": 0,
        "Yeu": 0
    }

    for student in students:
        classification = student["xep_loai"]
        summeray[classification] += 1
    return summeray

def ghi_file_result (students, filename):

    fieldnames = [
        "ma_sv",
        "ho_ten",
        "diem_chuyen_can",
        "diem_kiem_tra",
        "diem_thi",
        "diem_tong_ket",
        "xep_loai"
    ]

    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)


def ghi_file_summary(best_students, summary, filename):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write("Thong ke ket qua:\n")
        f.write("Sinh vien co diem tong ket cao nhat: \n")

        if best_students:
            for student in best_students:
                f.write(f"- {student}\n")
        else:
            f.write("- Khong co cu lieu sinh vien. \n")

        f.write("\n Thong ke theo xep loai: \n")
        f.write(f"- Gioi: {summary['Gioi']}\n")
        f.write(f"- Kha: {summary['Kha']}\n")
        f.write(f"- Trung binh: {summary['Trung_binh']}\n")
        f.write(f"- Yeu: {summary['Yeu']}\n")


def hien_thi_kq(students):
    print("\n Danh sach ket qua")
    print(
        f"{"Ma SV":<12}"
        f"{"Ho ten":<25}"
        f"{"Tong ket":<12}"
        f"{"Xep loai":<15}"
    )

    for student in students:
        print(
            f"{student['ma_sv']:<12}"
            f"{student['ho_ten']:<25}"
            f"{student['diem_tong_ket']:<12}"
            f"{student['xep_loai']:<15}"
        )
def main():
    # try:
        if not ktra_file(INPUT_FILE):
            raise FileNotFoundError(
                f"khong tim thay file {INPUT_FILE}"
            )
        
        students = doc_ds(INPUT_FILE)

        if not students:
            print("khong co du lieu")
            return

        best_students = tim_sv_diem_cao(students)

        summary = thong_ke_xep_loai(students)

        ghi_file_result(students, RESULT_FILE)

        ghi_file_summary(best_students, summary, SUMMARY_FILE)

        hien_thi_kq(students)

    # except Exception as e:
    #     print(f"Loi: {e}")
    
if __name__ == "__main__":
    main()
