<template>
  <div @click="handleClick">
    <img :src="thumbnail" alt="YouTube Video Thumbnail">
    <div>
      <h3 v-html="title"></h3>
      <div># {{ descriptions }}</div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(['thumbnail', 'title', 'descriptions'])

const emit = defineEmits()

const handleClick = () => {
  emit('click')
}


</script>

<style scoped>

</style>