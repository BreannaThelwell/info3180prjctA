<template>
  <div class="home">
    <!-- Main Content -->
    <section class="content">
      <h1>Welcome to JamDate!</h1>
      <p class="subtitle">Find your perfect match today.</p>

      <!-- Search Bar -->
      <div class="search-container">
        <input 
          v-model="searchQuery" 
          placeholder="Search by name, birth year, sex, or race..." 
          class="search-input"
          @keyup.enter="searchProfiles"
        />
        <button @click="searchProfiles" class="search-btn">Search</button>
      </div>

      <!-- Recent Profiles -->
      <div class="profiles-section">
        <h2>Recent Profiles</h2>
        <div v-if="profiles.length === 0" class="no-profiles">No profiles found.</div>
        <div class="profiles-grid">
          <div v-for="profile in profiles" :key="profile.id" class="profile-card">
            <div class="profile-content">
              <p><strong>Name:</strong> {{ profile.name }}</p>
              <p><strong>Birth Year:</strong> {{ profile.birth_year }}</p>
              <p><strong>Sex:</strong> {{ profile.sex }}</p>
              <p><strong>Race:</strong> {{ profile.race }}</p>
            </div>
            <router-link :to="`/profiles/${profile.id}`" class="view-details-btn">View Details</router-link>
          </div>
        </div>
      </div>
    </section>
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
        this.profiles = res.data.slice(-4).reverse() // Display last 4 profiles
      } catch (err) {
        console.error('Error fetching profiles:', err.response?.data || err.message)
        this.profiles = []
      }
    },
    async searchProfiles() {
      try {
        // Parse searchQuery into parameters
        const params = new URLSearchParams()
        const terms = this.searchQuery.split(',').map(t => t.trim())
        terms.forEach(term => {
          if (/^\d{4}$/.test(term)) params.set('birth_year', term)
          else if (['male', 'female', 'other'].includes(term.toLowerCase())) params.set('sex', term.toLowerCase())
          else if (term) params.append('name', term) // Assuming name can be partial
        })
        const res = await axios.get(`/search?${params.toString()}`)
        this.profiles = res.data
      } catch (err) {
        console.error('Search failed:', err.response?.data || err.message)
        this.profiles = []
      }
    },
    logout() {
      localStorage.removeItem('token')
      localStorage.removeItem('user_id')
      this.$router.push('/login')
    }
  },
  created() {
    this.fetchProfiles()
  }
}
</script>

<style scoped>
.home {
  max-width: auto;
  margin: 0 auto;
  padding: 40px 20px;
  background: linear-gradient(135deg, #fefefe, #ffe0dc);
  min-height: 100vh;
  font-family: 'Poppins', sans-serif;
}

.content {
  text-align: center;
}

h1 {
  color: #ff6f61;
  font-size: 48px;
  font-weight: 600;
  margin-bottom: 15px;
}

.subtitle {
  color: #666;
  font-size: 24px;
  margin-bottom: 40px;
}

.search-container {
  display: flex;
  justify-content: center;
  margin: 30px 0;
  gap: 15px;
}

.search-input {
  padding: 15px 20px;
  width: 100%;
  max-width: 600px;
  border: 2px solid #ff6f61;
  border-radius: 30px;
  font-size: 16px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.search-input:focus {
  border-color: #ff3b2f;
  box-shadow: 0 0 8px rgba(255, 59, 47, 0.3);
  outline: none;
}

.search-btn {
  background-color: #ff6f61;
  color: white;
  border: none;
  padding: 15px 40px;
  border-radius: 30px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.search-btn:hover {
  background-color: #ff3b2f;
  transform: scale(1.05);
}

.profiles-section {
  margin-top: 60px;
}

h2 {
  color: #333;
  font-size: 32px;
  font-weight: 600;
  margin-bottom: 30px;
}

.no-profiles {
  color: #999;
  font-size: 18px;
  font-style: italic;
}

.profiles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
}

.profile-card {
  background-color: #ffffff;
  border: 2px solid #ff6f61;
  border-radius: 20px;
  padding: 25px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.profile-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
}

.profile-content p {
  margin: 12px 0;
  color: #555;
  font-size: 16px;
}

.profile-content strong {
  color: #333;
}

.view-details-btn {
  display: inline-block;
  background-color: #ff6f61;
  color: white;
  padding: 12px 25px;
  border-radius: 30px;
  text-decoration: none;
  font-size: 16px;
  font-weight: 600;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.view-details-btn:hover {
  background-color: #ff3b2f;
  transform: scale(1.05);
}
</style>