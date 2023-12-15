import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'
import APIs from '@/api'

export default function Header() {
    const [categories, setCategories] = useState([])
    const [isDropdownOpen, setIsDropdownOpen] = useState(false)

    useEffect(() => {
        APIs.categories
            .getCategories()
            .then((response) => {
                setCategories(response.data.results)
            })
            .catch((error) => {
                console.error('Error fetching data:', error)
            })
    }, [])

    const toggleDropdown = () => {
        setIsDropdownOpen(!isDropdownOpen)
    }

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
                <ul className="flex space-x-8">
                    <li>
                        <Link className="hover:text-gray-300" to="/">
                            Trang Chủ
                        </Link>
                    </li>
                    <li
                        className="relative"
                        onMouseEnter={toggleDropdown}
                        onMouseLeave={toggleDropdown}
                    >
                        <Link className="hover:text-gray-300" to="/products">
                            Các Sản Phẩm
                        </Link>

                        {isDropdownOpen && (
                            <ul className="absolute top-full left-0 bg-white py-2 px-4 shadow-lg w-36">
                                {categories.map((category) => (
                                    <li className="py-1" key={category.id}>
                                        <Link
                                            to={'#'}
                                            className="text-gray-600"
                                        >
                                            {category.name}
                                        </Link>
                                    </li>
                                ))}
                            </ul>
                        )}
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
