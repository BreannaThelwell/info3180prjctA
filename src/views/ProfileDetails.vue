 <template>
  <div v-if="profile">
    <h3>{{ profile.name }}</h3>
    <p>{{ profile.description }}</p>
    <!-- Heart icon (clickable) -->
    <button @click="favouriteProfile">❤️ Favourite</button>
    <button>Email Profile</button>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  data() {
    return { profile: null }
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

.profile-details button:hover {
  background-color: #ff3b2f;
  transform: scale(1.05);
}

.profile-details button.favourited {
  background-color: #ff3b2f;
}
</style>