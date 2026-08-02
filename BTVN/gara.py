class MatHang:
    def __init__(self, ten_hang="", don_gia=0.0, so_luong=0):
        self.ten_hang = ten_hang
        self.don_gia = float(don_gia)
        self.so_luong = int(so_luong)

    @property
    def thanh_tien(self):
        return self.don_gia * self.so_luong

    def nhap(self):
        print("--- Nhập thông tin mặt hàng ---")
        self.ten_hang = input("Tên hàng: ")
        self.don_gia = float(input("Đơn giá: "))
        self.so_luong = int(input("Số lượng: "))

    def hien_thi(self):
        print(f"{self.ten_hang:<15} {self.don_gia:<10} {self.so_luong:<10} {self.thanh_tien:<10}")


class PhieuNhapHang:
    def __init__(self):
        self.ma_phieu = ""
        self.ngay_lap = ""
        self.ma_ncc = ""
        self.ten_ncc = ""
        self.dia_chi = ""
        self.danh_sach_hang = []  # Quan hệ hợp thành (Phiếu nhập hàng chứa các mặt hàng)

    def nhap(self):
        print("=== NHẬP THÔNG TIN PHIẾU NHẬP HÀNG ===")
        self.ma_phieu = input("Mã phiếu: ")
        self.ngay_lap = input("Ngày lập: ")
        self.ma_ncc = input("Mã NCC: ")
        self.ten_ncc = input("Tên NCC: ")
        self.dia_chi = input("Địa chỉ: ")

        n = int(input("Nhập số lượng mặt hàng: "))
        for i in range(n):
            print(f"\nNhập mặt hàng thứ {i + 1}:")
            mh = MatHang()
            mh.nhap()
            self.danh_sach_hang.append(mh)

    @property
    def tong_thanh_tien(self):
        return sum(mh.thanh_tien for mh in self.danh_sach_hang)

    def hien_thi(self):
        print("\n" + "=" * 60)
        print(f"{'PHIẾU NHẬP HÀNG':^60}")
        print("=" * 60)
        print(f"Mã phiếu: {self.ma_phieu:<20} Ngày lập: {self.ngay_lap}")
        print(f"Mã NCC:   {self.ma_ncc:<20} Tên NCC:  {self.ten_ncc}")
        print(f"Địa chỉ:  {self.dia_chi}")
        print("-" * 60)
        print(f"{'Tên hàng':<15} {'Đơn giá':<10} {'Số lượng':<10} {'Thành tiền':<10}")
        print("-" * 60)
        for mh in self.danh_sach_hang:
            mh.hien_thi()
        print("-" * 60)
        print(f"{'Cộng thành tiền:':<45} {self.tong_thanh_tien}")
        print("=" * 60)

    def luu_file(self, ten_file="phieu_nhap.txt"):
        with open(ten_file, "w", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            f.write(f"{'PHIẾU NHẬP HÀNG':^60}\n")
            f.write("=" * 60 + "\n")
            f.write(f"Mã phiếu: {self.ma_phieu:<20} Ngày lập: {self.ngay_lap}\n")
            f.write(f"Mã NCC:   {self.ma_ncc:<20} Tên NCC:  {self.ten_ncc}\n")
            f.write(f"Địa chỉ:  {self.dia_chi}\n")
            f.write("-" * 60 + "\n")
            f.write(f"{'Tên hàng':<15} {'Đơn giá':<10} {'Số lượng':<10} {'Thành tiền':<10}\n")
            f.write("-" * 60 + "\n")
            for mh in self.danh_sach_hang:
                f.write(f"{mh.ten_hang:<15} {mh.don_gia:<10} {mh.so_luong:<10} {mh.thanh_tien:<10}\n")
            f.write("-" * 60 + "\n")
            f.write(f"{'Cộng thành tiền:':<45} {self.tong_thanh_tien}\n")
            f.write("=" * 60 + "\n")
        print(f"Đã lưu thông tin phiếu nhập vào tệp '{ten_file}' thành công!")


# --- Chương trình chính ---
if __name__ == "__main__":
    # Tạo đối tượng phiếu nhập hàng
    phieu = PhieuNhapHang()

    # Nhập dữ liệu từ bàn phím (hoặc bạn có thể tạo sẵn dữ liệu mẫu như đề bài)
    phieu.nhap()

    # Hiển thị thông tin ra màn hình
    phieu.hien_thi()

    # Lưu thông tin vào tệp văn bản
    phieu.luu_file("phieu_nhap_hang.txt")