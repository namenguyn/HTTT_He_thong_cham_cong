import React, { useState, useEffect } from 'react';

function DuAnInfo() {
  const [employeeStatus, setEmployeeStatus] = useState([]);  
  const [loading, setLoading] = useState(true);  
  const [error, setError] = useState(null);  

  // useEffect(() => {
  //   const fetchEmployeeStatus = async () => {
  //     try {
  //       const response = await fetch('/api/trang-thai');  
  //       console.log('Response Status:', response.status);  

  //       if (!response.ok) {
  //         throw new Error(`Failed to fetch data. Status: ${response.status}`);
  //       }

  //       const result = await response.json();
  //       console.log('Fetched Data:', result);  

  //       if (result.success && Array.isArray(result.data)) {
  //         setEmployeeStatus(result.data);  
  //       } else {
  //         throw new Error('Invalid data format');
  //       }
  //     } catch (error) {
  //       console.error('Error details:', error);  
  //       setError(error.message);  
  //     } finally {~
  //       setLoading(false);  
  //     }
  //   };

  //   fetchEmployeeStatus();  
  // }, []); 

  useEffect(() => {
    const mockData = [
      { id: 1, name: 'Nguyễn Văn Nam', status: 'Có mặt' },
      { id: 2, name: 'Trần Thị Ánh Nguyệt', status: 'Vắng' },
      { id: 3, name: 'Lê Hồng Phong', status: 'Có mặt' },
      { id: 4, name: 'Phạm Thị Minh Hà', status: 'Vắng' },
      { id: 5, name: 'Hoàng Văn Quân', status: 'Có mặt' },
      { id: 6, name: 'Đặng Thị Thanh Hương', status: 'Có mặt' },
      { id: 7, name: 'Vũ Minh Trí', status: 'Vắng' },
      { id: 8, name: 'Ngô Thị Hồng Ngọc', status: 'Có mặt' },
      { id: 9, name: 'Bùi Văn Long', status: 'Có mặt' },
      { id: 10, name: 'Trương Thị Lan Anh', status: 'Vắng' },
      { id: 11, name: 'Phạm Thị Anh', status: 'Vắng'},
      { id: 12, name: 'Lê Văn Quân', status: 'Có mặt'},
      { id: 13, name: 'Hoàng Thị Nam', status: 'Vắng'},
      { id: 14, name: 'Trần Hồng Nguyệt', status: 'Có mặt'},
      { id: 15, name: 'Ngô Văn Hương', status: 'Có mặt'},
      { id: 16, name: 'Trương Thanh Long', status: 'Có mặt'},
      { id: 17, name: 'Trương Lan Ngọc', status: 'Vắng'},
      { id: 18, name: 'Vũ Quân Hương', status: 'Vắng'},
      { id: 19, name: 'Vũ Thanh Quân', status: 'Vắng'},
      { id: 20, name: 'Trương Thị Nguyệt', status: 'Vắng'}
    ];
    setTimeout(() => {
      setEmployeeStatus(mockData);
      setLoading(false);
    }, 1000);
  }, []);


  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>Trạng thái nhân viên</h1>
      <table border="1" style={{ width: '100%', textAlign: 'left', marginTop: '20px' }}>
        <thead>
          <tr>
            <th>Tên nhân viên</th>
            <th>Trạng thái</th>
          </tr>
        </thead>
        <tbody>
          {employeeStatus.map((employee) => (
            <tr key={employee.id}>
              <td>{employee.name}</td>
              <td>{employee.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DuAnInfo;
