<template>
  <div>
    <div>
      <img :src="getImageUrl(movie.poster_path)" alt="#">
    </div>
    <h1>{{ movie.title }}</h1>
    <div>
      <p>개봉일 : {{ movie.release_date }}</p>
      <p>러닝타임 : {{ movie.runtime }} 분</p>
      <p>TMDB 평점 : {{ movie.vote_average }}</p>
    </div>

    <h3>장르</h3>
    <div>
      <ul>
        <li v-for="genre in movie.genres" :key="genre.name">
          {{ genre.name }}
        </li>
      </ul>
    </div>

    <div>
      <h3>줄거리</h3>
      <p>{{ movie.overview }}</p>
    </div>

    <div>
      <h3>공식 예고편</h3>
      <button
        type="button"
        class="btn"
        @click="openModal"
        data-bs-toggle="modal"
        data-bs-target="#youtubeTrailerModal"
      >
        <img :src="youtubeLogo" alt="YouTube">
      </button>

      <YoutubeTrailerModal :movieTitle="movie.title" />
    </div>
  </div>
</template>

<script setup>
import youtubeLogo from '@/assets/YouTube_full-color_icon_(2017).svg.webp'
import YoutubeTrailerModal from "@/components/YoutubeTrailerModal.vue";
import { onMounted, ref } from 'vue'

const props = defineProps(["movie"])

const getImageUrl = (path) => {
  if (!path) {
    return '';
  }
  return `https://image.tmdb.org/t/p/w500${path}`;
}

onMounted(() => {
  getImageUrl()
})
</script>

<script scoped>

</script>