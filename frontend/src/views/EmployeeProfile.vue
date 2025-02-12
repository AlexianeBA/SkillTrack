<template>
    <div class="min-h-screen bg-gray-100 p-8">
      <div class="max-w-7xl mx-auto bg-white shadow-lg rounded-lg p-8">
        <h1 class="text-3xl font-bold mb-8 text-center">Profil de l'employé</h1>
        <div v-if="employee">
          <p><strong>Nom :</strong> {{ employee.last_name }}</p>
          <p><strong>Prénom :</strong> {{ employee.first_name }}</p>
          <p><strong>Email :</strong> {{ employee.email }}</p>
          <p><strong>Poste :</strong> {{ employee.position }}</p>
          <p><strong>Compétences :</strong></p>
          <ul>
            <li v-for="skill in employee.skill_objects" :key="skill.id">{{ skill.name }}</li>
          </ul>
          <p><strong>Salaire :</strong> {{ employee.salary }}</p>
          <p><strong>Date d'embauche :</strong> {{ employee.hire_date }}</p>
          <p><strong>CV :</strong> <a :href="employee.cv" target="_blank">Télécharger</a></p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        employee: null
      };
    },
    created() {
      this.fetchEmployee();
    },
    methods: {
      async fetchEmployee() {
        const employeeId = this.$route.params.id;
        try {
          const response = await fetch(`http://localhost:8000/api/employees/${employeeId}/`);
          const data = await response.json();
          this.employee = data;
        } catch (error) {
          console.error('Error fetching employee:', error);
        }
      }
    }
  };
  </script>
  
