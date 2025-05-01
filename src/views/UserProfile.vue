<template>
  <div class="user-profile">
    <h2>My Profile</h2>
    <div v-for="p in profiles" :key="p.id" class="profile-card">
      <p><strong>Description:</strong> {{ p.description }}</p>
      <button @click="matchMe(p.id)" class="btn-primary">Match Me</button>
    </div>

    <div v-if="matches.length" class="matches-section">
      <h3>Your Matches</h3>
      <ul>
        <li v-for="m in matches" :key="m.id" class="match-item">
          {{ m.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  data() {
    return {
      profiles: [],
      matches: [],
    }
  },
  async created() {
    const user_id = localStorage.getItem('user_id')
    try {
      const res = await axios.get(`/users/${user_id}`)
      this.profiles = res.data.profiles
    } catch (err) {
      console.error('Error fetching profiles:', err)
    }
  },
  methods: {
    async matchMe(profile_id) {
      try {
        const res = await axios.get(`/profiles/matches/${profile_id}`)
        this.matches = res.data
      } catch (err) {
        console.error('Error fetching matches:', err)
      }
    },
  },
}
</script>

<style scoped>
.user-profile {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  color: #333;
  font-weight: bold;
  color: #006400; /* Subtle green for Jamaican theme */
}

.profile-card {
  background: #fff;
  border: 2px solid #ffd700; /* Yellow border for Jamaican theme */
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-card p {
  margin: 0 0 10px;
}

.btn-primary {
  background-color: #000; /* Black for Jamaican theme */
  color: #ffd700; /* Yellow text */
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
}

.btn-primary:hover {
  background-color: #006400; /* Green hover effect */
}

.matches-section {
  margin-top: 20px;
  padding: 15px;
  background: #fff;
  border: 2px solid #006400; /* Green border for Jamaican theme */
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.matches-section h3 {
  margin-bottom: 10px;
  color: #333;
  font-weight: bold;
}

.match-item {
  list-style: none;
  padding: 5px 0;
  border-bottom: 1px solid #ddd;
}

.match-item:last-child {
  border-bottom: none;
}
</style>
