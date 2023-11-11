<template>
  <div>
    <div>
      <input 
        type="text"
        v-model="searchQuery"
        placeholder="영화 제목을 검색해보세요"
        class="search-input"
        v-on:keyup.enter="searchReviews"
      >
      <button @click="searchReviews" class="search-button">검색</button>
    </div>
  </div>

  <div>
    <div v-for="(video, index) in videos" :key="index">
      <YoutubeCard 
        :thumbnail="video.snippet.thumbnails.default.url"
        :title="video.snippet.title"
        :descriptions="video.snippet.description"
        @click="openModal(index)"
        data-bs-toggle="modal"
        data-bs-target="#youtubeTrailerModal"
      />
      <YoutubeReviewModal
        :videoTitle="videoTitle"
        :currentVideoId="currentVideoId"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import axios from "axios"
import YoutubeReviewModal from "@/components/YoutubeReviewModal.vue"
import YoutubeCard from "@/components/YoutubeCard.vue"

const searchQuery = ref("")
const videos = ref([])
const currentVideoId = ref("")
const youtubeKey = import.meta.env.VITE_YOUTUBE_API_KEY
const videoTitle = ref("")

const searchReviews = () => {
  axios
    .get("https://www.googleapis.com/youtube/v3/search", {
      params: {
        part: "snippet",
        q: `영화 ${searchQuery.value} 리뷰`,
        key: youtubeKey,
        type: "video",
        maxResults: 10,
      },
    })
    .then((response) => {
      videos.value = response.data.items
    })
    .catch((error) => {
      alert("API 호출 중 에러 발생: " + error)
    })
}

const openModal = (index) => {
  const videoId = videos.value[index].id.videoId
  currentVideoId.value = videoId
  videoTitle.value = videos.value[index].snippet.title
}
</script>

<style scoped>

</style>