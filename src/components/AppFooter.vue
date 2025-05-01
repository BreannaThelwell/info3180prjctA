<template>
  <footer class="app-footer">
    <div class="container">
      <p>&copy; {{ year }} Jam Date. All Rights Reserved.</p>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear()
</script>

<style scoped>
.app-footer {
  background-color: #000000; /* Black for Jamaican theme */
  color: #e6f7b0; /* Yellow text */
  text-align: center;
  padding: 10px 0;
  margin-top: 20px;
  font-size: 14px;
}
</style>