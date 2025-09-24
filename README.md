# QuanMBL-FastApi_Fresher
Dùng Thunder client để test API 

1. GET /A → hello world
<img width="1077" height="305" alt="image" src="https://github.com/user-attachments/assets/5eccfb7d-d77c-4f7c-a2b0-c6c7f682d5a8" />



2. Tạo /B qua Admin API → gọi được /B
  2.1. Tạo path /B 
    - tạo key, value, ghi log và json body
    <img width="1080" height="583" alt="image" src="https://github.com/user-attachments/assets/d0000ed4-a09f-4c22-9be7-0592c55176db" />
    <img width="1077" height="627" alt="image" src="https://github.com/user-attachments/assets/f15963d6-7be8-4a7a-8040-c358f433de23" />
  2.2. Kiểm tra Get /B coi đã được tạo chưa
   <img width="1073" height="585" alt="image" src="https://github.com/user-attachments/assets/ef3c392e-44bc-4c9a-8036-3c86a1743d80" />


3. Restart container → /B vẫn tồn tại
  <img width="1073" height="585" alt="image" src="https://github.com/user-attachments/assets/ef3c392e-44bc-4c9a-8036-3c86a1743d80" />


4. Xóa /B → gọi /B trả 404
   4.1. xóa /B
  <img width="1086" height="477" alt="image" src="https://github.com/user-attachments/assets/b6224447-e6f9-4d91-ae4d-a1f0afbf58c7" />
  4.2. kiểm tra coi còn không -> không còn trả về 404
  <img width="1401" height="487" alt="image" src="https://github.com/user-attachments/assets/5609fd59-2a28-4cd4-b01a-2c94d89d1451" />


5. Sai/thiếu X-API-Key → 401
  5.1. Test sai Key,value của header
     <img width="1382" height="597" alt="image" src="https://github.com/user-attachments/assets/5c589e03-9daf-4de6-b5cf-e217d3e53ce7" />


  5.2 Test thiếu không có Key, value
    <img width="1391" height="376" alt="image" src="https://github.com/user-attachments/assets/c8147892-2127-418b-894c-94ac996d7360" />
    





