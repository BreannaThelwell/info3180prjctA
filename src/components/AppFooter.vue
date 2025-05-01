<template>
  <footer class="app-footer">
    <div class="container">
      <p>&copy; {{ year }} Jam-Date. All Rights Reserved.</p>
    </div>
  </footer>
</template>

<script setup>
const year = new Date().getFullYear();
</script>

<style scoped>
.app-footer {
  background-color: #ff6f61; 
  color: white;
  text-align: center;
  padding: 15px 0;
  font-size: 14px;
  position: relative;
  width: 100%;
  margin-top: auto;
  box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1);
}

.app-footer p {
  margin: 0;
  font-size: 14px;
}
</style>