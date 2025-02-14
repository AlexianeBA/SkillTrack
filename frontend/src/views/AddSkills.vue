<template>
    <div>
        <Navbar />
        <div class="container mx-auto p-8">
      <div class="bg-white p-6 rounded-lg shadow-lg">
        <h1 class="text-3xl font-bold text-primary text-center mb-6">Ajouter une compétence</h1>
        <form @submit.prevent="addSkill">
          <div class="form-control mb-4">
            <label class="label">
              <span class="label-text">Nom de la compétence</span>
            </label>
            <input 
              type="text" 
              v-model="skillName" 
              placeholder="Entrez le nom de la compétence" 
              class="input input-bordered w-full" 
              required 
            />
          </div>
          <div class="form-control">
            <button type="submit" class="btn btn-primary w-full">Ajouter</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import Navbar from '@/components/NavbarConnected.vue';

const router = useRouter();
const skillName = ref('');

const addSkill = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/skills/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: skillName.value }),
    });

    if (!response.ok) {
      throw new Error('Erreur lors de l\'ajout de la compétence');
    }

    router.push('/list-skills');
  } catch (error) {
    console.error('Erreur lors de l\'ajout de la compétence:', error);
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
}

.form-control {
  margin-bottom: 1rem;
}

.input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
}

.input:focus {
  outline: none;
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.btn-primary {
  background-color: #1d4ed8;
  color: white;
  border: none;
  border-radius: 0.375rem;
  transition: background-color 0.3s ease-in-out;
}

.btn-primary:hover {
  background-color: #2563eb;
}
</style>