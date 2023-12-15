import { Route, Routes } from 'react-router-dom'
import RootLayout from '@/components/layouts/RootLayout'
import { paths } from '@/routes/routes'
import { Suspense } from 'react'

const App = () => {
    return (
        <Routes>
            <Route element={<RootLayout />}>
                {paths.map((router, index) => {
                    const Page = router.component
                    return (
                        <Route
                            key={index}
                            path={router.path}
                            element={
                                <Suspense fallback={<div>Loading...</div>}>
                                    <Page />
                                </Suspense>
                            }
                        />
                    )
                })}
            </Route>
        </Routes>
    )
}

export default App
