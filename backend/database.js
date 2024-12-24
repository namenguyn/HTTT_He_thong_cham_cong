// database.js

import mysql from 'mysql2/promise';
import dotenv from 'dotenv';

dotenv.config();

// Tạo một connection pool
export const pool = mysql.createPool({
    host: process.env.MYSQL_HOST,
    user: process.env.MYSQL_USER,
    password: process.env.MYSQL_PASSWORD,
    database: process.env.MYSQL_DATABASE,
    waitForConnections: true,
    connectionLimit: 10, // Số lượng kết nối tối đa
    queueLimit: 0
});

// Hàm để thực hiện các truy vấn đọc
export async function ReadQuery(sql, params = []) {
    try {
        const [rows, fields] = await pool.execute(sql, params);
        return rows;
    } catch (error) {
        console.error("Error in ReadQuery:", error);
        throw error;
    }
}

// Hàm để thực hiện các truy vấn từ thủ tục Stored Procedure và trả về mảng đầu tiên
export async function ReadFromProcedureQuery(sql, params = []) {
    try {
        const [rows, fields] = await pool.execute(sql, params);
        return rows;
    } catch (error) {
        console.error("Error in ReadFromProcedureQuery:", error);
        throw error;
    }
}

// Hàm để thực hiện các truy vấn ghi
export async function WriteQuery(sql, params = []) {
    try {
        const [result] = await pool.execute(sql, params);
        return [200, 'Thành công'];
    } catch (error) {
        console.error("Error in WriteQuery:", error);
        return [400, error.message];
    }
}
