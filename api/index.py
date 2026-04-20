from fasthtml.common import *
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Khởi tạo Firebase
# Lưu ý: Trên Vercel, hãy dùng biến môi trường để bảo mật key
if not firebase_admin._apps:
    cred = credentials.Certificate("path/to/your/firebase-key.json") # Hoặc dùng env dict
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Khởi tạo FastHTML app
app, rt = fast_app()

@rt("/")
def get():
    # Ví dụ lấy dữ liệu từ Firestore
    docs = db.collection("users").stream()
    user_list = [Li(doc.to_dict().get("name")) for doc in docs]
    
    return Titled("FastHTML + Firebase",
        Ul(*user_list),
        P("Đang chạy trên Vercel!")
    )

# Quan trọng: Vercel cần object 'app' để serve
serve()
