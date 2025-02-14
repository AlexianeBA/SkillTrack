<template>
    <div class="bg-gray-100">
      <Navbar />
      <div class="container mx-auto p-8">
        <div class="bg-white p-6 rounded-lg shadow-lg">
            <div class="flex justify-between items-center mb-6">
                <h1 class="text-3xl font-bold text-primary text-center mb-6">Liste des compétences</h1>
                <button class="btn btn-primary mb-4" @click="addSkills">Ajouter une compétence</button>
            </div>
          <div v-if="skills.length">

            <table class="table-auto w-full">
              <thead>
                <tr>
                  <th class="px-4 py-2">Nom de la compétence</th>
                  <th class="px-4 py-2">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="skill in skills" :key="skill.id">
                  <td class="border px-4 py-2">{{ skill.name }}</td>
                  <td class="border px-4 py-2">
                    <button class="btn btn-error btn-sm" @click="deleteSkill(skill.id)">Supprimer</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div v-else>
            <p class="text-center text-gray-500">Aucune compétence trouvée.</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import Navbar from '@/components/NavbarConnected.vue';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const skills = ref([]);
  
  const fetchSkills = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/skills/');
      const data = await response.json();
      skills.value = data;
    } catch (error) {
      console.error('Erreur lors de la récupération des compétences:', error);
    }
  };
  
  const deleteSkill = async (skillId) => {
    try {
      const response = await fetch(`http://localhost:8000/api/skills/${skillId}/`, {
        method: 'DELETE',
      });
      if (response.ok) {
        skills.value = skills.value.filter(skill => skill.id !== skillId);
      } else {
        console.error('Erreur lors de la suppression de la compétence:', response.statusText);
      }
    } catch (error) {
      console.error('Erreur lors de la suppression de la compétence:', error);
    }
  };

  const addSkills = () => {
  router.push('/add-skills');
};
  
  onMounted(fetchSkills);
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  
  .table-auto {
    width: 100%;
    border-collapse: collapse;
  }
  
  .table-auto th, .table-auto td {
    border: 1px solid #e2e8f0;
    padding: 0.75rem;
    text-align: left;
  }
  
  .table-auto th {
    background-color: #f9fafb;
    font-weight: bold;
  }
  
  .btn-error {
    background-color: #e3342f;
    color: white;
    border: none;
    border-radius: 0.375rem;
    padding: 0.5rem 1rem;
    transition: background-color 0.3s ease-in-out;
  }
  
  .btn-error:hover {
    background-color: #cc1f1a;
  }
  </style>