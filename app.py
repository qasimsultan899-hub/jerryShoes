import streamlit as st
import pandas as pd

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SOLE — Premium Shoe Outlet",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Root tokens ── */
:root {
    --cream:   #F5F0E8;
    --charcoal:#1A1A1A;
    --gold:    #C9A84C;
    --gold-lt: #E8D5A3;
    --muted:   #6B6B6B;
    --card-bg: #FFFFFF;
    --border:  #E8E0D0;
    --danger:  #C0392B;
    --success: #27AE60;
    --radius:  12px;
    --shadow:  0 4px 24px rgba(0,0,0,0.08);
}

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--cream) !important;
    color: var(--charcoal);
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--charcoal) !important;
    border-right: 1px solid #2e2e2e;
}
[data-testid="stSidebar"] * {
    color: #EFEFEF !important;
}
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stMultiSelect label,
[data-testid="stSidebar"] .stRadio label {
    color: #AAAAAA !important;
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
[data-testid="stSidebar"] hr {
    border-color: #333 !important;
}

/* ── Main area background ── */
[data-testid="stAppViewContainer"] > .main {
    background: var(--cream) !important;
}

/* ── Headings ── */
h1, h2, h3 { font-family: 'Playfair Display', serif !important; }

/* ── Cards ── */
.shoe-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 0;
    overflow: hidden;
    box-shadow: var(--shadow);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    height: 100%;
}
.shoe-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 36px rgba(0,0,0,0.14);
}
.shoe-card-img {
    width: 100%;
    height: 210px;
    object-fit: cover;
    display: block;
}
.shoe-card-body {
    padding: 16px 18px 18px;
}
.shoe-brand {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--gold);
}
.shoe-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.05rem;
    font-weight: 700;
    margin: 4px 0 2px;
    color: var(--charcoal);
}
.shoe-category {
    font-size: 0.72rem;
    color: var(--muted);
    margin-bottom: 10px;
}
.shoe-price {
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--charcoal);
}
.shoe-price span {
    font-size: 0.78rem;
    font-weight: 400;
    color: var(--muted);
    margin-left: 2px;
}

/* ── Gold pill badge ── */
.badge {
    display: inline-block;
    background: var(--gold-lt);
    color: #7A5C1E;
    border-radius: 20px;
    font-size: 0.68rem;
    font-weight: 600;
    padding: 2px 10px;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
}

/* ── Section divider ── */
.section-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 24px 0;
}

/* ── Hero banner ── */
.hero {
    background: linear-gradient(135deg, var(--charcoal) 0%, #2C2C2C 60%, #3A3020 100%);
    border-radius: 16px;
    padding: 52px 48px;
    margin-bottom: 36px;
    position: relative;
    overflow: hidden;
}
.hero::after {
    content: '';
    position: absolute;
    right: -60px; top: -60px;
    width: 340px; height: 340px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(201,168,76,0.18) 0%, transparent 70%);
}
.hero h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.8rem;
    font-weight: 900;
    color: #FFFFFF !important;
    line-height: 1.15;
    margin: 0 0 12px;
}
.hero p {
    color: #AAAAAA !important;
    font-size: 1.05rem;
    max-width: 480px;
    margin: 0;
}
.hero-accent { color: var(--gold) !important; }

