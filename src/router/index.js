import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue';
import Register from '../views/Register.vue';
import Login from '../views/Login.vue';
import ProfileDetails from '../views/ProfileDetails.vue';
import AddProfile from '../views/AddProfile.vue';
import Favourites from '../views/Favourites.vue';
import UserProfile from '../views/UserProfile.vue';

const routes = [
  { path: '/', component: Home }, // Public
  { path: '/register', component: Register, meta: { requiresGuest: true } },
  { path: '/login', component: Login, meta: { requiresGuest: true } },
  { path: '/profiles/new', component: AddProfile, meta: { requiresAuth: true } },
  { path: '/profiles/:profile_id', component: ProfileDetails }, // Public
  { path: '/profiles/favourites', component: Favourites, meta: { requiresAuth: true } },
  { path: '/users/:user_id', component: UserProfile, meta: { requiresAuth: true } },
  { path: '/logout', component: () => import('../views/Logout.vue') 
  }
]

const router = createRouter({ 
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token');
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login');
    } else {
      next();
    }
  } else if (to.matched.some(record => record.meta.requiresGuest)) {
    if (isAuthenticated) {
      next('/');
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router
