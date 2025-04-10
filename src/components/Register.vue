<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Username" required />
      <input v-model="name" placeholder="Full Name" required />
      <input v-model="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  data() {
    return {
      username: '',
      name: '',
      email: '',
      password: '',
    }
  },
  methods: {
    async register() {
      try {
        await axios.post('/register', {
          username: this.username,
          name: this.name,
          email: this.email,
          password: this.password,
        });
        this.$router.push('/login') //redirect to login after registration
      } catch (err) {
        alert('Registration failed.')
      }
    },
  },
}
</script>
 