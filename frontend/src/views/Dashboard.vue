<template>
  <div class="min-h-screen bg-base-200">
    <Navbar />
    <div class="container mx-auto px-6 py-10">
      <div class="text-center">
        <h1 class="text-5xl font-bold text-primary">📊 Tableau de Bord</h1>
        <p class="text-lg text-gray-600 mt-2">Bienvenue sur votre espace de gestion.</p>
      </div>

      <!-- Cartes d'actions -->
      <div class="grid gap-6 mt-10 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
        
        <div class="card bg-white shadow-xl hover:shadow-2xl transition-all transform hover:scale-105">
          <div class="card-body items-center text-center">
            <h2 class="card-title text-primary">🔍 Rechercher par compétences</h2>
            <p class="text-gray-500">Trouvez les employés en fonction de leurs compétences.</p>
            <button class="btn btn-primary w-full" @click="searchEmployees">Rechercher</button>
          </div>
        </div>

        <div class="card bg-white shadow-xl hover:shadow-2xl transition-all transform hover:scale-105">
          <div class="card-body items-center text-center">
            <h2 class="card-title text-secondary">🔎 Rechercher par nom</h2>
            <p class="text-gray-500">Trouvez un employé en saisissant son nom.</p>
            <button class="btn btn-secondary w-full" @click="searchEmployeesByName">Rechercher</button>
          </div>
        </div>

        <div class="card bg-white shadow-xl hover:shadow-2xl transition-all transform hover:scale-105">
          <div class="card-body items-center text-center">
            <h2 class="card-title text-accent">👥 Liste des employés</h2>
            <p class="text-gray-500">Affichez la liste complète des employés.</p>
            <button class="btn btn-accent w-full" @click="listEmployees">Afficher</button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import Navbar from '@/components/NavbarConnected.vue';

const router = useRouter();

const searchEmployees = () => {
  router.push('/search-by-skill');
};

const searchEmployeesByName = () => {
  router.push('/search-by-name');
};

const listEmployees = () => {
  router.push('/list-employees');
};
</script>
