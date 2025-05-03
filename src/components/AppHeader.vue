<script setup>
import { useAuthStore } from '@/stores/auth';
import { computed } from 'vue';

const authStore = useAuthStore();
const isAuthenticated = computed(() => authStore.isAuthenticated);
const userId = computed(() => authStore.userId);
</script>

<template>
  <header class="app-header">
    <nav class="navbar">
      <div class="container">
        <a class="navbar-brand" href="/">Jam-Date</a>
        <ul class="navbar-nav">
          <li class="nav-item" v-if="!isAuthenticated">
            <RouterLink class="nav-link" to="/register">Register</RouterLink>
          </li>
          <li class="nav-item" v-if="!isAuthenticated">
            <RouterLink class="nav-link" to="/login">Login</RouterLink>
          </li>
          <li class="nav-item" v-if="isAuthenticated">
            <RouterLink class="nav-link" :to="`/users/${userId}`">My Profile</RouterLink>
          </li>
          <li class="nav-item" v-if="isAuthenticated">
            <RouterLink class="nav-link" to="/profiles/new">Add Profile</RouterLink>
          </li>
          <li class="nav-item" v-if="isAuthenticated">
            <RouterLink class="nav-link" to="/profiles/favourites">Reports</RouterLink>
          </li>
          <li class="nav-item" v-if="isAuthenticated">
            <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { computed } from 'vue';
import { RouterLink } from 'vue-router';

const isAuthenticated = computed(() => !!localStorage.getItem('token'));
const userId = computed(() => localStorage.getItem('user_id') || '');
</script>

<style scoped>
.app-header {
  background-color: #ff6f61; 
  color: white;
  padding: 15px 0;
  text-align: center;
  font-size: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.navbar-brand {
  font-size: 24px;
  font-weight: bold;
  color: white;
  text-decoration: none;
}

.navbar-nav {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-item {
  margin-left: 15px;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #ffe0dc;
}
</style>
