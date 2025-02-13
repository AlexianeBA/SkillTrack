<template>
  <div >
    <!-- Navbar -->
    <Navbar />

    <div class="container mx-auto px-6 py-10">
      <div class="bg-white p-6 rounded-lg shadow-lg">
        <h1 class="text-3xl font-bold text-primary text-center mb-6">🔎 Rechercher un employé</h1>

        <!-- Champ de recherche -->
        <div class="mb-4">
          <input 
            type="text"
            v-model="searchName"
            placeholder="Entrez un nom"
            class="input input-bordered input-lg w-full"
          />
        </div>

        <!-- Bouton de recherche -->
        <button 
          @click="searchEmployeesByName" 
          class="btn btn-primary w-full text-lg font-semibold transition-transform hover:scale-105"
        >
          🔍 Rechercher
        </button>

        <!-- Résultats -->
        <div v-if="employees.length" class="mt-6">
          <h2 class="text-xl font-semibold text-gray-700 mb-4">📋 Résultats :</h2>
          
          <div class="space-y-3">
            <div 
              v-for="employee in employees" 
              :key="employee.id" 
              class="card bg-base-100 shadow-md p-4 rounded-lg"
            >
              <p class="text-lg font-medium">
                {{ employee.first_name }} {{ employee.last_name }} - 
                <span class="text-primary">{{ employee.position }}</span>
              </p>
            </div>
          </div>
        </div>

        <!-- Message si aucun résultat -->
        <div v-else-if="searchName && employees.length === 0" class="text-center mt-4 text-gray-500">
          Aucun employé trouvé ❌
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import Navbar from '@/components/NavbarConnected.vue';
  export default {
    components: {
    Navbar
  },
    data() {
      return {
        searchName: '',
        employees: []
      };
    },
    methods: {
      async searchEmployeesByName() {
        try {
          const params = new URLSearchParams();
          params.append('name', this.searchName);
          console.log('Searching for name:', this.searchName);
          const response = await fetch(`http://localhost:8000/api/search-by-name/?${params.toString()}`);
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const data = await response.json();
          console.log('Employees found:', data);
          this.employees = data;
        } catch (error) {
          console.error('Error searching employees by name:', error);
        }
      }
    }
  };
  </script>
  
  <style >

  
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
  </style>