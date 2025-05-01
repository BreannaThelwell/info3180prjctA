<template>
  <div class="home">
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

h1 {
  text-align: center;
  color: #006400; /* Green for Jamaican theme */
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
  border: 2px solid #ffd700; /* Yellow border for Jamaican theme */
  padding: 15px;
  background-color: white;
  border-radius: 5px;
}

.btn-primary {
  background-color: #000; /* Black for Jamaican theme */
  color: #ffd700; /* Yellow text */
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #006400; /* Green hover effect */
}

.btn-secondary {
  background-color: #ffd700; /* Yellow for Jamaican theme */
  color: #000; /* Black text */
  padding: 5px 10px;
  border-radius: 5px;
  text-decoration: none;
}

.btn-secondary:hover {
  background-color: #006400; /* Green hover effect */
  color: white;
}
</style>

