<template>
  <div class="add-profile-page">
    <h2>Add a New Profile</h2>
    <form @submit.prevent="submitProfile" class="add-profile-form">
      <input v-model="description" placeholder="Description" required>
      <input v-model="parish" placeholder="Parish" required>
      <textarea v-model="biography" placeholder="Biography" required></textarea>
      <select v-model="sex" required>
        <option value="">Select Sex</option>
        <option>Male</option>
        <option>Female</option>
        <option>Other</option>
      </select>
      <input v-model="race" placeholder="Race" required>
      <input v-model.number="birthYear" type="number" placeholder="Birth Year" required>
      <input v-model.number="height" type="number" step="0.1" placeholder="Height (inches)" required>
      <input v-model="favCuisine" placeholder="Favorite Cuisine" required>
      <input v-model="favColour" placeholder="Favorite Colour" required>
      <input v-model="favSchoolSubject" placeholder="Favorite School Subject" required>
      <label>
        <input type="checkbox" v-model="political"> Political
      </label>
      <label>
        <input type="checkbox" v-model="religious"> Religious
      </label>
      <label>
        <input type="checkbox" v-model="familyOriented"> Family Oriented
      </label>
      <button type="submit">Add a New Profile</button>
    </form>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  data() {
    return {
      description: '',
      parish: '',
      biography: '',
      sex: '',
      race: '',
      birthYear: null,
      height: null,
      favCuisine: '',
      favColour: '',
      favSchoolSubject: '',
      political: false,
      religious: false,
      familyOriented: false
    }
  },
  methods: {
    async submitProfile() {
      try {
        await axios.post('/profiles', {
          description: this.description,
          parish: this.parish,
          biography: this.biography,
          sex: this.sex,
          race: this.race,
          birth_year: this.birthYear,
          height: this.height,
          fav_cuisine: this.favCuisine,
          fav_colour: this.favColour,
          fav_school_subject: this.favSchoolSubject,
          political: this.political,
          religious: this.religious,
          family_oriented: this.familyOriented
        })
        this.$router.push('/')
      } catch (error) {
        alert('Error creating profile')
      }
    }
  }
}
</script>


<style scoped>
.add-profile-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #fefefe, #ffe0dc);
  padding: 20px;
}

.add-profile-form {
  background-color: #ffffff;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  width: 100%;
  max-width: 600px;
  text-align: center;
}

.add-profile-form h2 {
  color: #ff6f61;
  margin-bottom: 30px;
  font-size: 28px;
  font-weight: 600;
  font-family: 'Poppins', sans-serif;
}

.add-profile-form input,
.add-profile-form select,
.add-profile-form textarea {
  width: 100%;
  padding: 15px;
  border: 2px solid #ff6f61;
  border-radius: 12px;
  font-size: 16px;
  margin-bottom: 20px;
  font-family: 'Poppins', sans-serif;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.add-profile-form input:focus,
.add-profile-form select:focus,
.add-profile-form textarea:focus {
  border-color: #ff3b2f;
  box-shadow: 0 0 8px rgba(255, 59, 47, 0.5);
  outline: none;
}

.add-profile-form textarea {
  min-height: 120px;
  resize: vertical;
}

.add-profile-form label {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  font-size: 16px;
  color: #333;
  font-family: 'Poppins', sans-serif;
}

.add-profile-form button {
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

.add-profile-form button:hover {
  background-color: #ff3b2f;
  transform: scale(1.05);
}
</style>
