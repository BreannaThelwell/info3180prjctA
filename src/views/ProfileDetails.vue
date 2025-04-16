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
