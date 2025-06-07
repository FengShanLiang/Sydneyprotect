# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# 设置跨域中间件（允许前端访问）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 建议上线后改为你的前端域名更安全
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 示例：健康检查接口
@app.get("/api/ping")
def ping():
    return {"message": "pong", "timestamp": datetime.utcnow().isoformat()}

# 示例：一键求助数据结构
class HelpRequest(BaseModel):
    user_id: str
    location: str
    message: str

# 接收求助请求
@app.post("/api/help")
def submit_help(request: HelpRequest):
    # 你可以把这个数据存入数据库，或者发邮件、消息通知
    print(f"[HELP] 用户: {request.user_id}, 地点: {request.location}, 信息: {request.message}")
    return {"status": "received", "user_id": request.user_id}
