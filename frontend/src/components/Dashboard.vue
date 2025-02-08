<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl font-bold mb-8">Tableau de bord</h1>
      <p>Bienvenue sur votre tableau de bord !</p>
      <button class="btn btn-success" @click="logout">Se déconnecter</button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const logout = () => {
  // Supprimer le token des cookies
  localStorage.removeItem('token');
  localStorage.removeItem('user');

  // Rediriger vers la page de déconnexion
  router.push('/logout');
};
</script>

<style scoped>
/* Ajoutez vos styles ici */
</style>