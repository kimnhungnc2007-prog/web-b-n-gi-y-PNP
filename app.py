import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="PNP | Men's Sneakers",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {font-family: 'Inter', sans-serif;}
.stApp {background: #f4f4f2; color:#171717;}
.block-container {max-width:1250px; padding-top:1.3rem;}
[data-testid="stSidebar"] {background:#171717;}
[data-testid="stSidebar"] * {color:#fff !important;}
.hero {
 background:linear-gradient(110deg,rgba(0,0,0,.92),rgba(30,30,30,.78)),
 linear-gradient(45deg,#333,#777);
 border-radius:24px; padding:42px 38px; color:white;
 border:1px solid #333; min-height:280px;
}
.hero h1 {font-family:'Barlow Condensed',sans-serif; font-size:76px; line-height:.9;
 color:#fff; letter-spacing:2px; margin:10px 0;}
.hero p {color:#dedede; font-size:17px; max-width:650px;}
.orange {color:#ff6b2c;}
.kicker {font-size:12px; letter-spacing:3px; font-weight:800; color:#ff7a42;}
.product {
 background:white; border:1px solid #e5e5e5; border-radius:18px;
 padding:16px; min-height:150px; box-shadow:0 5px 18px rgba(0,0,0,.035);
}
.product h3 {font-size:18px; color:#171717; margin:8px 0 4px;}
.price {font-weight:900; color:#f05a24; font-size:20px;}
.tag {display:inline-block;background:#171717;color:white;padding:5px 10px;
 border-radius:20px;font-size:11px;font-weight:800;letter-spacing:1px;}
.panel {background:white;border:1px solid #e6e6e6;border-radius:18px;padding:22px;}
.metric {background:#fff;border-radius:16px;padding:16px;border:1px solid #e7e7e7;}
div.stButton > button, div.stFormSubmitButton > button {
 background:#ff6b2c;color:white;border:0;border-radius:12px;font-weight:800;
 min-height:42px;
}
div.stButton > button:hover, div.stFormSubmitButton > button:hover {
 background:#e9571c;color:white;border:0;
}
h1,h2,h3 {color:#171717;}
hr {border-color:#dedede;}
.small-note {color:#777;font-size:12px;}
</style>
""", unsafe_allow_html=True)

# =========================
# DATA
# =========================
PRODUCTS = [
    {"id":"PNP01","name":"PNP Street Classic","price":459000,"category":"Classic","badge":"BEST SELLER","emoji":"👟","desc":"Thiết kế basic, dễ phối đồ hằng ngày.","sizes":[39,40,41,42,43,44]},
    {"id":"PNP02","name":"PNP Urban White","price":499000,"category":"Minimal","badge":"NEW","emoji":"🤍","desc":"Tông trắng tối giản, hợp mọi outfit.","sizes":[39,40,41,42,43,44,45]},
    {"id":"PNP03","name":"PNP Retro Court","price":529000,"category":"Retro","badge":"HOT","emoji":"🏀","desc":"Cảm hứng retro thể thao năng động.","sizes":[39,40,41,42,43,44]},
    {"id":"PNP04","name":"PNP Black Move","price":489000,"category":"Sport","badge":"DAILY PICK","emoji":"🖤","desc":"Phối đen cá tính, linh hoạt khi di chuyển.","sizes":[39,40,41,42,43,44,45]},
    {"id":"PNP05","name":"PNP Chunky Wave","price":599000,"category":"Streetwear","badge":"TRENDING","emoji":"⚡","desc":"Đế chunky nổi bật, phong cách streetwear.","sizes":[39,40,41,42,43,44]},
    {"id":"PNP06","name":"PNP Canvas Low","price":399000,"category":"Classic","badge":"EASY WEAR","emoji":"🛹","desc":"Phom thấp gọn nhẹ, trẻ trung và thoải mái.","sizes":[38,39,40,41,42,43,44]},
    {"id":"PNP07","name":"PNP Grey Runner","price":559000,"category":"Sport","badge":"ACTIVE","emoji":"🏃","desc":"Phong cách runner khỏe khoắn.","sizes":[39,40,41,42,43,44,45]},
    {"id":"PNP08","name":"PNP Mono Street","price":549000,"category":"Streetwear","badge":"LIMITED","emoji":"🔥","desc":"Phối màu đơn sắc mạnh mẽ, cá tính.","sizes":[39,40,41,42,43,44]},
]
PRIZES = [
    ("🎟️ Voucher giảm 10%", 25),
    ("🔥 Giảm ngay 50.000đ", 20),
    ("🚚 Hỗ trợ phí vận chuyển", 20),
    ("🧦 Tặng vớ PNP", 15),
    ("💥 Voucher giảm 15%", 10),
    ("🍀 Chúc bạn may mắn lần sau", 10),
]

def money(value):
    return f"{value:,.0f}đ".replace(",", ".")

# =========================
# SESSION
# =========================
for key, default in {
    "cart": [], "spin_result": None, "orders": []
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# =========================
# HEADER / SIDEBAR
# =========================
st.markdown("""
<div class="hero">
  <div class="kicker">MEN'S SNEAKERS • STREET CULTURE • EVERYDAY COMFORT</div>
Bạn đã đạt giới hạn phân tích dữ liệu. Nâng cấp lên ChatGPT Plus hoặc thử lại ngày mai sau 22:59.


