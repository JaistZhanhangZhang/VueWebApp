import {createRouter, createWebHistory} from 'vue-router';

const routes = [
    {path:'/',
    component:()=>import('../components/ImageShow.vue')},
    {path:'/SignIn',
    component:()=>import('../components/SignIn.vue')},
    {path:'/SignUp',
    component:()=>import('../components/SignUp.vue')},
    {path:"/ImageSubmit",
    component:()=>import('../components/ImageSubmit.vue')},
]

const router = createRouter({
    history: createWebHistory(),
    routes : routes})

export default router;