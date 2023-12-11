import { lazy } from "react";

const paths = [
    { path: "/", component: lazy(() => import("@/pages/Home")) },
    { path: "/products", component: lazy(() => import("@/pages/Products")) },
    { path: "/about", component: lazy(() => import("@/pages/About")) },
    { path: "/contact", component: lazy(() => import("@/pages/Contact")) },
    { path: "/register", component: lazy(() => import("@/pages/Register")) },
];

export { paths };
