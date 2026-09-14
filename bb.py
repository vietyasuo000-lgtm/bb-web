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
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f5f5f5;
            color: #222;
        }

        header {
            background: #111;
            color: white;
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 25px;
            font-weight: bold;
        }

        .logo span {
            color: #ff3366;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 20px;
        }

        .hero {
            background: linear-gradient(135deg, #111, #ff3366);
            color: white;
            text-align: center;
            padding: 90px 20px;
        }

        .hero h1 {
            font-size: 50px;
            margin-bottom: 15px;
        }

        .hero p {
            font-size: 20px;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: 50px auto;
        }

        .title {
            text-align: center;
            margin-bottom: 30px;
        }

        .title h2 {
            font-size: 32px;
            margin-bottom: 10px;
        }

        .products {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .product {
            background: white;
            padding: 30px;
            text-align: center;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,.1);
            transition: .3s;
        }

        .product:hover {
            transform: translateY(-8px);
        }

        .icon {
            font-size: 70px;
            margin-bottom: 20px;
        }

        .product h3 {
            font-size: 23px;
            margin-bottom: 10px;
        }

        .price {
            color: #ff3366;
            font-size: 21px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        button {
            background: #111;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background: #ff3366;
        }

        footer {
            background: #111;
            color: white;
            text-align: center;
            padding: 30px;
            margin-top: 60px;
        }

        @media (max-width: 800px) {
            .products {
                grid-template-columns: 1fr;
            }

            .hero h1 {
                font-size: 35px;
            }

            nav {
                display: none;
            }
        }
    </style>
</head>

<body>

<header>
    <div class="logo">
        🛒 SHOP <span>CỦA LONG</span>
    </div>

    <nav>
        <a href="/">Trang chủ</a>
        <a href="#products">Sản phẩm</a>
    </nav>
</header>


<section class="hero">

    <h1>SHOP CỦA LONG</h1>

    <p>
        Thời trang đẹp - Giá tốt - Uy tín
    </p>

</section>


<section class="container" id="products">

    <div class="title">

        <h2>🔥 Sản phẩm nổi bật</h2>

        <p>
            Chọn sản phẩm bạn yêu thích
        </p>

    </div>


    <div class="products">


        <div class="product">

            <div class="icon">
                👖
            </div>

            <h3>
                Jean Short(CỦA LONG)
            </h3>

            <div class="price">
                300.000đ
            </div>

            <button onclick="buy('Jean Short')">
                🛒 Mua ngay
            </button>

        </div>


        <div class="product">

            <div class="icon">
                👕
            </div>

            <h3>
                Áo thun(CỦA LONG)
            </h3>

            <div class="price">
                200.000đ
            </div>

            <button onclick="buy('Áo thun')">
                🛒 Mua ngay
            </button>

        </div>


        <div class="product">

            <div class="icon">
                👟
            </div>

            <h3>
                Giày Sneaker(CỦA LONG)
            </h3>

            <div class="price">
                500.000đ
            </div>

            <button onclick="buy('Giày Sneaker')">
                🛒 Mua ngay
            </button>

        </div>


    </div>

</section>


<footer>

    <h3>
        🛒 SHOP CỦA LONG
    </h3>

    <br>

    <p>
        © 2026 Shop Của Long<br>
        Lien He Voi Chung Toi:0982618795
    </p>

</footer>


<script>

function buy(product) {

    alert(
        "🎉 Bạn đã chọn: " +
        product +
        "\\n\\nCảm ơn bạn đã mua hàng!"
    );

}

</script>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
