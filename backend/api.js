// api.js

import { ReadFromProcedureQuery, ReadQuery, WriteQuery, pool } from "./database.js";

// Các hàm khác...

export const getNhanVien = async () => {
    const rows = await ReadQuery('SELECT * FROM NhanVien');
    return rows;
};

export const getPhongBan = async (MaPB) => {
    const rows = await ReadQuery('SELECT * FROM phongban WHERE MaPhongBan = ?', [MaPB]);
    return rows;
};

export const getPhongBanInfo = async () => {
    const rows = await ReadQuery('SELECT * FROM phongban');
    return rows;
};

export const getChiNhanh = async () => {
    const rows = await ReadQuery('SELECT * FROM chinhanh');
    return rows;
};

export const getMaChiNhanh_TenChiNhanh = async () => {
    const rows = await ReadQuery(`SELECT CONCAT(MaChiNhanh, ' - ', TenChiNhanh) AS MaTenChiNhanh FROM chinhanh`);
    return rows;
};

export const getChiNhanh_Manager = async () => {
    const rows = await ReadQuery(`
        SELECT 
            chinhanh.MaChiNhanh, 
            chinhanh.TenChiNhanh, 
            chinhanh.DiaChi, 
            nhanvien.MaNV, 
            CONCAT(nhanvien.Ho, ' ', nhanvien.TenLot, ' ', nhanvien.Ten) AS TenQuanLy 
        FROM chinhanh 
        JOIN nhanvien ON chinhanh.MSNV_QuanLy = nhanvien.MaNV
    `);
    return rows;
};

export const getPhongBanInfo_Manager = async () => {
    const rows = await ReadQuery(`
        SELECT 
            nhanvien.MaPhongBan, 
            phongban.TenPhongBan, 
            phongban.MaChiNhanh, 
            phongban.SoLuongNhanVien, 
            nhanvien.MaNV, 
            CONCAT(nhanvien.Ho, ' ', nhanvien.TenLot, ' ', nhanvien.Ten) AS TenVanHanh 
        FROM phongban 
        JOIN nhanvien ON phongban.MSNV_VanHanh = nhanvien.MaNV
    `);
    return rows;
};

export const getMaPhongBan_TenPhongBan = async (MaChiNhanh) => {
    if (MaChiNhanh !== "") {
        const rows = await ReadQuery(`SELECT CONCAT(MaPhongBan, ' - ', TenPhongBan) AS MaTenPhongBan FROM phongban WHERE MaChiNhanh = ?`, [MaChiNhanh]);
        return rows;
    } 
    const rows = await ReadQuery(`SELECT CONCAT(MaPhongBan, ' - ', TenPhongBan) AS MaTenPhongBan FROM phongban`);
    return rows;
};

export const insertChiNhanh = async (MaChiNhanh, TenChiNhanh, DiaChi, MSNV_QuanLy) => {
    try {
        const [result] = await pool.execute(
            `CALL insert_ChiNhanh(?, ?, ?, ?)`,
            [MaChiNhanh, TenChiNhanh, DiaChi, MSNV_QuanLy]
        );
        return [200, 'Thành công'];
    } catch (error) {
        console.error("Error in insertChiNhanh:", error);
        return [400, 'Lỗi khi chèn dữ liệu'];
    }
};

export const getMaNV_TenNhanVien = async () => {
    const rows = await ReadQuery(`
        SELECT 
            MaNV, 
            CONCAT(nhanvien.Ho, ' ', nhanvien.TenLot, ' ', nhanvien.Ten) AS TenNhanVien 
        FROM nhanvientoanthoigian 
        NATURAL INNER JOIN nhanvien 
        ORDER BY MaNV
    `);
    return rows;
};

export const insertNhanVien = async (MaNV, Ho, TenLot, Ten, GioiTinh, Email, LuongTheoGio, MaPhongBan) => {
    try {
        const [result] = await pool.execute(
            `CALL ThemNhanVien(?, ?, ?, ?, ?, ?, ?, ?)`,
            [MaNV, Ho, TenLot, Ten, GioiTinh, Email, LuongTheoGio, MaPhongBan]
        );
        console.log("result", result);
        return [200, 'Thành công'];
    } catch (error) {
        console.error("Error in insertNhanVien:", error);
        return [400, 'Lỗi khi chèn dữ liệu'];
    }
};

