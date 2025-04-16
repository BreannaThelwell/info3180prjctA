 <template>
  <div>
    <h2>Top 20 Most Favourited Users</h2>
    <ul>
      <li v-for="u in topFavs" :key="u.user.id">
        {{ u.user.name }} - Favourited {{ u.fav_count }} times
      </li>
    </ul>

    <h2>My Favourites</h2>
    <ul>
      <li v-for="u in myFavs" :key="u.id">{{ u.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  data() {
    return {
      topFavs: [],
      myFavs: [],
    };
  },
  async created() {
    const user_id = localStorage.getItem('user_id')
    const top = await axios.get('/users/favourites/20')
    const mine = await axios.get(`/users/${user_id}/favourites`)
    this.topFavs = top.data
    this.myFavs = mine.data
  },
}
</script>
