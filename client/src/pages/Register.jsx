import { useState } from 'react'
import APIs from '../api'

export default function Register() {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
    })

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        APIs.authAPI.registerUser(formData)
            .then((response) => {
                console.log('Registration successful', response.data)
            })
            .catch((error) => {
                console.error('Error registering:', error)
            })
    }

    return (
        <div className="mt-32">
            <h2>Đăng ký</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="username"
                    placeholder="Tên đăng nhập"
                    onChange={handleChange}
                />
                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    onChange={handleChange}
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Mật khẩu"
                    onChange={handleChange}
                />
                <button type="submit">Đăng ký</button>
            </form>
        </div>
    )
}
