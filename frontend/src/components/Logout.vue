<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
      <div class="text-center">
        <h1 class="text-3xl font-bold mb-4">Vous avez été déconnecté</h1>
        <router-link to="/login" class="btn btn-primary">Se connecter</router-link>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  onMounted(() => {
    // Supprimer le token des cookies
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  
    // Rediriger vers la page de connexion après un délai
    setTimeout(() => {
      router.push('/login');
    }, 3000);
  });
  </script>
  
  <style scoped>
  /* Ajoutez vos styles ici */
  </style>