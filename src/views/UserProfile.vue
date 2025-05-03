<template>
  <div class="user-profile">
    <h2>My Profile</h2>
    <div v-for="p in profiles" :key="p.id" class="profile-card">
      <p><strong>Description:</strong> {{ p.description }}</p>
      <button @click="matchMe(p.id)" class="btn-primary">Match Me</button>
    </div>
    <div v-if="matches.length" class="matches-section">
      <h3>Matches</h3>
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
  max-width: 900px;
  margin: 40px auto;
  padding: 30px;
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  font-family: 'Poppins', sans-serif;
}

h2 {
  text-align: center;
  color: #ff6f61;
  font-size: 28px;
  font-weight: 600;
  margin-bottom: 30px;
}

.profile-card {
  background: #ffffff;
  border: 2px solid #ff6f61;
  border-radius: 20px;
  padding: 25px;
  margin-bottom: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.profile-card:hover {
  transform: translateY(-5px);
}

.profile-card p {
  margin: 12px 0;
  color: #555;
  font-size: 16px;
}

.btn-primary {
  background-color: #ff6f61;
  color: white;
  border: none;
  padding: 12px 25px;
  border-radius: 30px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn-primary:hover {
  background-color: #ff3b2f;
  transform: scale(1.05);
}

.matches-section {
  margin-top: 40px;
  padding: 25px;
  background: #ffffff;
  border: 2px solid #ff6f61;
  border-radius: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.matches-section h3 {
  color: #ff6f61;
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 20px;
}

.match-item {
  list-style: none;
  padding: 15px 0;
  border-bottom: 1px solid #ffe0dc;
  font-size: 16px;
  color: #333;
}

.match-item:last-child {
  border-bottom: none;
}
</style>
