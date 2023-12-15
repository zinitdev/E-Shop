const categoriesAPI = (axiosInstance) => {
    const getCategories = () => {
        return axiosInstance.get('/categories')
    }

    const getCategoryById = (categoryId) => {
        return axiosInstance.get(`/categories/${categoryId}`)
    }

    return {
        getCategories,
        getCategoryById,
    }
}

export default categoriesAPI
