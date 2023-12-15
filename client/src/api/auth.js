const authAPI = (axiosInstance) => {
    const registerUser = async (userData) => {
        try {
            const response = await axiosInstance.post('users/', userData);
            return response.data;
        } catch (error) {
            throw new Error(error.response?.data?.message || 'Registration failed');
        }
    };

    return {
        registerUser,
    };
};

export default authAPI;
