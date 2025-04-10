<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    async login() {
      try {
        const res = await axios.post('/auth/login', {
          username: this.username,
          password: this.password,
        })
        localStorage.setItem('token', res.data.token) //store jwt
        localStorage.setItem('user_id', res.data.user.id) //store user id
        this.$router.push('/') //redirect to homepage
      } catch (err) {
        alert('Login failed.')
      }
    },
  },
}
</script>
 