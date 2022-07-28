<script setup>
import { RouterLink, RouterView } from "vue-router";
import "./components/Navbar.vue";
import Navbar from "./components/Navbar.vue";
import BlogPost from "./components/TodoPost.vue";
import Task from "./components/Task.vue";

</script>
<template>
  <Navbar/>
  <Task/>
  <BlogPost/>
</template>

<style scoped>

</style>
