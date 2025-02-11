<template>
  <div class="h-screen w-full flex flex-col bg-base-200">
    
    <div class="w-full h-full bg-white p-50">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-4xl font-extrabold text-primary">Tableau de bord</h1>
        <button class="btn btn-error btn-lg shadow-md transition-transform transform hover:scale-105" @click="logout">
          🚪 Se déconnecter
        </button>
      </div>
      <p class="text-center mb-6 text-gray-600">Bienvenue sur votre tableau de bord !</p>
      <div class="flex flex-col space-y-4 flex-grow">
        <button class="btn btn-primary btn-lg w-full shadow-md transition-transform transform hover:scale-105" @click="searchEmployees">
          🔍 Rechercher par compétences
        </button>
        <button class="btn btn-secondary btn-lg w-full shadow-md transition-transform transform hover:scale-105" @click="searchEmployeesByName">
          🔍 Rechercher par nom
        </button>
        
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const searchEmployees = () => {
  router.push('/search-by-skill');
};

const searchEmployeesByName = () => {
  router.push('/search-by-name');
};

const logout = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('user');
  router.push('/logout');
};
</script>

<style scoped>
button {
  transition: all 0.3s ease-in-out;
}
</style>
