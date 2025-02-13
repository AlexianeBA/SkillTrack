<template>
  <div>
    <Navbar />
    <div class="flex justify-center mt-4 animate-fade-down">
      <img :src="logo" alt="SkillTrack Logo" class="w-60 h-auto" />
    </div>
    <div class="hero min-h-[40vh]">
      <div class="hero-content text-center">
        <div class="max-w-2xl">
          <h1 class="text-5xl font-bold text-primary animate-fade-up">
            Bienvenue sur <span class="text-accent">SkillTrack</span>
          </h1>
          <p class="py-6 text-lg text-gray-500 animate-fade-up">
            Gérez facilement vos compétences et celles de votre équipe. Rejoignez-nous dès maintenant pour un suivi optimal et efficace.
          </p>
          <div class="flex justify-center gap-4 animate-fade-up">
            <router-link to="/login">
              <button class="btn btn-primary btn-lg">🔓 Connexion</button>
            </router-link>
            <router-link to="/register">
              <button class="btn btn-outline btn-lg">📝 Inscription</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import logo from '@/assets/images/logo.png';
import Navbar from '@/components/Navbar.vue';

</script>

<style scoped>
@keyframes fade-down {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-down {
  animation: fade-down 0.8s ease-out;
}

.animate-fade-up {
  animation: fade-up 0.8s ease-out;
}
</style>