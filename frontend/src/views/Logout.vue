<template>
  <div>
    <Navbar />
  
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
      <div class="text-center">
        <h1 class="text-3xl font-bold mb-4">Vous avez été déconnecté</h1>
        <p>Vous allez être redirigé vers la page d'accueil dans quelques secondes...</p>
      </div>
    </div>
  </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import Navbar from '@/components/Navbar.vue';
  
  const router = useRouter();
  
  onMounted(() => {
    // Supprimer le token des cookies
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  
    // Rediriger vers la page d'accueil' après un délai
    setTimeout(() => {
      router.push('/');
    }, 3000);
  });
  </script>
  
  <style scoped>
  /* Ajoutez vos styles ici */
  </style>