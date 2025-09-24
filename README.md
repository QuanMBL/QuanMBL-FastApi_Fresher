# QuanMBL-FastApi_Fresher

<!-- 

3
http://localhost:8000/B" -Method GET
4 http://localhost:8000/admin/routes/B" -Method DELETE -Headers @
 -->


#File đã được xóa route, nhưng endpoint vẫn còn trong memory. Đây là limitation của FastAPI - không thể xóa route động trong runtime. Tuy nhiên, sau khi restart server, route sẽ không còn.