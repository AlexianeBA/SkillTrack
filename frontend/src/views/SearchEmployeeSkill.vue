<template>
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Rechercher un employé à partir de ses compétences</h1>
      <div class="mb-4">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="Enter skills"
          class="input form-control"
        />
      </div>
      <button @click="searchEmployees" class="btn btn-primary">Rechercher</button>
      <div v-if="employees.length" class="mt-4">
        <h2 class="text-xl font-semibold">Résultats:</h2>
        <ul>
          <li v-for="employee in employees" :key="employee.id" class="mt-2">
            {{ employee.first_name }} {{ employee.last_name }} - {{ employee.position }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: '',
        employees: []
      };
    },
    methods: {
      async searchEmployees() {
        try {
          const params = new URLSearchParams();
          params.append('skills', this.searchQuery);
          console.log('Searching for skills:', this.searchQuery);
          const response = await fetch(`http://localhost:8000/api/search/?${params.toString()}`);
          const data = await response.json();
          console.log('Employees found:', data);
          this.employees = data;
        } catch (error) {
          console.error('Error searching employees:', error);
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