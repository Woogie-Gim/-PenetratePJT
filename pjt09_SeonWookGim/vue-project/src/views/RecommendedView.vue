<template>
  <div
    v-if="recommendedMovie"
    class="movie-container d-flex flex-column align-items-center justify-content-center"
  >
    <h1>날씨 기반 추천 영화</h1>
    <h5 class="weather-div">현재 날씨 : {{ weatherStatus }}</h5>
    <div class="card mb-3 movie-card">
      <div class="d-flex flex-column align-items-center">
        <RouterLink
          :to="{
            name: 'movie',
            params: { id: recommendedMovie.id },
          }"
        >
          <img
            :src="getImageUrl(recommendedMovie.poster_path)"
            class="img-fluid rounded-top movie-image"
            alt="..."
          />
        </RouterLink>
        <div class="card-body text-center">
          <h5 class="card-title">{{ recommendedMovie.title }}</h5>
          <button
            type="button"
            class="btn"
            @click="openModal"
            data-bs-toggle="modal"
            data-bs-target="#youtubeTrailerModal"
          >
            <img :src="youtubeLogo" alt="YouTube" class="youtube-logo" />
          </button>
          <YoutubeTrailerModal :movieTitle="recommendedMovie.title" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"
import youtubeLogo from "@/assets/YouTube_full-color_icon_(2017).svg.webp"
import YoutubeTrailerModal from "@/components/YoutubeTrailerModal.vue"

const key = import.meta.env.VITE_TMDB_API_KEY
const weatherApiKey = import.meta.env.VITE_WEATHER_API_KEY

const recommendedMovie = ref(null)
const weatherStatus = ref("")
const fetchWeather = () => {
  const url = `http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=${weatherApiKey}`
  axios
    .get(url)
    .then((response) => {
      console.log(response.data.weather[0].main)
      return response.data.weather[0].main
    })
    .catch((err) => {
      alert("날씨정보 요청 실패")
    })
}

const selectGenreByWeather = (weather) => {
  switch (weather) {
    case "Rain":
      weatherStatus.value = "비 내리는 중"
      return 27
    case "Snow":
      weatherStatus.value = "눈 내리는 중"
      return 10749
    case "Clear":
      weatherStatus.value = "쾌청한 날씨"
      return 12
    case "Clouds":
      weatherStatus.value = "흐림"
      return 35
    default:
      weatherStatus.value = "흐림"
      return 35
  }
}

const fetchMovie = () => {
  const weather = fetchWeather();
  const genre = selectGenreByWeather(weather);

  const url = `https://api.themoviedb.org/3/discover/movie?with_genres=${genre}&language=ko-KR&page=1`;
  const headers = {
    accept: "application/json",
    Authorization: `Bearer ${key}`,
  };
  axios
    .get(url, { headers })
    .then((response) => {
      const movies = response.data.results.slice(0, 10);
      recommendedMovie.value =
        movies[Math.floor(Math.random() * movies.length)];
    })
    .catch((error) => {
      console.error("TMDB 서버 요청간 에러 발생:", error);
    });
};

const getImageUrl = (path) => {
  return `https://image.tmdb.org/t/p/w500${path}`
};

onMounted(fetchMovie)
</script>

<style scoped>

</style>
