import { useState } from "react";
import axios from "axios";
import { mutate } from "swr";

export default function Register() {
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password: "",
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                "http://localhost:8000/users/",
                formData,
                { timeout: 3000 }
            );
            mutate("http://localhost:8000/users/");
            console.log("Registration successful:", response.data);
        } catch (error) {
            if (axios.isCancel(error)) {
                console.log("Request timeout");
            } else {
                console.error("Registration failed:", error);
            }
        }
    };

    return (
        <div>
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
    );
}
