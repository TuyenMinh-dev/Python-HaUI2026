from abc import ABC, abstractmethod

class Xe(ABC):
    def __init__(self, ma_xe, hang, nam_sx, gia):
        self.ma_xe = ma_xe
        self.hang = hang
        self.nam_sx = nam_sx
        self.gia = gia

    @abstractmethod
    def hien_thi(self):
        pass


class XeMay(Xe):
    def __init__(self, ma_xe, hang, nam_sx, gia, dung_tich, loai_xe):
        super().__init__(ma_xe, hang, nam_sx, gia)
        self.dung_tich = dung_tich
        self.loai_xe = loai_xe

    def hien_thi(self):
        print(f"Mã xe: {self.ma_xe}")
        print(f"Hãng: {self.hang}")
        print(f"Năm sản xuất: {self.nam_sx}")
        print(f"Giá xe: {self.gia}")
        print(f"Dung tích: {self.dung_tich}")
        print(f"Loại xe: {self.loai_xe}")
        print("-" * 40)

    def __str__(self):
        return (f"Mã xe: {self.ma_xe}\n"
                f"Hãng: {self.hang}\n"
                f"Năm sản xuất: {self.nam_sx}\n"
                f"Giá xe: {self.gia}\n"
                f"Dung tích: {self.dung_tich}\n"
                f"Loại xe: {self.loai_xe}\n")


class Gara:
    def __init__(self, ten_gara, dia_chi):
        self.ten_gara = ten_gara
        self.dia_chi = dia_chi
        self.ds_xe = []

    # Nhập danh sách xe
    def nhap_ds(self):
        while True:
            n = int(input("Nhập số lượng xe (n > 3): "))
            if n > 3:
                break
            print("n phải lớn hơn 3!")

        for i in range(n):
            print(f"\nNhập xe thứ {i + 1}")

            ma = input("Mã xe: ")
            hang = input("Hãng: ")
            nam = int(input("Năm sản xuất: "))
            gia = float(input("Giá xe: "))
            dung_tich = input("Dung tích: ")
            loai = input("Loại xe: ")

            xe = XeMay(ma, hang, nam, gia, dung_tich, loai)
            self.ds_xe.append(xe)

    # Hiển thị danh sách
    def hien_thi_ds(self):
        print("\n===== DANH SÁCH XE =====")
        for xe in self.ds_xe:
            xe.hien_thi()

    # Tìm xe giá cao nhất
    def xe_gia_cao_nhat(self):
        max_gia = max(xe.gia for xe in self.ds_xe)

        print("\n===== XE GIÁ CAO NHẤT =====")
        for xe in self.ds_xe:
            if xe.gia == max_gia:
                xe.hien_thi()

    # Sắp xếp
    def sap_xep(self):
        self.ds_xe.sort(key=lambda x: (x.nam_sx, -x.gia))

    # Ghi file
    def ghi_file(self):
        with open("gara.txt", "w", encoding="utf-8") as f:
            f.write(f"Tên gara: {self.ten_gara}\n")
            f.write(f"Địa chỉ: {self.dia_chi}\n\n")

            for xe in self.ds_xe:
                f.write(str(xe))
                f.write("-" * 40 + "\n")

        print("Đã ghi dữ liệu vào file gara.txt")


def main():
    print("===== NHẬP THÔNG TIN GARA =====")
    ten = input("Tên gara: ")
    dia_chi = input("Địa chỉ: ")

    gara = Gara(ten, dia_chi)

    gara.nhap_ds()

    gara.hien_thi_ds()

    gara.xe_gia_cao_nhat()

    gara.sap_xep()

    print("\n===== DANH SÁCH SAU KHI SẮP XẾP =====")
    gara.hien_thi_ds()

    gara.ghi_file()


if __name__ == "__main__":
    main()