from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>DEMO STORE</title>

<style>

* {
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    background: #fff9f5;
    color: #273044;
}

/* ================= HEADER ================= */

header {
    background: rgba(255,255,255,0.95);
    padding: 15px 5%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 3px 15px rgba(100,100,100,0.08);
}

.logo {
    font-size: 25px;
    font-weight: bold;
    color: #4b8dcc;
}

.logo span {
    color: #ff7fa9;
}

nav a {
    text-decoration: none;
    color: #273044;
    margin: 0 12px;
    font-weight: bold;
}

nav a:hover {
    color: #ff6f9d;
}

.search {
    background: #f3f6fa;
    border-radius: 30px;
    padding: 10px 18px;
    border: none;
    outline: none;
}

/* ================= HERO ================= */

.hero {
    width: 94%;
    max-width: 1450px;
    margin: 20px auto;
    padding: 65px 7%;
    border-radius: 30px;

    background:
        radial-gradient(circle at 80% 20%, #ffd6e5 0, transparent 25%),
        radial-gradient(circle at 20% 80%, #cceeff 0, transparent 30%),
        linear-gradient(135deg, #eaf7ff, #fff1f7);

    display: flex;
    align-items: center;
    justify-content: space-between;
    overflow: hidden;
}

.hero-text {
    max-width: 600px;
}

.hero small {
    background: #ffffff;
    padding: 8px 15px;
    border-radius: 20px;
    color: #ff6f9d;
    font-weight: bold;
}

.hero h1 {
    font-size: 55px;
    margin: 20px 0 10px;
}

.hero h1 span {
    color: #4e9ddd;
}

.hero p {
    font-size: 19px;
    color: #667085;
}

.hero button {
    margin-top: 15px;
    background: #ff76a8;
    color: white;
    border: none;
    padding: 15px 28px;
    border-radius: 30px;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
}

.hero button:hover {
    transform: translateY(-3px);
    background: #ff5c98;
}

.hero-products {
    font-size: 110px;
    line-height: 1.2;
}

/* ================= SECTION ================= */

.container {
    width: 92%;
    max-width: 1250px;
    margin: 45px auto;
}

.section-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.section-title h2 {
    font-size: 28px;
}

.section-title a {
    color: #579bd5;
    text-decoration: none;
}

/* ================= CATEGORY ================= */

.categories {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    gap: 15px;
}

.category {
    padding: 20px 10px;
    text-align: center;
    border-radius: 20px;
    font-weight: bold;
    transition: 0.2s;
}

.category:hover {
    transform: translateY(-5px);
}

.category .emoji {
    font-size: 40px;
    display: block;
    margin-bottom: 8px;
}

.cat1 { background: #ffe3ed; }
.cat2 { background: #dff2ff; }
.cat3 { background: #e1f7ed; }
.cat4 { background: #fff0ce; }
.cat5 { background: #e9e1ff; }
.cat6 { background: #dff8f7; }
.cat7 { background: #e7edff; }
.cat8 { background: #f1e5ff; }

/* ================= PRODUCTS ================= */

.products {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
}

.product {
    background: white;
    padding: 15px;
    border-radius: 22px;
    box-shadow: 0 8px 25px rgba(80,90,120,0.08);
    transition: 0.25s;
    position: relative;
}

.product:hover {
    transform: translateY(-7px);
    box-shadow: 0 15px 30px rgba(80,90,120,0.15);
}

.product-img {
    height: 180px;
    border-radius: 17px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 90px;
}

.pink { background: #fff0f5; }
.blue { background: #eaf6ff; }
.green { background: #eafaf2; }
.yellow { background: #fff8df; }

.product h3 {
    margin: 14px 5px 7px;
}

.rating {
    color: #ffb52e;
    font-size: 14px;
}

.price {
    color: #ff5f91;
    font-size: 19px;
    font-weight: bold;
    margin: 8px 5px;
}

.old-price {
    color: #aaa;
    text-decoration: line-through;
    font-size: 13px;
    margin-left: 5px;
}

.buy-btn {
    width: 100%;
    border: none;
    background: #ff79a8;
    color: white;
    padding: 11px;
    border-radius: 15px;
    cursor: pointer;
    font-weight: bold;
}

.buy-btn:hover {
    background: #ff5b96;
}

/* ================= FLASH SALE ================= */

.flash {
    background: linear-gradient(135deg, #ffe6ef, #f1e9ff);
    padding: 30px;
    border-radius: 28px;
}

.flash-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.countdown {
    background: white;
    padding: 10px 18px;
    border-radius: 20px;
    color: #ff5e91;
    font-weight: bold;
}

/* ================= PROMOTION ================= */

.promotions {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    gap: 20px;
}

.promo {
    padding: 30px;
    border-radius: 25px;
    min-height: 170px;
}

.promo h2 {
    font-size: 27px;
}

.promo-main {
    background: #dff3ff;
}

.promo-pink {
    background: #ffe1ec;
}

.promo-yellow {
    background: #fff0c9;
}

/* ================= BENEFITS ================= */

.benefits {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 20px;
}

.benefit {
    background: white;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}

.benefit-icon {
    font-size: 40px;
}

/* ================= REVIEWS ================= */

.reviews {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 20px;
}

.review {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}

.stars {
    color: #ffb52e;
}

/* ================= NEWSLETTER ================= */

.newsletter {
    background: linear-gradient(135deg,#dff2ff,#ffe4ef);
    padding: 45px;
    border-radius: 30px;
    text-align: center;
}

.newsletter input {
    width: 300px;
    max-width: 90%;
    padding: 14px 20px;
    border: none;
    border-radius: 30px;
    margin-top: 15px;
    outline: none;
}

.newsletter button {
    padding: 14px 22px;
    border: none;
    border-radius: 30px;
    background: #ff77a7;
    color: white;
    font-weight: bold;
}

/* ================= FOOTER ================= */

footer {
    margin-top: 60px;
    background: #273044;
    color: white;
    padding: 45px 7%;
}

.footer-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 30px;
}

footer h3 {
    color: #8fd1ff;
}

footer a {
    color: #ddd;
    display: block;
    margin: 10px 0;
    text-decoration: none;
}

.copyright {
    border-top: 1px solid #495267;
    margin-top: 30px;
    padding-top: 20px;
    text-align: center;
}

/* ================= ORDER FORM ================= */

#background {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(30,40,60,0.5);
    z-index: 200;
}

#orderForm {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    width: 90%;
    max-width: 430px;
    background: white;
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.25);
    z-index: 300;
}

#orderForm h2 {
    color: #ff6598;
}

#orderForm input {
    width: 100%;
    padding: 13px;
    margin: 7px 0;
    border: 1px solid #ddd;
    border-radius: 12px;
    outline: none;
}

.form-btn {
    width: 100%;
    margin-top: 10px;
    padding: 13px;
    border: none;
    border-radius: 13px;
    cursor: pointer;
    font-weight: bold;
}

.confirm {
    background: #ff77a7;
    color: white;
}

.cancel {
    background: #edf0f5;
    color: #555;
}

/* ================= RESPONSIVE ================= */

@media(max-width:900px) {

    .categories {
        grid-template-columns: repeat(4,1fr);
    }

    .products {
        grid-template-columns: repeat(2,1fr);
    }

    .benefits {
        grid-template-columns: repeat(2,1fr);
    }

    .promotions {
        grid-template-columns: 1fr;
    }

    .footer-grid {
        grid-template-columns: 1fr 1fr;
    }

    .hero-products {
        display: none;
    }

}

@media(max-width:600px) {

    nav {
        display: none;
    }

    .search {
        width: 130px;
    }

    .hero {
        padding: 40px 25px;
    }

    .hero h1 {
        font-size: 38px;
    }

    .categories {
        grid-template-columns: repeat(2,1fr);
    }

    .products {
        grid-template-columns: 1fr;
    }

    .reviews {
        grid-template-columns: 1fr;
    }

    .benefits {
        grid-template-columns: 1fr;
    }

    .footer-grid {
        grid-template-columns: 1fr;
    }
}

</style>
</head>


<body>


<!-- ================= HEADER ================= -->

<header>

    <div class="logo">
        🛍️ DEMO <span>STORE</span>
    </div>

    <nav>
        <a href="#home">HOME</a>
        <a href="#products">SẢN PHẨM</a>
        <a href="#sale">🔥 SALE</a>
        <a href="#about">GIỚI THIỆU</a>
        <a href="#contact">LIÊN HỆ</a>
    </nav>

    <input
        class="search"
        type="text"
        placeholder="🔎 Tìm sản phẩm..."
    >

</header>


<!-- ================= HERO ================= -->

<section class="hero" id="home">

    <div class="hero-text">

        <small>✨ WELCOME TO DEMO STORE</small>

        <h1>
            Mua sắm <span>chill</span><br>
            Giá cực xinh 💖
        </h1>

        <p>
            Thời trang • Công nghệ • Phụ kiện
            <br>
            Đẹp - chất - giá tốt - giao nhanh 🚚
        </p>

        <button onclick="location.href='#products'">
            🛒 MUA NGAY →
        </button>

    </div>

    <div class="hero-products">
        👕 🎒 👟
        <br>
        💻 🎧 📱
    </div>

</section>


<!-- ================= CATEGORY ================= -->

<div class="container">

    <div class="section-title">
        <h2>🛍️ Danh mục sản phẩm</h2>
        <a href="#products">Xem tất cả →</a>
    </div>

    <div class="categories">

        <div class="category cat1">
            <span class="emoji">👕</span>
            Thời trang
        </div>

        <div class="category cat2">
            <span class="emoji">👖</span>
            Quần
        </div>

        <div class="category cat3">
            <span class="emoji">👟</span>
            Giày
        </div>

        <div class="category cat4">
            <span class="emoji">🎒</span>
            Balo
        </div>

        <div class="category cat5">
            <span class="emoji">🎧</span>
            Phụ kiện
        </div>

        <div class="category cat6">
            <span class="emoji">📱</span>
            Điện thoại
        </div>

        <div class="category cat7">
            <span class="emoji">💻</span>
            Laptop
        </div>

        <div class="category cat8">
            <span class="emoji">✨</span>
            Khác
        </div>

    </div>

</div>


<!-- ================= BÁN CHẠY ================= -->

<div class="container" id="products">

    <div class="section-title">
        <h2>🔥 Sản phẩm bán chạy</h2>
        <a href="#products">Xem tất cả →</a>
    </div>

    <div class="products">


        <div class="product">

            <div class="product-img pink">👕</div>

            <h3>Áo thun Basic</h3>

            <div class="rating">
                ⭐ 4.8
            </div>

            <div class="price">
                200.000đ
            </div>

            <button
                class="buy-btn"
                onclick="buy('Áo thun Basic','200.000đ')">
                🛒 Mua ngay
            </button>

        </div>


        <div class="product">

            <div class="product-img blue">👖</div>

            <h3>Jean Short</h3>

            <div class="rating">
                ⭐ 4.7
            </div>

            <div class="price">
                300.000đ
            </div>

            <button
                class="buy-btn"
                onclick="buy('Jean Short','300.000đ')">
                🛒 Mua ngay
            </button>

        </div>


        <div class="product">

            <div class="product-img green">👟</div>

            <h3>Giày Sneaker</h3>

            <div class="rating">
                ⭐ 4.9
            </div>

            <div class="price">
                500.000đ
            </div>

            <button
                class="buy-btn"
                onclick="buy('Giày Sneaker','500.000đ')">
                🛒 Mua ngay
            </button>

        </div>


        <div class="product">

            <div class="product-img yellow">🎒</div>

            <h3>Balo Của Long</h3>

            <div class="rating">
                ⭐ 4.6
            </div>

            <div class="price">
                300.000đ
            </div>

            <button
                class="buy-btn"
                onclick="buy('Balo Của Long','300.000đ')">
                🛒 Mua ngay
            </button>

        </div>


    </div>

</div>


<!-- ================= FLASH SALE ================= -->

<div class="container" id="sale">

    <div class="flash">

        <div class="flash-header">

            <h2>⚡ Flash Sale</h2>

            <div class="countdown">
                ⏰ 02 : 14 : 32
            </div>

        </div>

        <div class="products">


            <div class="product">

                <div class="product-img pink">👕</div>

                <h3>Áo thun Oversize</h3>

                <div class="price">
                    140.000đ
                    <span class="old-price">200.000đ</span>
                </div>

                <button
                    class="buy-btn"
                    onclick="buy('Áo thun Oversize','140.000đ')">
                    🔥 Mua ngay
                </button>

            </div>


            <div class="product">

                <div class="product-img blue">👟</div>

                <h3>Giày Sneaker</h3>

                <div class="price">
                    375.000đ
                    <span class="old-price">500.000đ</span>
                </div>

                <button
                    class="buy-btn"
                    onclick="buy('Giày Sneaker Sale','375.000đ')">
                    🔥 Mua ngay
                </button>

            </div>


            <div class="product">

                <div class="product-img yellow">🎒</div>

                <h3>Balo thời trang</h3>

                <div class="price">
                    240.000đ
                    <span class="old-price">300.000đ</span>
                </div>

                <button
                    class="buy-btn"
                    onclick="buy('Balo thời trang','240.000đ')">
                    🔥 Mua ngay
                </button>

            </div>

        </div>

    </div>

</div>


<!-- ================= SẢN PHẨM MỚI ================= -->

<div class="container">

    <div class="section-title">
        <h2>✨ Sản phẩm mới</h2>
        <a href="#products">Xem tất cả →</a>
    </div>

    <div class="products">


        <div class="product">

            <div class="product-img pink">🧥</div>

            <h3>Áo Hoodie</h3>

            <div class="rating">⭐ 4.7</div>

            <div class="price">350.000đ</div>

            <button
                class="buy-btn"
                onclick="buy('Áo Hoodie','350.000đ')">
                🛒 Mua ngay
            </button>

        </div>


        <div class="product">

            <div class="product-img yellow">👖</div>

            <h3>Quần Cargo</h3>

            <div class="rating">⭐ 4.8</div>

            <div class="price">400.000đ</div>

            <button
                class="buy-btn"
                onclick="buy('Quần Cargo','400.000đ')">
                🛒 Mua ngay
            </button>

        </div>


        <div class="product">

            <div class="product-img blue">📱</div>

            <h3>Điện thoại</h3>

            <div class="rating">⭐ 4.9</div>

            <div class="price">8.000.000đ</div>

            <button
                class="buy-btn"
                onclick="buy('Điện thoại Của Long','8.000.000đ')">
                🛒 Mua ngay
            </button>

        </div>


        <div class="product">

            <div class="product-img green">🎧</div>

            <h3>Tai nghe Bluetooth</h3>

            <div class="rating">⭐ 4.8</div>

            <div class="price">700.000đ</div>

            <button
                class="buy-btn"
                onclick="buy('Tai nghe Bluetooth','700.000đ')">
                🛒 Mua ngay
            </button>

        </div>

    </div>

</div>


<!-- ================= ƯU ĐÃI ================= -->

<div class="container">

    <div class="section-title">
        <h2>🎁 Ưu đãi hôm nay</h2>
    </div>

    <div class="promotions">

        <div class="promo promo-main">

            <h2>🚚 FREESHIP TOÀN QUỐC</h2>

            <p>
                Cho đơn từ 300.000đ
            </p>

            <b>SHOP CỦA LONG 💙</b>

        </div>


        <div class="promo promo-pink">

            <h2>💖 GIẢM 10%</h2>

            <p>
                Cho khách hàng mới
            </p>

        </div>


        <div class="promo promo-yellow">

            <h2>🎁 TÍCH ĐIỂM</h2>

            <p>
                Mỗi đơn hàng
            </p>

        </div>

    </div>

</div>


<!-- ================= LÝ DO CHỌN SHOP ================= -->

<div class="container" id="about">

    <div class="section-title">
        <h2>💙 Vì sao chọn SHOP CỦA LONG?</h2>
    </div>

    <div class="benefits">

        <div class="benefit">

            <div class="benefit-icon">🛡️</div>

            <h3>Sản phẩm chất lượng</h3>

            <p>
                Kiểm tra kỹ trước khi giao
            </p>

        </div>


        <div class="benefit">

            <div class="benefit-icon">💰</div>

            <h3>Giá tốt</h3>

            <p>
                Nhiều ưu đãi hấp dẫn
            </p>

        </div>


        <div class="benefit">

            <div class="benefit-icon">🚚</div>

            <h3>Giao hàng nhanh</h3>

            <p>
                Hỗ trợ giao toàn quốc
            </p>

        </div>


        <div class="benefit">

            <div class="benefit-icon">🎧</div>

            <h3>Hỗ trợ 24/7</h3>

            <p>
                Luôn sẵn sàng hỗ trợ
            </p>

        </div>

    </div>

</div>


<!-- ================= ĐÁNH GIÁ ================= -->

<div class="container">

    <div class="section-title">
        <h2>💬 Khách hàng nói gì?</h2>
    </div>

    <div class="reviews">


        <div class="review">

            <h3>👩 Minh Anh</h3>

            <div class="stars">
                ⭐⭐⭐⭐⭐
            </div>

            <p>
                "Shop đẹp, hàng chất lượng,
                giao nhanh nữa. Sẽ ủng hộ lâu dài!"
            </p>

        </div>


        <div class="review">

            <h3>👩 Quỳnh Chi</h3>

            <div class="stars">
                ⭐⭐⭐⭐⭐
            </div>

            <p>
                "Giá hợp lý, đóng gói cẩn thận,
                shop tư vấn nhiệt tình!"
            </p>

        </div>


        <div class="review">

            <h3>👨 Hoàng Nam</h3>

            <div class="stars">
                ⭐⭐⭐⭐⭐
            </div>

            <p>
                "Mình mua laptop ở đây,
                máy đẹp và chạy rất mượt!"
            </p>

        </div>


    </div>

</div>


<!-- ================= NEWSLETTER ================= -->

<div class="container">

    <div class="newsletter">

        <h2>💌 Nhận ưu đãi từ SHOP CỦA LONG</h2>

        <p>
            Đăng ký để nhận mã giảm giá mới nhất!
        </p>

        <input
            type="email"
            placeholder="Nhập email của bạn..."
        >

        <button onclick="alert('🎉 Đăng ký thành công!')">
            Đăng ký
        </button>

    </div>

</div>


<!-- ================= FORM ĐẶT HÀNG ================= -->

<div id="background"></div>

<div id="orderForm">

    <h2>🛒 Đặt hàng</h2>

    <p id="product"></p>

    <p id="price"></p>

    <input
        type="text"
        id="name"
        placeholder="👤 Họ và tên"
    >

    <input
        type="text"
        id="phone"
        placeholder="📱 Số điện thoại"
    >

    <input
        type="text"
        id="address"
        placeholder="📍 Địa chỉ nhận hàng"
    >

    <button
        class="form-btn confirm"
        onclick="confirmOrder()">
        ✅ Xác nhận đặt hàng
    </button>

    <button
        class="form-btn cancel"
        onclick="closeForm()">
        ❌ Hủy
    </button>

</div>


<!-- ================= FOOTER ================= -->

<footer id="contact">

    <div class="footer-grid">


        <div>

            <h2>🛍️ DEMO STORE</h2>

            <p>
                Mua sắm chill - Giá xinh -
                Giao nhanh 💙
            </p>

            <p>
                ⭐ Uy tín • Chất lượng • Tận tâm
            </p>

        </div>


        <div>

            <h3>SHOP</h3>

            <a href="#home">Trang chủ</a>
            <a href="#products">Sản phẩm</a>
            <a href="#sale">Sale</a>

        </div>


        <div>

            <h3>HỖ TRỢ</h3>

            <a href="#contact">Liên hệ</a>
            <a href="#about">Giới thiệu</a>
            <a href="#">Chính sách</a>

        </div>


        <div>

            <h3>LIÊN HỆ</h3>

            <p>📞 0982618795</p>
            <p>📧 viet2222223@gmail.com</p>
            <p>📍 Hà Nội</p>

        </div>


    </div>


    <div class="copyright">

        © 2026 DEMO STORE
        <br>
        Cảm ơn bạn đã ủng hộ 💖

    </div>

</footer>


<script>

let currentProduct = "";
let currentPrice = "";


function buy(productName, productPrice) {

    currentProduct = productName;
    currentPrice = productPrice;

    document.getElementById("product").innerHTML =
        "📦 Sản phẩm: <b>" + productName + "</b>";

    document.getElementById("price").innerHTML =
        "💰 Giá: <b>" + productPrice + "</b>";

    document.getElementById("orderForm").style.display = "block";

    document.getElementById("background").style.display = "block";
}


function confirmOrder() {

    let name =
        document.getElementById("name").value.trim();

    let phone =
        document.getElementById("phone").value.trim();

    let address =
        document.getElementById("address").value.trim();


    if (name == "" || phone == "" || address == "") {

        alert("⚠️ Vui lòng nhập đầy đủ thông tin!");

        return;
    }


    alert(
        "🎉 ĐẶT HÀNG THÀNH CÔNG!\\n\\n" +

        "📦 Sản phẩm: " +
        currentProduct +

        "\\n💰 Giá: " +
        currentPrice +

        "\\n👤 Họ tên: " +
        name +

        "\\n📱 SĐT: " +
        phone +

        "\\n📍 Địa chỉ: " +
        address
    );


    closeForm();
}


function closeForm() {

    document.getElementById("orderForm").style.display = "none";

    document.getElementById("background").style.display = "none";

}

</script>


</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)
                  
