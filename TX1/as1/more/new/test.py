import os
import csv

required_colums = {
    "ma_sv",
    "ho_ten",
    "diem_chuyen_can",
    "diem_kiem_tra",
    "diem_thi"
}
input_file = "students.csv"
result_file = "result.csv"
sumary_file = "sumary.txt"

#ktra xem co ton tai that khong?
def kiem_tra(input_file):
    if not os.path.exists(input_file):
        return False
    return True

def tinh_tong_ket(a,b,c):
    return 0.1*a + 0.3*b +0.6*c

def xep_loai(d):
    if d >= 8.5:
        return "Gioi"
    elif d >= 7:
        return "Kha"
    elif d >= 6.0:
        return "Trung_binh"
    else:
        return "Yeu"

def doc_ds(input_file):
    students = []
    with open(input_file,"r",encoding="utf-8")  as f:
        reader = csv.DictReader(f)  # tra ra mot list dict
        if reader.fieldnames is None:
            raise ValueError("File CSV khong co tieu de") 

        for line, row in enumerate(reader, start=2):
            try: 
                diem_chuyen_can = float(row["diem_chuyen_can"])
                diem_kiem_tra = float(row["diem_kiem_tra"])
                diem_thi = float(row["diem_thi"])

                if not(
                    0 <= diem_chuyen_can <= 10
                    and 0<= diem_kiem_tra <= 10
                    and 0<= diem_thi <= 10
                ):
                    raise ValueError("Diem phai nam trong khoang tu 0 den 10")

                diem_tong_ket = tinh_tong_ket(diem_chuyen_can,diem_kiem_tra,diem_thi)

                student = {
                    "ma_sv" : row["ma_sv"].strip(),
                    "ho_ten" : row["ho_ten"].strip(),
                    "diem_chuyen_can" : diem_chuyen_can,
                    "diem_kiem_tra" : diem_kiem_tra,
                    "diem_thi" : diem_thi,
                    "diem_tong_ket" : round(diem_tong_ket,2),
                    "xep_loai" : xep_loai(diem_tong_ket)
                }
                students.append(student)

            except Exception as e:
                print(f"Bo qua dong {line} : {e}")

    return students

def tim_max(students):
    if not students:
        return []
    diem_max = max(student["diem_tong_ket"] for student in students)

    return [
        #chi ra cai muon lay sau khi loc du lieu truoc 
        #f"{student['ma_sv']} - {student['ho_ten']}" : truong hop muon in ma sv va ten sv
        student["ho_ten"]
        for student in students if student["diem_tong_ket"] == diem_max
    ]        

def thong_ke(students):
    summeray = {
        "Gioi" : 0,
        "Kha" : 0,
        "Trung_binh" : 0,
        "Yeu" : 0
    }
    for student in students:
        classification = student["xep_loai"]
        summeray[classification] += 1
    return summeray    

def ghi_result(students, filename):
    try:
        with open(filename, "w", encoding="utf-8", newline="") as file:
            file.write(
                f"{'Ma SV':<10} | "
                f"{'Ten SV':<20} | "
                f"{'Diem TK':<10} | "
                f"{'Xep loai':<20} |\n"
            )
            file.write("-" * 60 +"\n")
            for sv in students:
                row = (
                    f"{sv['ma_sv']:<10} | "
                    f"{sv['ho_ten']:<20} | "
                    f"{sv['diem_tong_ket']:<10} | "
                    f"{sv['xep_loai']:<20} |\n"
                )
                file.write(row)
        print(f"Da ghi thanh cong danh sach vao file: {filename}")
    except Exception as e:
        print(f"Khong ghi file thanh cong. Loi: {e}")

def ghi_summary(best_student, summeray, filename):
    try: 
        with open(filename,"w", encoding="utf-8" ) as file:
            file.write("Danh sach sv co diem tk cao nhat \n")

            if len(best_student) > 0:
                for student in best_student:
                    file.write(f"{student}\n")
            else:
                file.write("Khong co du du lieu. \n")   

            file.write("Thong ke theo xep loai \n")
            file.write(f"Gioi : {summeray['Gioi']}\n")
            file.write(f"Kha : {summeray['Kha']}\n")
            file.write(f"Trung binh : {summeray['Trung_binh']}\n")
            file.write(f"Yeu : {summeray['Yeu']}\n")

            print(f"Da ghi thanh cong du lieu vao file {filename}")
    except Exception as e:
        print(f"Khong ghi tep thanh cong . Loi: {e}")
               
def hien_thi(students):
    print(f"Danh sach ket qua")
    print(
            f"{"Ma SV":<10} | "
            f"{"Ho ten":<20} | "
            f"{"Tong ket":<10} | "
            f"{"Xep loai":<20} |"
    )
    for sv in students:
        print(
            f"{sv['ma_sv'] :<10} | "
            f"{sv['ho_ten']:<20} | "
            f"{sv['diem_tong_ket']:<10} | "
            f"{sv['xep_loai']:<20} |"
        )

def main():
    if not kiem_tra(input_file):
        raise FileNotFoundError(
            f"Khong tim thay file {input_file}"
        ) 
     
    
    students = doc_ds(input_file)

    if not len(students) > 0:
        print("Khong co du lieu")
        return
    hien_thi(students)    

    best_student = tim_max(students)

    summary = thong_ke(students)

    ghi_result(students, result_file)

    ghi_summary(best_student, summary, sumary_file) 


if __name__ == "__main__":
    main()     

