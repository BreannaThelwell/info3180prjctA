<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <AppHeader />

  <main>
    <RouterView />
  </main>
  
  <AppFooter />
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

body {
  padding-top: 80px;
  margin: 0;
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(135deg, #fefefe, #ffe0dc);
  color: #333;
}

.app-main {
  min-height: calc(100vh - 160px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

</style>