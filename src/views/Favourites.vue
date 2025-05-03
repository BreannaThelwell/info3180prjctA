<template>
  <div class="favourites-page">
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


<style scoped>
.favourites-page {
  max-width: 900px;
  margin: 40px auto;
  padding: 30px;
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  font-family: 'Poppins', sans-serif;
}

.favourites-page h2 {
  color: #ff6f61;
  font-size: 28px;
  font-weight: 600;
  margin-bottom: 30px;
  text-align: center;
}

.favourites-page ul {
  list-style: none;
  padding: 0;
}

.favourites-page li {
  padding: 15px 20px;
  border-bottom: 1px solid #ffe0dc;
  font-size: 16px;
  color: #333;
  transition: background-color 0.3s ease;
}

.favourites-page li:hover {
  background-color: #ffe0dc;
}

.favourites-page li:last-child {
  border-bottom: none;
}

.favourites-page li:hover {
  background-color: #ffe0dc;
  transform: translateX(10px);
  transition: transform 0.3s ease, background-color 0.3s ease;
}
</style>
