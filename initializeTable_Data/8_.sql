use quanlynhansu

CREATE TABLE BangChamCong(
    LogID INT AUTO_INCREMENT,
    MaNV CHAR(6), 
    TinhTrang CHAR(20),
    Ngay DATE,
    Gio TIME,
    PRIMARY KEY (LogID)
);
DELIMITER $$

CREATE PROCEDURE insert_BangChamCong(
    IN p_MaNV CHAR(6),
    IN p_TinhTrang CHAR(20),
    IN p_Ngay DATE,
    IN p_Gio TIME
)
BEGIN
    INSERT INTO BangChamCong (MaNV, TinhTrang, Ngay, Gio)
    VALUES (p_MaNV, p_TinhTrang, p_Ngay, p_Gio);
END $$

DELIMITER ;
select* from BangChamCong




