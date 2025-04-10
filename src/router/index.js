//file used to set up vue router
import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue';
import Register from '../views/Register.vue';
import Login from '../views/Login.vue';
import ProfileDetails from '../views/ProfileDetails.vue';
import AddProfile from '../views/AddProfile.vue';
import Favourites from '../views/Favourites.vue';
import UserProfile from '../views/UserProfile.vue';

const router = createRouter({ 
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: '/', component: Home }, //home page with recent profiles + search
        { path: '/register', component: Register }, //registration form
        { path: '/login', component: Login }, //login form
        { path: '/profiles/new', component: AddProfile }, //add new profile form
        { path: '/profiles/:profile_id', component: ProfileDetails }, //view a specific profile
        { path: '/profiles/favourites', component: Favourites }, //reports page: favourites
        { path: '/users/:user_id', component: UserProfile }, //view logged-in user's profile(s)
        {path: '/logout',
            beforeEnter(to, from, next) {
                localStorage.removeItem('token'); //clear token
                localStorage.removeItem('user_id');  //clear user id
                next('/login'); //redirect to login
            }
        }   
    ]

})

export default router
