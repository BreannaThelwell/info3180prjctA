<template>
  <div class="login-wrapper">
    <div class="login-form">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="Username" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <button type="submit">Login</button>
      </form>
    </div>
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

    if (res && res.data) {
      localStorage.setItem('token', res.data.token)
      localStorage.setItem('user_id', res.data.user_id)
      localStorage.setItem('name', res.data.name)
      this.$router.push('/')
    } else {
      alert('Unexpected response from server.')
    }

  } catch (err) {
    console.error('Login error:', err)
    alert('Login failed. Please check your credentials and try again.')
     }
    },
  },
}
</script>

<style scoped>
.login-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #fefefe, #ffe0dc);
  padding: 20px;
}

.login-form {
  background-color: #ffffff;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 8px 16px rgba(0 Vacation, 0, 0, 0.15);
  width: 100%;
  max-width: 450px;
  text-align: center;
}

.login-form h2 {
  color: #ff6f61;
  margin-bottom: 30px;
  font-size: 28px;
  font-weight: 600;
  font-family: 'Poppins', sans-serif;
}

.login-form input {
  width: 100%;
  padding: 15px;
  border: 2px solid #ff6f61;
  border-radius: 12px;
  font-size: 16px;
  margin-bottom: 20px;
  font-family: 'Poppins', sans-serif;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.login-form input:focus {
  border-color: #ff3b2f;
  box-shadow: 0 0 8px rgba(255, 59, 47, 0.3);
  outline: none;
}

.login-form button {
  background-color: #ff6f61;
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 12px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  font-family: 'Poppins', sans-serif;
}

.login-form button:hover {
  background-color: #ff3b2f;
  transform: scale(1.05);
}
</style>
