<template>
  <div>
    <!-- Navigation Menu -->
    <nav class="navbar">
      <router-link to="/">Home</router-link>
      <router-link v-if="!isLoggedIn" to="/login">Login</router-link>
      <router-link v-if="!isLoggedIn" to="/register">Register</router-link>
      <router-link v-if="isLoggedIn" to="/profiles/favourites">Reports</router-link>
      <router-link v-if="isLoggedIn" to="/logout">Logout</router-link>
    </nav>

    <h1>Welcome to JamDate!</h1>

    <!-- Search Bar -->
    <div class="search-bar">
      <input v-model="searchQuery" placeholder="Search by name, birth year, sex, or race..." />
      <button @click="searchProfiles">Search</button>
    </div>

    <!-- Profile List -->
    <div class="profile-list">
      <h2>Recent Profiles</h2>
      <div v-if="profiles.length === 0">No profiles found.</div>
      <div v-for="profile in profiles" :key="profile.id" class="profile-card">
        <p><strong>Name:</strong> {{ profile.name }}</p>
        <p><strong>Birth Year:</strong> {{ profile.birth_year }}</p>
        <p><strong>Sex:</strong> {{ profile.sex }}</p>
        <p><strong>Race:</strong> {{ profile.race }}</p>
        <router-link :to="`/profiles/${profile.id}`">View Details</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from '@/axios'

export default {
  data() {
    return {
      profiles: [],
      searchQuery: ''
    }
  },
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem('token')
    }
  },
  methods: {
    async fetchProfiles() {
      try {
        const token = localStorage.getItem('token');
        const res = await axios.get('/profiles', {
          headers: { Authorization: `Bearer ${token}` }
        })
        //display the last 4 profiles (most recent)
        this.profiles = res.data.slice(-4).reverse()
      } catch (err) {
        console.error('Error fetching profiles:', err)
      }
    },
    async searchProfiles() {
      try {
        const token = localStorage.getItem('token')
        const res = await axios.get(`/search?query=${this.searchQuery}`, {
          headers: { Authorization: `Bearer ${token}` }
        })
        this.profiles = res.data
      } catch (err) {
        console.error('Search failed:', err)
      }
    }
  },
  created() {
    this.fetchProfiles();
  }
}
</script>

<style scoped>
.navbar {
  display: flex;
  gap: 15px;
  background: #f5f5f5;
  padding: 10px;
}

.search-bar {
  margin: 20px 0;
}

.profile-list {
  display: grid;
  gap: 15px;
}

.profile-card {
  border: 1px solid #ccc;
  padding: 10px;
}
</style>

