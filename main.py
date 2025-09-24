from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional, Dict, Any
import json
import os
from pathlib import Path

app = FastAPI()

# Biến môi trường
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY", "admin-secret-key-123")
PORT = int(os.getenv("PORT", "8000"))

# File lưu trữ routes
ROUTES_FILE = "data/routes.json"

# Lưu trữ các routes động
dynamic_routes: Dict[str, Dict[str, Any]] = {}

def load_routes():
    """Load routes từ file JSON"""
    global dynamic_routes
    # Tạo thư mục data nếu chưa có
    Path("data").mkdir(exist_ok=True)
    
    if Path(ROUTES_FILE).exists():
        try:
            with open(ROUTES_FILE, 'r', encoding='utf-8') as f:
                dynamic_routes = json.load(f)
                # Đăng ký lại các routes đã lưu
                for path, data in dynamic_routes.items():
                    async def create_endpoint(msg=data["message"]):
                        return {"message": msg}
                    app.get(f"/{path}")(create_endpoint)
        except Exception as e:
            print(f"Error loading routes: {e}")
            dynamic_routes = {}

def save_routes():
    """Lưu routes vào file JSON"""
    try:
        with open(ROUTES_FILE, 'w', encoding='utf-8') as f:
            json.dump(dynamic_routes, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving routes: {e}")

# Load routes khi khởi động
load_routes()

def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != ADMIN_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

@app.get("/A")
async def get_a():
    return {"message": "hello world"}

# Admin API endpoints
@app.post("/admin/routes")
async def create_route(
    path: str,
    message: str,
    api_key: str = Depends(verify_api_key)
):
    """Tạo route mới với path và message tùy chỉnh"""
    if path.startswith("/"):
        path = path[1:]  # Bỏ dấu / ở đầu
    
    if path in dynamic_routes:
        raise HTTPException(status_code=400, detail="Route already exists")
    
    # Lưu route mới
    dynamic_routes[path] = {"message": message}
    
    # Tạo endpoint động
    async def dynamic_endpoint():
        return {"message": message}
    
    # Đăng ký route với FastAPI
    app.get(f"/{path}")(dynamic_endpoint)
    
    # Lưu vào file
    save_routes()
    
    return {"message": f"Route /{path} created successfully", "data": {"message": message}}

@app.get("/admin/routes")
async def list_routes(api_key: str = Depends(verify_api_key)):
    """Liệt kê tất cả routes đã tạo"""
    return {"routes": dynamic_routes}

@app.delete("/admin/routes/{path}")
async def delete_route(path: str, api_key: str = Depends(verify_api_key)):
    """Xóa route theo path"""
    if path not in dynamic_routes:
        raise HTTPException(status_code=404, detail="Route not found")
    
    # Xóa route khỏi dictionary
    del dynamic_routes[path]
    
    # Lưu vào file
    save_routes()
    
    return {"message": f"Route /{path} deleted successfully"}
