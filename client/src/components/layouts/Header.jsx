import { Link } from "react-router-dom";

export default function Header() {
    return (
        <header>
            <nav>
                <ul>
                    <li>
                        <Link to="/">Trang Chủ</Link>
                    </li>
                    <li>
                        <Link to="/products">Các Sản Phẩm</Link>
                    </li>
                    <li>
                        <Link to="/about">Giới Thiệu</Link>
                    </li>
                    <li>
                        <Link to="/contact">Liên Hệ</Link>
                    </li>
                    <li>
                        <Link to="/register">Đăng Kí</Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
}
