import { ReadFromProcedureQuery, ReadQuery, WriteQuery } from "./database.js";

export const getNhanVien = async () => {
    const rows = await ReadQuery('SELECT * FROM NhanVien');
    return rows;
};


export const getPhongBan = async (MaPB) => {
    const rows = await ReadQuery(`SELECT * FROM phongban WHERE MaPhongBan='${MaPB}'`)
    return rows;
}

export const getPhongBanInfo = async () => {
    const rows = await ReadQuery('SELECT * FROM phongban');
    return rows;
}

export const getChiNhanh = async () => {
    const rows = await ReadQuery('Select * from chinhanh');
    return rows;
}

export const getMaChiNhanh_TenChiNhanh = async() => {
    const rows = await ReadQuery(`Select CONCAT(\`MaChiNhanh\`, ' - ', \`TenChiNhanh\`) from chinhanh`)
    return rows;
}

export const getChiNhanh_Manager = async () => {
    const rows = await ReadQuery(`SELECT \`MaChiNhanh\`, \`TenChiNhanh\`, \`DiaChi\`, nhanvien.\`MaNV\`, CONCAT(nhanvien.\`Ho\`,' ', nhanvien.\`TenLot\`,' ', nhanvien.\`Ten\`) as 'TenQuanLy' from chinhanh JOIN nhanvien ON chinhanh.\`MSNV_QuanLy\`=nhanvien.\`MaNV\`;`)
    return rows;
}

export const getPhongBanInfo_Manager = async () => {
    const rows = await ReadQuery(`SELECT nhanvien.\`MaPhongBan\`, \`TenPhongBan\`, \`MaChiNhanh\`, \`SoLuongNhanVien\`, nhanvien.\`MaNV\`, CONCAT (nhanvien.\`Ho\`,' ', nhanvien.\`TenLot\`,' ', nhanvien.\`Ten\`) as 'TenVanHanh' from phongban JOIN nhanvien ON phongban.\`MSNV_VanHanh\`=nhanvien.\`MaNV\`;`)
    return rows;
}

export const getMaPhongBan_TenPhongBan = async (MaChiNhanh) => {
    if (MaChiNhanh !== "") {
        const rows = await ReadQuery(`SELECT CONCAT(phongban.\`MaPhongBan\`, ' - ', phongban.\`TenPhongBan\`) FROM phongban WHERE phongban.\`MaChiNhanh\` = '${MaChiNhanh}';`);
        return rows;
    } 
    const rows = await ReadQuery(`SELECT CONCAT(phongban.\`MaPhongBan\`, ' - ', phongban.\`TenPhongBan\`) FROM phongban`);
    return rows;
}

export const insertChiNhanh = async (MaChiNhanh, TenChiNhanh, DiaChi, MSNV_QuanLy) => {
    const [result, message] = await WriteQuery(`CALL \`insert_ChiNhanh\`('${MaChiNhanh}', '${TenChiNhanh}', '${DiaChi}', '${MSNV_QuanLy}')`);
    // console.log("result", result)
    return [result, message];
}

export const getMaNV_TenNhanVien = async () => {
    const rows = await ReadQuery("SELECT `MaNV`, CONCAT(nhanvien.`Ho`, ' ', nhanvien.`TenLot`, ' ', nhanvien.`Ten`) as 'TenNhanVien' from nhanvientoanthoigian NATURAL INNER JOIN nhanvien ORDER BY `MaNV`;")
    return rows
}


export const insertNhanVien = async (MaNV, Ho, TenLot, Ten, GioiTinh, Email, LuongTheoGio, MaPhongBan) => {
    const [result, message] = await WriteQuery(
        `CALL ThemNhanVien('${MaNV}', '${Ho}', '${TenLot}', '${Ten}', '${GioiTinh}', '${Email}', ${LuongTheoGio}, '${MaPhongBan}')`
    );
    console.log("result", result)
    return [result, message];
};

export const deleteNhanVien = async (MaNV) => {
    const [result, message] = await WriteQuery(`CALL XoaNhanVien('${MaNV}')`);
    return [result, message];
};

export const updateNhanVien = async (MaNV, Ho, TenLot, Ten, GioiTinh, Email, HeSoPhatDiTre, HeSoPhatVangKhongPhep, SoNgayNghi, LuongTheoGio, MaPhongBan) => {
    const [result, message] = await WriteQuery(
        `CALL SuaNhanVien('${MaNV}', '${Ho}', '${TenLot}', '${Ten}', '${GioiTinh}', '${Email}', ${HeSoPhatDiTre}, ${HeSoPhatVangKhongPhep}, ${SoNgayNghi}, ${LuongTheoGio}, '${MaPhongBan}')`
    );
    console.log("result", result)
    return [result, message];
};

export const getDanhSachPhongBan = async () => {
    const rows = await ReadQuery(`SELECT MaPhongBan, TenPhongBan FROM phongban`);
    return rows;
};

export const getNhanVienByMaNV = async (MaNV) => {
    const rows = await ReadQuery(`SELECT * FROM NhanVien WHERE MaNV = '${MaNV}'`);
    return rows.length ? rows[0] : null;
};

export const getBangLuong = async (MaPhongBan, EmpType, BeginDate, EndDate) => {
    if ((BeginDate === "") || (EndDate === "")) return [];
    const rows = await ReadFromProcedureQuery(`CALL View_BangLuong('${MaPhongBan}', ${EmpType}, '${BeginDate}', '${EndDate}')`);
    // console.log(rows);
    return rows;
}

export const getPhongBanCoSoLuongNhanVienLonHon = async (min) => {
    const rows = await ReadFromProcedureQuery(`CALL LocPhongBanCoSoLuongNhanVienLonHon(${min})`);
    return rows;
};

export const getPhongBanCoSoLuongNhanVienCoMatNhieuNhat = async () => {
    try {
        const rows = await ReadFromProcedureQuery('CALL LocPhongBanCoSoLuongNhanVienCoMatNhieuNhat');
        return rows;
    } catch (error) {
        console.error(error);
        throw error;  // Rerun the error if needed for logging
    }
};

export const getHienThiTrangThai = async (NgayBatDau, NgayKetThuc) => {
        const rows = await ReadFromProcedureQuery(`CALL HienThiTrangThai('${NgayBatDau}', '${NgayKetThuc}')`);
        return rows;
};

