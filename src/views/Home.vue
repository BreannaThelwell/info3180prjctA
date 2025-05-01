<template>
  <div class="home">
    <nav class="navbar">
      <a href="/">Home</a>
      <a v-if="!isLoggedIn" href="/register">Register</a>
      <a v-if="!isLoggedIn" href="/login">Login</a>
      <a v-if="isLoggedIn" href="/profiles/favourites">Reports</a>
      <a v-if="isLoggedIn" href="/profiles/new">Add Profile</a>
      <a v-if="isLoggedIn" @click="logout">Logout</a>
    </nav>

    <h1>Welcome to Jam Date!</h1>

    <div class="search-bar">
      <input v-model="searchQuery" placeholder="Search by name, birth year, sex, or race..." />
      <button @click="searchProfiles" class="btn-primary">Search</button>
    </div>

    <div class="profile-list">
      <h2>Recent Profiles</h2>
      <div v-if="profiles.length === 0">No profiles found.</div>
      <div v-for="profile in profiles" :key="profile.id" class="profile-card">
        <p><strong>Name:</strong> {{ profile.name }}</p>
        <p><strong>Birth Year:</strong> {{ profile.birth_year }}</p>
        <p><strong>Sex:</strong> {{ profile.sex }}</p>
        <p><strong>Race:</strong> {{ profile.race }}</p>
        <router-link :to="`/profiles/${profile.id}`" class="btn-secondary">View Details</router-link>
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
        const res = await axios.get('/profiles')
        this.profiles = res.data.slice(-4).reverse()
      } catch (err) {
        console.error('Error fetching profiles:', err)
      }
    },
    async searchProfiles() {
      try {
        const res = await axios.get(`/search?query=${this.searchQuery}`)
        this.profiles = res.data
      } catch (err) {
        console.error('Search failed:', err)
      }
    },
    logout() {
      localStorage.removeItem('token')
      localStorage.removeItem('user_id')
      window.location.href = '/login'
    }
  },
  created() {
    this.fetchProfiles()
  }
}
</script>

<style scoped>
.home {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.navbar {
  display: flex;
  gap: 15px;
  background: #007bff;
  padding: 10px;
  color: white;
}

.navbar a {
  color: white;
  text-decoration: none;
}

.navbar a:hover {
  text-decoration: underline;
}

.search-bar {
  margin: 20px 0;
  display: flex;
  gap: 10px;
}

.profile-list {
  display: grid;
  gap: 15px;
}

.profile-card {
  border: 1px solid #ccc;
  padding: 15px;
  background-color: white;
  border-radius: 5px;
}

.btn-primary {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  text-decoration: none;
}

.btn-secondary:hover {
  background-color: #5a6268;
}
</style>

