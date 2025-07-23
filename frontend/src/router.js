import { createRouter , createWebHistory} from 'vue-router'
import home from './components/home.vue'
import Dashboard from './components/Dashboard.vue'
import Analytics from './components/Analytics.vue'

const routes = [
    {
        path: '/',
        name: "Home",
        component:home
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component : Dashboard
    },
    {
        path: '/analytics',
        name: "Analytics",
        component : Analytics
    }


]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;
