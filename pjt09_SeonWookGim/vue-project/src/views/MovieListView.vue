<template>
  <div>
    <div class="container text-center">
      <div class="row">
          <MovieCard 
          v-for="(movie, index) in movies" 
          :key="index"
          :movie="movie" />
      </div>

    </div>
  </div>
</template>

<script setup>
import MovieCard from '@/components/MovieCard.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const key = import.meta.env.VITE_TMDB_API_KEY

const movies = ref([])

const fetchMovie = () => {
  const url = 'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=1'
  const headers = {
    Accept: 'application/json',
    Authorization: `Bearer ${key}`,
  }
  axios
    .get(url, { headers })
    .then((response) => {
      movies.value = response.data.results.slice(0, 10)
    })
    .catch((err) => {
      alert('Axios Error: ' + err.message)
    })
}

onMounted(fetchMovie)
</script>

<style scoped></style>