/* ── Stat bar ── */
.stat-row {
    display: flex;
    gap: 16px;
    margin-bottom: 32px;
}
.stat-box {
    flex: 1;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 18px 20px;
    text-align: center;
    box-shadow: var(--shadow);
}
.stat-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.7rem;
    font-weight: 700;
    color: var(--gold);
}
.stat-label {
    font-size: 0.72rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* ── Cart table ── */
.cart-row {
    display: flex;
    align-items: center;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 14px 18px;
    margin-bottom: 10px;
    gap: 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.cart-img {
    width: 68px; height: 68px;
    object-fit: cover;
    border-radius: 8px;
    flex-shrink: 0;
}
.cart-info { flex: 1; }
.cart-name {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 0.95rem;
}
.cart-sub { font-size: 0.75rem; color: var(--muted); margin-top: 2px; }
.cart-price { font-size: 1.1rem; font-weight: 700; color: var(--charcoal); }

/* ── Checkout total ── */
.total-box {
    background: var(--charcoal);
    color: #FFF;
    border-radius: var(--radius);
    padding: 24px 28px;
    margin-top: 20px;
}
.total-box .t-label { font-size: 0.78rem; color: #999; text-transform: uppercase; letter-spacing: 0.08em; }
.total-box .t-value {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--gold);
}

/* ── Order tracking ── */
.order-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px 24px;
    margin-bottom: 12px;
    box-shadow: var(--shadow);
}
.order-id { font-size: 0.72rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.1em; }
.order-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-weight: 700;
    margin: 4px 0;
}
.status-badge {
    display: inline-block;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 600;
    padding: 3px 12px;
    letter-spacing: 0.06em;
}
.status-delivered  { background: #D5F5E3; color: #1E8449; }
.status-shipped    { background: #D6EAF8; color: #1A5276; }
.status-processing { background: #FEF9E7; color: #9A7D0A; }
.status-cancelled  { background: #FADBD8; color: #922B21; }

/* ── Sidebar brand ── */
.sidebar-brand {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 900;
    color: #FFFFFF !important;
    letter-spacing: 0.04em;
}
.sidebar-tagline {
    font-size: 0.68rem;
    color: var(--gold) !important;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    margin-top: -4px;
}

/* ── Button overrides ── */
.stButton > button {
    background: var(--charcoal) !important;
    color: #FFF !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    padding: 8px 20px !important;
    transition: background 0.2s ease !important;
}
.stButton > button:hover {
    background: var(--gold) !important;
    color: var(--charcoal) !important;
}
.stButton > button[kind="primary"] {
    background: var(--gold) !important;
    color: var(--charcoal) !important;
}

/* ── Selectbox / slider accent ── */
[data-testid="stSlider"] .st-bw { background: var(--gold) !important; }

/* ── Hide default streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  INVENTORY DATA
# ─────────────────────────────────────────────
INVENTORY = [
    {"id": 1,  "name": "Air Monarch IV",      "brand": "Nike",   "category": "Sneakers", "price": 89,  "sizes": [7,8,9,10,11,12], "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&q=80"},
    {"id": 2,  "name": "Ultraboost 22",        "brand": "Adidas", "category": "Running",  "price": 180, "sizes": [7,8,9,10,11],    "image": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=600&q=80"},
    {"id": 3,  "name": "Suede Classic XXI",    "brand": "Puma",   "category": "Sneakers", "price": 70,  "sizes": [8,9,10,11,12],   "image": "https://images.unsplash.com/photo-1516478177764-9fe5bd7e9717?w=600&q=80"},
    {"id": 4,  "name": "Chuck Taylor All Star","brand": "Converse","category":"Sneakers", "price": 60,  "sizes": [6,7,8,9,10,11],  "image": "https://images.unsplash.com/photo-1463100099107-aa0980cbb2b1?w=600&q=80"},
    {"id": 5,  "name": "Classic Leather",      "brand": "Reebok", "category": "Formal",   "price": 75,  "sizes": [7,8,9,10,11],    "image": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?w=600&q=80"},
    {"id": 6,  "name": "Gel-Nimbus 25",        "brand": "Asics",  "category": "Running",  "price": 160, "sizes": [8,9,10,11,12],   "image": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=600&q=80"},
    {"id": 7,  "name": "Fresh Foam 1080v12",   "brand": "New Balance","category":"Running","price":165, "sizes": [7,8,9,10,11,12], "image": "https://images.unsplash.com/photo-1556906781-9a412961d28c?w=600&q=80"},
    {"id": 8,  "name": "Old Skool",            "brand": "Vans",   "category": "Sneakers", "price": 65,  "sizes": [6,7,8,9,10,11],  "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=600&q=80"},
    {"id": 9,  "name": "React Infinity Run 3", "brand": "Nike",   "category": "Running",  "price": 160, "sizes": [8,9,10,11],      "image": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=600&q=80"},
    {"id": 10, "name": "Forum Low",            "brand": "Adidas", "category": "Sneakers", "price": 90,  "sizes": [7,8,9,10,11,12], "image": "https://images.unsplash.com/photo-1605408499391-6368c628ef42?w=600&q=80"},
    {"id": 11, "name": "Oxford Brogue Elite",  "brand": "Clarks", "category": "Formal",   "price": 120, "sizes": [7,8,9,10,11],    "image": "https://images.unsplash.com/photo-1533867617858-e7b97e060509?w=600&q=80"},
    {"id": 12, "name": "Speedcat OG",          "brand": "Puma",   "category": "Sneakers", "price": 80,  "sizes": [8,9,10,11,12],   "image": "https://images.unsplash.com/photo-1584735175315-9d5df23be620?w=600&q=80"},
]

MOCK_ORDERS = [
    {"order_id": "ORD-2024-001", "customer": "Alex Johnson",   "item": "Air Monarch IV",    "brand": "Nike",   "size": 10, "qty": 1, "total": 89,  "status": "Delivered"},
    {"order_id": "ORD-2024-002", "customer": "Maria Garcia",   "item": "Ultraboost 22",     "brand": "Adidas", "size": 9,  "qty": 2, "total": 360, "status": "Shipped"},
    {"order_id": "ORD-2024-003", "customer": "James Chen",     "item": "Classic Leather",   "brand": "Reebok", "size": 11, "qty": 1, "total": 75,  "status": "Processing"},
    {"order_id": "ORD-2024-004", "customer": "Sarah Williams", "item": "Chuck Taylor",      "brand": "Converse","size":8,  "qty": 1, "total": 60,  "status": "Delivered"},
    {"order_id": "ORD-2024-005", "customer": "David Park",     "item": "Gel-Nimbus 25",     "brand": "Asics",  "size": 10, "qty": 1, "total": 160, "status": "Cancelled"},
    {"order_id": "ORD-2024-006", "customer": "Emily Brown",    "item": "Fresh Foam 1080v12","brand": "New Balance","size":9,"qty": 1, "total": 165, "status": "Shipped"},
]

df = pd.DataFrame(INVENTORY)

# ─────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────
if "cart" not in st.session_state:
    st.session_state.cart = []          # list of dicts
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home / Shop"
if "checkout_done" not in st.session_state:
    st.session_state.checkout_done = False

# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-brand">SOLE.</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">Premium Shoe Outlet</div>', unsafe_allow_html=True)
    st.markdown("---")

    cart_count = len(st.session_state.cart)
    cart_label = f"🛒 Cart ({cart_count})" if cart_count else "🛒 Cart"

    page = st.radio(
        "Navigate",
        ["🏠 Home / Shop", cart_label, "📦 Order Tracking"],
        index=["🏠 Home / Shop", cart_label, "📦 Order Tracking"].index(
            st.session_state.page
        ) if st.session_state.page in ["🏠 Home / Shop", cart_label, "📦 Order Tracking"] else 0,
        label_visibility="collapsed",
    )
    st.session_state.page = page
    st.markdown("---")

    # ── Filters (only on shop page) ──
    if "Home" in page:
        st.markdown("**FILTER BY**")
        all_brands = sorted(df["brand"].unique())
        sel_brands = st.multiselect("Brand", all_brands, default=all_brands, label_visibility="visible")

        price_min, price_max = int(df["price"].min()), int(df["price"].max())
        sel_price = st.slider("Price Range ($)", price_min, price_max, (price_min, price_max))

        all_cats = sorted(df["category"].unique())
        sel_cats = st.multiselect("Category", all_cats, default=all_cats)

        sort_opt = st.selectbox("Sort By", ["Price: Low → High", "Price: High → Low", "Name A–Z"])
    else:
        sel_brands = list(df["brand"].unique())
        sel_cats   = list(df["category"].unique())
        sel_price  = (int(df["price"].min()), int(df["price"].max()))
        sort_opt   = "Price: Low → High"

    st.markdown("---")
    st.markdown('<div style="font-size:0.68rem;color:#555;text-align:center;">© 2024 SOLE Outlet</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def add_to_cart(product: dict, size: int):
    st.session_state.cart.append({
        "id":       product["id"],
        "name":     product["name"],
        "brand":    product["brand"],
        "size":     size,
        "price":    product["price"],
        "image":    product["image"],
        "category": product["category"],
    })

def remove_from_cart(idx: int):
    st.session_state.cart.pop(idx)

def cart_total() -> float:
    return sum(item["price"] for item in st.session_state.cart)

def status_class(s: str) -> str:
    return {"Delivered": "status-delivered",
            "Shipped":   "status-shipped",
            "Processing":"status-processing",
            "Cancelled": "status-cancelled"}.get(s, "")

# ─────────────────────────────────────────────
#  PAGE: HOME / SHOP
# ─────────────────────────────────────────────
def page_shop():
    # Hero
    st.markdown("""
    <div class="hero">
      <h1>Step Into <span class="hero-accent">Luxury.</span></h1>
      <p>Curated footwear from the world's leading brands — sport, style, and everything in between.</p>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown(f"""
    <div class="stat-row">
      <div class="stat-box"><div class="stat-value">{len(INVENTORY)}+</div><div class="stat-label">Products</div></div>
      <div class="stat-box"><div class="stat-value">{len(df['brand'].unique())}</div><div class="stat-label">Brands</div></div>
      <div class="stat-box"><div class="stat-value">3</div><div class="stat-label">Categories</div></div>
      <div class="stat-box"><div class="stat-value">Free</div><div class="stat-label">Shipping $99+</div></div>
    </div>
    """, unsafe_allow_html=True)

    # Filter
    filtered = df[
        (df["brand"].isin(sel_brands)) &
        (df["category"].isin(sel_cats)) &
        (df["price"] >= sel_price[0]) &
        (df["price"] <= sel_price[1])
    ]
    if sort_opt == "Price: Low → High":
        filtered = filtered.sort_values("price")
    elif sort_opt == "Price: High → Low":
        filtered = filtered.sort_values("price", ascending=False)
    else:
        filtered = filtered.sort_values("name")

    st.markdown(f'<p style="color:var(--muted);font-size:0.82rem;margin-bottom:20px;">{len(filtered)} products found</p>', unsafe_allow_html=True)

    if filtered.empty:
        st.info("No products match your filters. Try adjusting the sidebar.")
        return

    # Grid – 3 columns
    cols_per_row = 3
    products = filtered.to_dict("records")
    for row_start in range(0, len(products), cols_per_row):
        row_products = products[row_start: row_start + cols_per_row]
        cols = st.columns(cols_per_row, gap="medium")
        for col, product in zip(cols, row_products):
            with col:
                # Card HTML (non-interactive part)
                st.markdown(f"""
                <div class="shoe-card">
                  <img class="shoe-card-img" src="{product['image']}" alt="{product['name']}"/>
                  <div class="shoe-card-body">
                    <div class="shoe-brand">{product['brand']}</div>
                    <div class="shoe-name">{product['name']}</div>
                    <div class="shoe-category">{product['category']}</div>
                    <div class="shoe-price">${product['price']}<span>USD</span></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

                # Interactive controls below card
                size_key  = f"size_{product['id']}"
                btn_key   = f"add_{product['id']}"
                sel_size  = st.selectbox(
                    "Size (US)",
                    product["sizes"],
                    key=size_key,
                    label_visibility="collapsed",
                )
                if st.button("Add to Cart", key=btn_key, use_container_width=True):
                    add_to_cart(product, sel_size)
                    st.toast(f"✅ {product['name']} (Size {sel_size}) added to cart!", icon="👟")

        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  PAGE: CART
# ─────────────────────────────────────────────
def page_cart():
    st.markdown("## 🛒 Your Cart")

    if st.session_state.checkout_done:
        st.success("🎉 **Order placed successfully!** Thank you for shopping at SOLE. You'll receive a confirmation shortly.")
        if st.button("Continue Shopping"):
            st.session_state.checkout_done = False
            st.session_state.cart = []
            st.session_state.page = "🏠 Home / Shop"
            st.rerun()
        return

    if not st.session_state.cart:
        st.markdown("""
        <div style="text-align:center;padding:60px 0;">
          <div style="font-size:3rem;">👟</div>
          <h3 style="font-family:'Playfair Display',serif;margin:12px 0 6px;">Your cart is empty</h3>
          <p style="color:var(--muted);">Discover our curated collection and find your perfect pair.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Browse Products", use_container_width=False):
            st.session_state.page = "🏠 Home / Shop"
            st.rerun()
        return

    # Cart items
    to_remove = None
    for i, item in enumerate(st.session_state.cart):
        col_img, col_info, col_price, col_remove = st.columns([1, 4, 2, 1])
        with col_img:
            st.image(item["image"], width=80)
        with col_info:
            st.markdown(f"""
            <div class="cart-name">{item['name']}</div>
            <div class="cart-sub">{item['brand']} · {item['category']} · Size US {item['size']}</div>
            """, unsafe_allow_html=True)
        with col_price:
            st.markdown(f'<div class="cart-price" style="padding-top:18px;">${item["price"]}</div>', unsafe_allow_html=True)
        with col_remove:
            if st.button("✕", key=f"remove_{i}", help="Remove item"):
                to_remove = i
        st.markdown('<hr style="border-color:var(--border);margin:6px 0;">', unsafe_allow_html=True)

    if to_remove is not None:
        remove_from_cart(to_remove)
        st.rerun()

    # Summary
    total = cart_total()
    shipping = 0 if total >= 99 else 9.99
    tax = round(total * 0.08, 2)
    grand = round(total + shipping + tax, 2)

    st.markdown(f"""
    <div class="total-box">
      <table style="width:100%;color:#ccc;font-size:0.85rem;">
        <tr><td>Subtotal</td><td style="text-align:right;">${total:.2f}</td></tr>
        <tr><td>Shipping</td><td style="text-align:right;">{'FREE' if shipping == 0 else f'${shipping:.2f}'}</td></tr>
        <tr><td>Tax (8%)</td><td style="text-align:right;">${tax:.2f}</td></tr>
        <tr><td colspan="2"><hr style="border-color:#333;margin:8px 0;"></td></tr>
        <tr><td class="t-label">TOTAL</td>
            <td style="text-align:right;" class="t-label">AMOUNT DUE</td></tr>
        <tr><td colspan="2" style="text-align:center;">
            <div class="t-value">${grand:.2f}</div>
        </td></tr>
      </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("✅  Checkout Now", use_container_width=True):
            st.session_state.checkout_done = True
            st.rerun()
    with col2:
        if st.button("🗑 Clear Cart", use_container_width=True):
            st.session_state.cart = []
            st.rerun()

    if shipping > 0:
        st.caption(f"💡 Add ${99 - total:.2f} more to qualify for **FREE shipping**.")


# ─────────────────────────────────────────────
#  PAGE: ORDER TRACKING / ADMIN
# ─────────────────────────────────────────────
def page_orders():
    st.markdown("## 📦 Order Tracking & Admin")

    tab_track, tab_admin = st.tabs(["🔍 Track My Order", "🛠 Admin Dashboard"])

    # ── Track tab ──
    with tab_track:
        st.markdown('<p style="color:var(--muted);font-size:0.9rem;">Enter your order ID to check status.</p>', unsafe_allow_html=True)
        order_input = st.text_input("Order ID", placeholder="e.g. ORD-2024-001")

        if order_input:
            match = next((o for o in MOCK_ORDERS if o["order_id"].upper() == order_input.upper()), None)
            if match:
                sc = status_class(match["status"])
                st.markdown(f"""
                <div class="order-card">
                  <div class="order-id">{match['order_id']}</div>
                  <div class="order-name">{match['item']}</div>
                  <div style="font-size:0.8rem;color:var(--muted);margin:2px 0 10px;">
                    {match['brand']} · Size US {match['size']} · Qty {match['qty']}
                  </div>
                  <div style="display:flex;justify-content:space-between;align-items:center;">
                    <span class="status-badge {sc}">{match['status']}</span>
                    <span style="font-weight:700;font-size:1.1rem;">${match['total']}</span>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("No order found with that ID. Please check and try again.")

        st.markdown("**Sample Order IDs to try:**")
        for o in MOCK_ORDERS:
            sc = status_class(o["status"])
            st.markdown(f'`{o["order_id"]}` &nbsp; <span class="status-badge {sc}">{o["status"]}</span>', unsafe_allow_html=True)

    # ── Admin tab ──
    with tab_admin:
        orders_df = pd.DataFrame(MOCK_ORDERS)

        # KPI row
        total_rev  = orders_df[orders_df["status"] != "Cancelled"]["total"].sum()
        delivered  = (orders_df["status"] == "Delivered").sum()
        processing = (orders_df["status"] == "Processing").sum()
        shipped    = (orders_df["status"] == "Shipped").sum()

        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Total Revenue", f"${total_rev:,}")
        k2.metric("Delivered",  delivered)
        k3.metric("Shipped",    shipped)
        k4.metric("Processing", processing)

        st.markdown("---")
        st.markdown("**All Orders**")

        # Colour-code status
        def highlight_status(val):
            colours = {
                "Delivered":  "background-color:#D5F5E3;color:#1E8449",
                "Shipped":    "background-color:#D6EAF8;color:#1A5276",
                "Processing": "background-color:#FEF9E7;color:#9A7D0A",
                "Cancelled":  "background-color:#FADBD8;color:#922B21",
            }
            return colours.get(val, "")

        styled = orders_df.style.applymap(highlight_status, subset=["status"])
        st.dataframe(styled, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.markdown("**Revenue by Brand** (active orders only)")
        rev_brand = (
            orders_df[orders_df["status"] != "Cancelled"]
            .groupby("brand")["total"]
            .sum()
            .reset_index()
            .sort_values("total", ascending=False)
        )
        st.bar_chart(rev_brand.set_index("brand"))

        st.markdown("**Full Inventory Snapshot**")
        st.dataframe(df[["name","brand","category","price"]].rename(columns={
            "name":"Product","brand":"Brand","category":"Category","price":"Price ($)"
        }), use_container_width=True, hide_index=True)


# ─────────────────────────────────────────────
#  ROUTER
# ─────────────────────────────────────────────
current = st.session_state.page
if "Home" in current:
    page_shop()
elif "Cart" in current:
    page_cart()
elif "Order" in current or "Tracking" in current:
    page_orders()
