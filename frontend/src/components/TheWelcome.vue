<template>
  <div>
    <h1 class="text-3xl font-bold underline">
      Hello world!
    </h1>
    <img alt="Vue logo" :src="logo" class="logo" />
    <LoginForm />
  </div>
  <router-link to="/login">
      <button class="btn btn-success">Connexion</button>
  </router-link>
  <router-link to="/register">
      <button class="btn btn-success">Inscription</button>
  </router-link>
</template>

<script setup>
import { ref } from 'vue';
import logo from '@/assets/images/logo.png';

</script>