
import streamlit as st
import random

st.set_page_config(
    page_title="PNP Sneakers",
    page_icon="👟",
    layout="wide"
)

# =========================
# GIAO DIỆN
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800;900&family=Inter:wght@400;600;700;800&display=swap');

.stApp {
    background: #f4f4f2;
    font-family: 'Inter', sans-serif;
}
.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
}
[data-testid="stSidebar"] {
    background: #171717;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.hero {
    background: linear-gradient(120deg,#171717,#454545);
    padding: 40px;
    border-radius: 22px;
    color: white;
}
.hero h1 {
    color: white;
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 75px;
}
.orange {
    color: #ff6b2c;
}
.product {
    background: white;
    border-radius: 18px;
    padding: 20px;
    border: 1px solid #ddd;
    margin-bottom: 12px;
}
.product h3 {
    color: #171717;
}
.price {
    color: #f05a24;
    font-size: 22px;
    font-weight: 900;
}
.panel {
    background: white;
    border-radius: 18px;
    padding: 22px;
    border: 1px solid #ddd;
}
div.stButton > button {
    background: #ff6b2c;
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 800;
}
div.stButton > button:hover {
    background: #e9571c;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# =========================
# DANH SÁCH SẢN PHẨM
# =========================
PRODUCTS = [
    {
        "name": "PNP Street Classic",
        "price": 459000,
        "emoji": "👟",
        "category": "Classic",
        "desc": "Giày bata basic, dễ phối đồ.",
        "sizes": [39,40,41,42,43,44]
    },
    {
        "name": "PNP Urban White",
        "price": 499000,
        "emoji": "🤍",
        "category": "Minimal",
        "desc": "Thiết kế trắng tối giản, trẻ trung.",
        "sizes": [39,40,41,42,43,44,45]
    },
    {
        "name": "PNP Retro Court",
        "price": 529000,
        "emoji": "🏀",
        "category": "Retro",
        "desc": "Phong cách thể thao retro năng động.",
        "sizes": [39,40,41,42,43,44]
    },
    {
        "name": "PNP Black Move",
        "price": 489000,
        "emoji": "🖤",
        "category": "Sport",
        "desc": "Tông đen cá tính, mạnh mẽ.",
        "sizes": [39,40,41,42,43,44,45]
    },
    {
        "name": "PNP Chunky Wave",
        "price": 599000,
        "emoji": "⚡",
        "category": "Streetwear",
        "desc": "Đế chunky nổi bật, thời thượng.",
        "sizes": [39,40,41,42,43,44]
    },
    {
        "name": "PNP Canvas Low",
        "price": 399000,
        "emoji": "🛹",
        "category": "Classic",
        "desc": "Giày thấp cổ nhẹ nhàng, năng động.",
        "sizes": [38,39,40,41,42,43,44]
    },
    {
        "name": "PNP Grey Runner",
        "price": 559000,
        "emoji": "🏃",
        "category": "Sport",
        "desc": "Thiết kế thể thao khỏe khoắn.",
        "sizes": [39,40,41,42,43,44,45]
    },
    {
        "name": "PNP Mono Street",
        "price": 549000,
        "emoji": "🔥",
        "category": "Streetwear",
        "desc": "Phong cách streetwear cá tính.",
        "sizes": [39,40,41,42,43,44]
    }
]

PRIZES = [
    "🎟️ Giảm giá 10%",
    "🔥 Giảm ngay 50.000đ",
    "🚚 Miễn phí vận chuyển",
    "🧦 Tặng một đôi vớ",
    "💥 Giảm giá 15%",
    "🍀 Chúc bạn may mắn lần sau"
]

WEIGHTS = [25,20,20,15,10,10]

def money(price):
    return f"{price:,.0f}đ".replace(",", ".")

# =========================
# KHỞI TẠO GIỎ HÀNG
# =========================
if "cart" not in st.session_state:
    st.session_state.cart = []

if "prize" not in st.session_state:
    st.session_state.prize = None

if "orders" not in st.session_state:
    st.session_state.orders = []

if "size_result" not in st.session_state:
    st.session_state.size_result = None

# =========================
# BANNER
# =========================
st.markdown("""
<div class="hero">
    <h1>PNP<span class="orange">.</span></h1>
    <h2 style="color:white">MEN'S SNEAKERS</h2>
    <p>STEP UP YOUR GAME.</p>
    <p>Không chỉ là một đôi giày. Đó là cách bạn thể hiện chất riêng.</p>
</div>
""", unsafe_allow_html=True)

# =========================
# THANH ĐIỀU HƯỚNG
# =========================
with st.sidebar:
    st.markdown("# PNP.")
    st.caption("MEN'S SNEAKERS")

    page = st.radio(
        "KHÁM PHÁ",
        [
            "🏠 Trang chủ",
            "👟 Cửa hàng",
            "📏 Dự đoán size",
            "🎡 Vòng quay may mắn",
            "🛒 Giỏ hàng"
        ]
    )

    st.divider()
    st.write("📦 Hỗ trợ đổi size")
    st.write("☎️ Hotline: 0900 000 000")
    st.write("🚚 Giao hàng toàn quốc")

# =========================
# TRANG CHỦ
# =========================
if page == "🏠 Trang chủ":

    st.markdown("## WELCOME TO PNP")

    c1,c2,c3 = st.columns(3)

    c1.metric("Sản phẩm", "08+", "Sneaker nam")
    c2.metric("Giá bán", "399K+", "Nhiều lựa chọn")
    c3.metric("Ưu đãi", "Lucky Spin", "Nhận voucher")

    st.markdown("## 🔥 SẢN PHẨM NỔI BẬT")

    cols = st.columns(4)

    for col, p in zip(cols, PRODUCTS[:4]):
        with col:
            st.markdown(f"""
            <div class="product">
                <div style="font-size:55px;text-align:center">
                    {p['emoji']}
                </div>
                <h3>{p['name']}</h3>
                <div class="price">{money(p['price'])}</div>
                <p>{p['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="panel">
        <h2>YOUR STYLE. YOUR STEP.</h2>
        <p>Khám phá phong cách riêng cùng PNP Sneakers.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# CỬA HÀNG
# =========================
elif page == "👟 Cửa hàng":

    st.markdown("## PNP SNEAKER STORE")

    categories = ["Tất cả"] + sorted(
        set(p["category"] for p in PRODUCTS)
    )

    category = st.selectbox(
        "Danh mục",
        categories
    )

    search = st.text_input(
        "Tìm kiếm sản phẩm",
        placeholder="Nhập tên giày..."
    )

    shown = PRODUCTS

    if category != "Tất cả":
        shown = [
            p for p in shown
            if p["category"] == category
        ]

    if search:
        shown = [
            p for p in shown
            if search.lower() in p["name"].lower()
        ]

    if not shown:
        st.warning("Không tìm thấy sản phẩm.")

    for start in range(0, len(shown), 2):

        cols = st.columns(2)

        for col, p in zip(cols, shown[start:start+2]):

            with col:

                st.markdown(f"""
                <div class="product">
                    <div style="font-size:60px;text-align:center">
                        {p['emoji']}
                    </div>
                    <h3>{p['name']}</h3>
                    <div class="price">{money(p['price'])}</div>
                    <p>{p['desc']}</p>
                </div>
                """, unsafe_allow_html=True)

                with st.form(f"form_{p['name']}"):

                    size = st.selectbox(
                        "Chọn size",
                        p["sizes"],
                        key=f"size_{p['name']}"
                    )

                    qty = st.number_input(
                        "Số lượng",
                        1,10,1,
                        key=f"qty_{p['name']}"
                    )

                    add = st.form_submit_button(
                        "＋ THÊM VÀO GIỎ"
                    )

                    if add:

                        st.session_state.cart.append({
                            "name":p["name"],
                            "price":p["price"],
                            "size":size,
                            "qty":int(qty),
                            "emoji":p["emoji"]
                        })

                        st.success("Đã thêm sản phẩm vào giỏ!")

# =========================
# DỰ ĐOÁN SIZE
# =========================
elif page == "📏 Dự đoán size":

    st.markdown("## 📏 PNP SIZE FINDER")

    st.write(
        "Nhập số đo bàn chân để PNP tư vấn size giày phù hợp."
    )

    st.markdown("""
    <div class="panel">
        <h3>📌 Hướng dẫn đo chân</h3>
        1. Đặt giấy sát tường trên mặt sàn.<br>
        2. Đứng lên giấy, gót chân chạm tường.<br>
        3. Đánh dấu vị trí ngón chân dài nhất.<br>
        4. Đo khoảng cách từ tường đến dấu chân.<br>
        5. Đo thêm chiều rộng ở phần bè nhất của bàn chân.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### NHẬP SỐ ĐO")

    length = st.number_input(
        "Chiều dài bàn chân (cm)",
        min_value=18.0,
        max_value=33.0,
        value=25.0,
        step=0.1
    )

    width = st.number_input(
        "Chiều rộng bàn chân (cm)",
        min_value=6.0,
        max_value=13.0,
        value=9.5,
        step=0.1
    )

    foot = st.selectbox(
        "Đặc điểm bàn chân",
        ["Bình thường","Hơi bè","Bè rộng"]
    )

    if st.button("✨ DỰ ĐOÁN SIZE GIÀY"):

        # Công thức dự đoán tham khảo
        size = round((length + 1.2) * 1.5)

        if foot == "Hơi bè" and width >= 10:
            size += 1

        elif foot == "Bè rộng":
            size += 1

        st.session_state.size_result = size

    if st.session_state.size_result:

        size = st.session_state.size_result

        st.success(f"🎯 SIZE GỢI Ý: EU {size}")

        st.info(
            "Size chỉ mang tính tham khảo. "
            "Hãy đối chiếu bảng size riêng của từng mẫu giày."
        )

        available = sorted(
            set(s for p in PRODUCTS for s in p["sizes"])
        )

        if size in available:
            st.write(f"PNP hiện có mẫu demo với size EU {size}.")
        else:
            nearest = min(
                available,
                key=lambda x: abs(x-size)
            )
            st.write(
                f"Size gần nhất trong danh sách mẫu: EU {nearest}."
            )

# =========================
# VÒNG QUAY MAY MẮN
# =========================
elif page == "🎡 Vòng quay may mắn":

    st.markdown("## 🎡 PNP LUCKY SPIN")

    st.markdown("""
    <div class="panel" style="text-align:center">
        <div style="font-size:100px">🎡</div>
        <h2>SPIN YOUR LUCK!</h2>
        <p>Quay để nhận ưu đãi độc quyền từ PNP.</p>
        <p>🎟️ Voucher · 🧦 Quà tặng · 🚚 Freeship</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "🔥 QUAY NGAY",
        use_container_width=True
    ):

        st.session_state.prize = random.choices(
            [p[0] for p in PRIZES],
            weights=WEIGHTS,
            k=1
        )[0]

        st.balloons()

    if st.session_state.prize:

        st.success(
            f"🎉 CHÚC MỪNG! {st.session_state.prize}"
        )

        st.caption(
            "Vui lòng lưu kết quả và liên hệ shop để xác nhận ưu đãi."
        )

# =========================
# GIỎ HÀNG
# =========================
elif page == "🛒 Giỏ hàng":

    st.markdown("## 🛒 GIỎ HÀNG PNP")

    if not st.session_state.cart:

        st.info("Giỏ hàng đang trống.")

    else:

        total = 0

        for i, item in enumerate(st.session_state.cart):

            subtotal = item["price"] * item["qty"]

            total += subtotal

            a,b,c = st.columns([5,2,1])

            a.write(
                f"{item['emoji']} **{item['name']}** "
                f"| Size {item['size']}"
            )

            b.write(
                f"{item['qty']} x {money(item['price'])}"
            )

            c.write(money(subtotal))

            if st.button("Xóa", key=f"remove_{i}"):

                st.session_state.cart.pop(i)
                st.rerun()

        st.divider()

        st.markdown(f"## TỔNG TIỀN: {money(total)}")

        with st.form("checkout"):

            name = st.text_input("Họ và tên")

            phone = st.text_input("Số điện thoại")

            address = st.text_area("Địa chỉ nhận hàng")

            payment = st.selectbox(
                "Thanh toán",
                ["COD - Thanh toán khi nhận hàng",
                 "Chuyển khoản"]
            )

            confirm = st.form_submit_button(
                "✓ XÁC NHẬN ĐẶT HÀNG"
            )

            if confirm:

                if not name.strip() or not phone.strip() or not address.strip():

                    st.error("Vui lòng nhập đầy đủ thông tin.")

                else:

                    st.session_state.orders.append({
                        "name":name,
                        "phone":phone,
                        "address":address,
                        "payment":payment,
                        "total":total,
                        "items":st.session_state.cart.copy()
                    })

                    st.session_state.cart = []

                    st.success(
                        "Đặt hàng thành công! PNP sẽ liên hệ xác nhận."
                    )

    if st.button("🧹 XÓA GIỎ HÀNG"):

        st.session_state.cart = []
        st.rerun()

# =========================
# FOOTER
# =========================
st.divider()

st.markdown("""
<div style="text-align:center;padding:15px">
    <h2>PNP<span style="color:#ff6b2c">.</span></h2>
    MEN'S SNEAKERS
    <p>STEP UP YOUR GAME.</p>
</div>
""", unsafe_allow_html=True)
