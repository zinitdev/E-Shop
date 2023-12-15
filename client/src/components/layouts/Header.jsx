import { Link } from 'react-router-dom'

export default function Header() {
    return (
        <header className="bg-gray-800 text-white p-4 fixed top-0 w-full z-50">
            <nav className="flex justify-between items-center mx-auto max-w-5xl">
                <div className="logo">
                    <h1 className="text-3xl font-bold">
                        <Link to="/" className="text-white">
                            E-Shop
                        </Link>
                    </h1>
                </div>
                <ul className="flex space-x-4">
                    <li>
                        <Link className="hover:text-gray-300" to="/">
                            Trang Chủ
                        </Link>
                    </li>
                    <li>
                        <Link className="hover:text-gray-300" to="/products">
                            Các Sản Phẩm
                        </Link>
                    </li>
                    <li>
                        <Link className="hover:text-gray-300" to="/about">
                            Giới Thiệu
                        </Link>
                    </li>
                    <li>
                        <Link className="hover:text-gray-300" to="/contact">
                            Liên Hệ
                        </Link>
                    </li>
                    <li>
                        <Link className="hover:text-gray-300" to="/register">
                            Đăng Kí
                        </Link>
                    </li>
                </ul>
            </nav>
        </header>
    )
}
