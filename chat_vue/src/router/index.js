import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/home')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/login')
  },
  {
    path: '/chat/:room_name/:chat_type',
    name: 'chat',
    component: () => import('@/views/chat')
  },
  {
    path: '/my_chats/:id',
    name: 'my_chats',
    component: () => import('@/views/my_chats')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
