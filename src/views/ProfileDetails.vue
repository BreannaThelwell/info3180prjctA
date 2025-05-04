<template>
  <div v-if="profile" class="profile-details">
    <h3>{{ profile.name }}</h3>
    <p><strong>Name:</strong> {{ profile.user_name }}</p>
    <p><strong>Description:</strong>{{ profile.description }}</p>
    <p><strong>Parish:</strong> {{ profile.parish }}</p>
    <p><strong>Bio:</strong> {{ profile.biography }}</p>
    <p><strong>Sex:</strong> {{ profile.sex }}</p>
    <p><strong>Race:</strong> {{ profile.race }}</p>
    <p><strong>Birth Year:</strong> {{ profile.birth_year }}</p>
    <p><strong>Height:</strong> {{ profile.height }} </p>
    <p><strong>Favourite Cuisine:</strong> {{ profile.fav_cuisine }}</p>
    <p><strong>Favourite Color:</strong> {{ profile.fav_colour }}</p>
    <p><strong>Favourite Subject:</strong> {{ profile.fav_school_subject }}</p>
    <p><strong>Political:</strong> {{ profile.political }}</p>
    <p><strong>Religious:</strong> {{ profile.religious }}</p>
    <p><strong>Family Oriented:</strong> {{ profile.family_oriented}}</p>

    <button v-if="isAuthenticated" @click="favouriteProfile">❤️ Favourite</button>
    <button v-else disabled>❤️ Favourite (Login required)</button>
    <button>Email Profile</button>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  data() {
    return { profile: null }
  },
  computed: {
    isAuthenticated() {
      return !!localStorage.getItem('token')
    }
  },
  async created() {
    const id = this.$route.params.profile_id
    const res = await axios.get(`/profiles/${id}`)
    this.profile = res.data
  },
  methods: {
    async favouriteProfile() {
      await axios.post(`/profiles/${this.profile.user_id}/favourite`)
      alert('Profile added to favourites')
    },
  },
}
</script>

<style scoped>
.profile-details {
  max-width: 800px;
  margin: 40px auto;
  padding: 30px;
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  font-family: 'Poppins', sans-serif;
  text-align: center;
}

.profile-details h3 {
  color: #ff6f61;
  font-size: 32px;
  font-weight: 600;
  margin-bottom: 20px;
}

.profile-details p {
  color: #555;
  font-size: 18px;
  margin-bottom: 30px;
}

.profile-details button {
  background-color: #ff6f61;
  color: white;
  padding: 12px 25px;
  border: none;
  border-radius: 30px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin: 0 10px;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.profile-details button:hover:not(:disabled) {
  background-color: #ff3b2f;
  transform: scale(1.05);
}

.profile-details button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.profile-details button {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.profile-details button:hover:not(:disabled) {
  background-color: #ff3b2f;
  transform: scale(1.05);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}
</style>
