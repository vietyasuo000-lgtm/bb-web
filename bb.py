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

    <title>Shop Của Long</title>

    <style>
        * {
            box-sizing: border-box;
            font-family: Arial;
        }

        body {
            margin: 0;
            background: #f5f5f5;
        }

        header {
            background: #111;
            color: white;
            padding: 20px;
            text-align: center;
        }

        .hero {
            background: linear-gradient(135deg, #111, #ff3366);
            color: white;
            text-align: center;
            padding: 60px 20px;
        }

        .hero h1 {
            font-size: 45px;
        }

        .products {
            width: 90%;
            max-width: 1100px;
            margin: 40px auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }

        .product {
            background: white;
            padding: 25px;
            text-align: center;
            border-radius: 15px;
            box-shadow: 0 5px 15px #ddd;
        }

        .icon {
            font-size: 60px;
        }

        .price {
            color: #ff3366;
            font-size: 20px;
            font-weight: bold;
            margin: 15px;
        }

        button {
            background: #111;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            cursor: pointer;
        }

        button:hover {
            background: #ff3366;
        }

        #orderForm {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 30px;
            width: 90%;
            max-width: 400px;
            border-radius: 15px;
            box-shadow: 0 0 30px #555;
            z-index: 10;
        }

        #orderForm input {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 8px;
        }

        #background {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.5);
            z-index: 5;
        }

        footer {
            background: #111;
            color: white;
            text-align: center;
            padding: 30px;
        }

        @media (max-width: 800px) {
            .products {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

<header>
    <h2>🛒 SHOP CỦA LONG</h2>
</header>

<section class="hero">
    <h1>SHOP CỦA LONG</h1>
    <p>Thời trang đẹp - Giá tốt - Uy tín</p>
</section>


<div class="products">

    <div class="product">
        <div class="icon">👖</div>
        <h3>Jean Short(CỦA LONG)</h3>
        <div class="price">300.000đ</div>

        <button onclick="buy('Jean Short', '300.000đ')">
            🛒 Mua ngay
        </button>
    </div>


    <div class="product">
        <div class="icon">👕</div>
        <h3>Áo thun(CỦA LONG)</h3>
        <div class="price">200.000đ</div>

        <button onclick="buy('Áo thun', '200.000đ')">
            🛒 Mua ngay
        </button>
    </div>


    <div class="product">
        <div class="icon">💻</div>
        <h3>Laptop(CỦA LONG)</h3>
        <div class="price">15.000.000đ</div>

        <button onclick="buy('Laptop của Long', '15.000.000đ')">
            🛒 Mua ngay
        </button>
    </div>


    <div class="product">
        <div class="icon">📱</div>
        <h3>Điện thoại(CỦA LONG)</h3>
        <div class="price">8.000.000đ</div>

        <button onclick="buy('Điện thoại của Long', '8.000.000đ')">
            🛒 Mua ngay
        </button>
    </div>


    <div class="product">
        <div class="icon">🎒</div>
        <h3>Balo(CỦA LONG)</h3>
        <div class="price">300.000đ</div>

        <button onclick="buy('Balo của Long', '300.000đ')">
            🛒 Mua ngay
        </button>
    </div>


    <div class="product">
        <div class="icon">🎧</div>
        <h3>Tai nghe(CỦA LONG)</h3>
        <div class="price">700.000đ</div>

        <button onclick="buy('Tai nghe của Long', '700.000đ')">
            🛒 Mua ngay
        </button>
    </div>


    <div class="product">
        <div class="icon">👟</div>
        <h3>Giày Sneaker(CỦA LONG)</h3>
        <div class="price">500.000đ</div>

        <button onclick="buy('Giày Sneaker', '500.000đ')">
            🛒 Mua ngay
        </button>
    </div>

</div>


<!-- NỀN TỐI -->

<div id="background"></div>


<!-- FORM -->

<div id="orderForm">

    <h2>🛒 Đặt hàng</h2>

    <p id="product"></p>
    <p id="price"></p>

    <input
        type="text"
        id="name"
        placeholder="Họ và tên"
    >

    <input
        type="text"
        id="phone"
        placeholder="Số điện thoại"
    >

    <input
        type="text"
        id="address"
        placeholder="Địa chỉ"
    >

    <button onclick="confirmOrder()">
        ✅ Xác nhận
    </button>

    <button onclick="closeForm()">
        ❌ Hủy
    </button>

</div>


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

    let name = document.getElementById("name").value;
    let phone = document.getElementById("phone").value;
    let address = document.getElementById("address").value;

    if (name == "" || phone == "" || address == "") {

        alert("⚠️ Vui lòng nhập đầy đủ thông tin!");

        return;
    }

    alert(
        "🎉 ĐẶT HÀNG THÀNH CÔNG!\\n\\n" +
        "Sản phẩm: " + currentProduct + "\\n" +
        "Giá: " + currentPrice + "\\n" +
        "Họ tên: " + name + "\\n" +
        "SĐT: " + phone + "\\n" +
        "Địa chỉ: " + address
    );

    closeForm();
}


function closeForm() {

    document.getElementById("orderForm").style.display = "none";

    document.getElementById("background").style.display = "none";
}

</script>


<footer>
    🛒 SHOP CỦA LONG
    <br><br>
    © 2026 Shop Của Long
    <br>
    Liên hệ: 0982618795
</footer>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)
          