export const deleteNhanVien = async (MaNV) => {
    try {
        const [result] = await pool.execute(
            `CALL XoaNhanVien(?)`,
            [MaNV]
        );
        return [200, 'Thành công'];
    } catch (error) {
        console.error("Error in deleteNhanVien:", error);
        return [400, 'Lỗi khi xóa dữ liệu'];
    }
};

export const updateNhanVien = async (MaNV, Ho, TenLot, Ten, GioiTinh, Email, HeSoPhatDiTre, HeSoPhatVangKhongPhep, SoNgayNghi, LuongTheoGio, MaPhongBan) => {
    try {
        const [result] = await pool.execute(
            `CALL SuaNhanVien(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
            [MaNV, Ho, TenLot, Ten, GioiTinh, Email, HeSoPhatDiTre, HeSoPhatVangKhongPhep, SoNgayNghi, LuongTheoGio, MaPhongBan]
        );
        console.log("result", result);
        return [200, 'Thành công'];
    } catch (error) {
        console.error("Error in updateNhanVien:", error);
        return [400, 'Lỗi khi cập nhật dữ liệu'];
    }
};

export const getDanhSachPhongBan = async () => {
    const rows = await ReadQuery(`SELECT MaPhongBan, TenPhongBan FROM phongban`);
    return rows;
};

export const getNhanVienByMaNV = async (MaNV) => {
    const rows = await ReadQuery(`SELECT * FROM NhanVien WHERE MaNV = ?`, [MaNV]);
    return rows.length ? rows[0] : null;
};

export const getBangLuong = async (MaPhongBan, EmpType, BeginDate, EndDate) => {
    if ((BeginDate === "") || (EndDate === "")) return [];
    const rows = await ReadFromProcedureQuery(`CALL View_BangLuong(?, ?, ?, ?)`, [MaPhongBan, EmpType, BeginDate, EndDate]);
    return rows;
};

export const getPhongBanCoSoLuongNhanVienLonHon = async (min) => {
    const rows = await ReadFromProcedureQuery(`CALL LocPhongBanCoSoLuongNhanVienLonHon(?)`, [min]);
    return rows;
};

export const getPhongBanCoSoLuongNhanVienCoMatNhieuNhat = async () => {
    try {
        const rows = await ReadFromProcedureQuery('CALL LocPhongBanCoSoLuongNhanVienCoMatNhieuNhat()');
        return rows;
    } catch (error) {
        console.error(error);
        throw error;  // Rethrow the error if needed for logging
    }
};

export const getHienThiTrangThai = async (NgayBatDau, NgayKetThuc) => {
    const rows = await ReadFromProcedureQuery(`CALL HienThiTrangThai(?, ?)`, [NgayBatDau, NgayKetThuc]);
    return rows;
};

export const insertBangChamCong = async (MaNV, TinhTrang, Ngay, Gio) => {
    try {
        const [rows] = await pool.execute(
            `CALL insert_BangChamCong(?, ?, ?, ?)`,
            [MaNV, TinhTrang, Ngay, Gio]
        );
        return [200, 'Thành công'];
    } catch (error) {
        console.error("Error in insertBangChamCong:", error);
        return [400, 'Lỗi khi chèn dữ liệu'];
    }
};


export const insertPhongBan = async (MaPhongBan, TenPhongBan, MaChiNhanh, SoLuongNhanVien, MSNV_VanHanh) => {
    try {
        const [result] = await pool.execute(
            `CALL insert_PhongBan(?, ?, ?, ?, ?)`,
            [MaPhongBan, TenPhongBan, MaChiNhanh, SoLuongNhanVien, MSNV_VanHanh]
        );
        return [200, 'Thành công'];
    } catch (error) {
        console.error("Error in insertPhongBan:", error);
        return [400, 'Lỗi khi chèn dữ liệu'];
    }
};
