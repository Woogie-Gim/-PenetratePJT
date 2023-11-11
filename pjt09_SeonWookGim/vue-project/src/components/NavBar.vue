<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark" data-bs-theme="dark">
      <RouterLink :to="{ name: 'home' }">
        <img :src="logo" alt="Logo" height="50" width="50">
      </RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav align-items-end">
          <li class="nav-item">
            <RouterLink :to="{ name: 'movies' }" class="router-link" active-class="active-tab">영화조회</RouterLink>
          </li>
          <p></p>
          <li class="nav-item">
            <RouterLink :to="{ name: 'review' }" class="router-link" active-class="active-tab">리뷰검색</RouterLink>
          </li>
          <p></p>
          <li class="nav-item">
            <RouterLink :to="{ name: 'recommended' }" class="router-link" active-class="active-tab">영화추천</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import logoSrc from '@/assets/popcorn.png'

const logo = ref(logoSrc)
</script>

<style scoped>

.router-link {
  text-decoration: none;
  color: white;
  margin-right: 15px; 
}

.active-tab {
  color: rgb(174, 219, 250) !important;
  font-weight: bold !important;
}

</style>
