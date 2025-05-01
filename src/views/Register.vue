<template>
  <div class="register-page">

    <!-- Registration Form -->
    <div class="register-container">
      <form class="register-form" @submit.prevent="register">
        <h2>Register</h2>
        <div class="form-group">
          <input 
            id="username" 
            v-model="username" 
            placeholder="Username" 
            required 
            class="form-input"
          />
        </div>
        <div class="form-group">
          <input 
            id="name" 
            v-model="name" 
            placeholder="Full Name" 
            required 
            class="form-input"
          />
        </div>
        <div class="form-group">
          <input 
            id="email" 
            v-model="email" 
            type="email" 
            placeholder="Email" 
            required 
            class="form-input"
          />
        </div>
        <div class="form-group">
          <input 
            id="password" 
            v-model="password" 
            type="password" 
            placeholder="Password" 
            required 
            class="form-input"
          />
        </div>
        <div class="form-group">
        <label for="photo">Upload Photo:</label>
        <input 
        type="file" 
        id="photo" 
        @change="handleFileUpload"
        class="form-input"
        />
        </div>
        <button type="submit" class="register-btn">Register</button>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </form>
      <p class="login-link">
        Already have an account? <router-link to="/login">Login here</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import axios from '@/axios'

export default {
  data() {
    return {
    username: '',
    name: '',
    email: '',
    password: '',
    photoFile: null, 
    errorMessage: ''
    }
  },
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem('token')
    }
  },
  methods: {
     handleFileUpload(event) {
      this.photoFile = event.target.files[0];
    },
    async register() {
      try {
        const formData = new FormData();
        formData.append('username', this.username);
        formData.append('name', this.name);
        formData.append('email', this.email);
        formData.append('password', this.password);
        if (this.photoFile) {
          formData.append('photo', this.photoFile);
        }

        await axios.post('/register', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        this.$router.push('/login');
      } catch (err) {
        this.errorMessage = err.response?.data?.msg || 'Registration failed.';
      }
    },
    logout() {
      localStorage.removeItem('token')
      localStorage.removeItem('user_id')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #fefefe, #ffe0dc);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.register-container {
  background-color: #ffffff;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  width: 100%;
  max-width: 450px;
  text-align: center;
}

.register-form h2 {
  color: #ff6f61;
  margin-bottom: 30px;
  font-size: 28px;
  font-weight: 600;
  font-family: 'Poppins', sans-serif;
}

.form-input {
  width: 100%;
  padding: 15px;
  border: 2px solid #ff6f61;
  border-radius: 12px;
  font-size: 16px;
  margin-bottom: 20px;
  font-family: 'Poppins', sans-serif;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-input:focus {
  border-color: #ff3b2f;
  box-shadow: 0 0 8px rgba(255, 59, 47, 0.3);
  outline: none;
}

.register-btn {
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

.register-btn:hover {
  background-color: #ff3b2f;
  transform: scale(1.05);
}

.error {
  color: #ff3b2f;
  font-size: 14px;
  margin-top: 10px;
}

.login-link {
  margin-top: 20px;
  font-size: 16px;
  color: #333;
}

.login-link a {
  color: #ff6f61;
  text-decoration: none;
  font-weight: 600;
}

.login-link a:hover {
  color: #ff3b2f;
}

</style>