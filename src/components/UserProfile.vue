 <template>
  <div>
    <h2>My Profile</h2>
    <div v-for="p in profiles" :key="p.id">
      <p>{{ p.description }}</p>
      <button @click="matchMe(p.id)">Match Me</button>
    </div>

    <div v-if="matches.length">
      <h3>Matches</h3>
      <ul>
        <li v-for="m in matches" :key="m.id">{{ m.name }}</li>
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
    const res = await axios.get(`/users/${user_id}`)
    this.profiles = res.data.profiles;
  },
  methods: {
    async matchMe(profile_id) {
      const res = await axios.get(`/profiles/matches/${profile_id}`)
      this.matches = res.data
    },
  },
}
</script>
