<template>
    <div>
        <!--Form Title to create a new form-->
      <h2>Add a New Profile</h2>
      <form @submit.prevent="submitProfile">

        <!--Text inputs are here-->
        <input v-model="description" placeholder="Description" required>
        <input v-model="parish" placeholder="Parish" required>
        
        <!--Biography textarea-->
        <textarea v-model="biography" placeholder="Biography" required></textarea>
        
        <!--Sex Options-->
        <select v-model="sex" required>
          <option value="">Select Sex</option>
          <option>Male</option>
          <option>Female</option>
          <option>Other</option>
        </select>

        <!--Text and number inputs-->
        <input v-model="race" placeholder="Race" required>
        <input v-model.number="birthYear" type="number" placeholder="Birth Year" required>
        <input v-model.number="height" type="number" step="0.1" placeholder="Height (inches)" required>
        <input v-model="favCuisine" placeholder="Favorite Cuisine" required>
        <input v-model="favColour" placeholder="Favorite Colour" required>
        <input v-model="favSchoolSubject" placeholder="Favorite School Subject" required>
        
        <!--Checkboxes based on project are here-->
        <label>
          <input type="checkbox" v-model="political"> Political
        </label>
        <label>
          <input type="checkbox" v-model="religious"> Religious
        </label>
        <label>
          <input type="checkbox" v-model="familyOriented"> Family Oriented
        </label>

        <!--Submit form-->
        <button type="submit">Add a New Profile</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from '../axios'
  
  export default {
    data() {
        //Profile details
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
        //handles the form submission
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