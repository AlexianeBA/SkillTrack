<template>
  <div>
    <h1 class="text-3xl font-bold underline">
      Hello world!
    </h1>
    <img alt="Vue logo" :src="logo" class="logo" />
    <LoginForm />
  </div>
  <router-link to="/login">
      <button class="btn btn-primary">Connexion</button>
  </router-link>
</template>

<script setup>
import { ref } from 'vue';
import logo from '@/assets/images/logo.png';

</script>