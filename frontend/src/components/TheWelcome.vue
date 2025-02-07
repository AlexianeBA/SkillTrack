<template>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
  <img alt="Vue logo" :src="logo" class="logo" />
  <button class="btn color-base-100">Default</button>
  <input type="text" placeholder="Type here" class="input" />
</template>

<script setup>
import { ref } from 'vue';
import logo from '@/assets/images/logo.png';


</script>