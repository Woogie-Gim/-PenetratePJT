<template>
  <div v-if="movie">
    <MovieDetailInfo :movie="movie" />
  </div>
</template>

<script setup>
import MovieDetailInfo from '@/components/MovieDetailInfo.vue';
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const key = import.meta.env.VITE_TMDB_API_KEY
const route = useRoute()
const id = route.params.id

const movie = ref({})

const fethchMovieDetail = (id) => {
  const url = `https://api.themoviedb.org/3/movie/${id}?language=ko-KR`
  const headers = {
    accept: 'application/json',
    Authorization: `Bearer ${key}`
  }

  axios
    .get(url, { headers })
    .then((response) => {
      movie.value = response.data
    })
    .catch((err) => {
      alert('서버 에러')
      console.log(err)
    })
}

onMounted(() => {
  fethchMovieDetail(id)
})

</script>

<style scoped>

</style>