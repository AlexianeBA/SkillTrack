<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div class="max-w-7xl mx-auto bg-white shadow-lg rounded-lg p-8">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold mb-8 text-center">Liste des employés</h1>
        <button class="btn btn-primary" @click="addEmployees">
          ➕ Ajouter des employés
        </button>
      </div>
      <div class="overflow-x-auto">
        <table class="table w-full">
          <thead>
            <tr>
              <th>Nom</th>
              <th>Prénom</th>
              <th>Email</th>
              <th>Poste</th>
              <th>Compétences</th>
              <th>Salaire</th>
              <th>Date d'embauche</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="employee in employees" :key="employee.id">
              <td>{{ employee.last_name }}</td>
              <td>{{ employee.first_name }}</td>
              <td>{{ employee.email }}</td>
              <td>{{ employee.position }}</td>
              <td>
                <ul>
                  <li v-for="skill in employee.skill_objects" :key="skill.id">{{ skill.name }}</li>
                </ul>
              </td>
              <td>{{ employee.salary }}</td>
              <td>{{ employee.hire_date }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      employees: []
    };
  },
  created() {
    this.fetchEmployees();
  },
  methods: {
    async fetchEmployees() {
      try {
        const response = await fetch('http://localhost:8000/api/employees/');
        const data = await response.json();
        this.employees = data;
      } catch (error) {
        console.error('Error fetching employees:', error);
      }
    },
    addEmployees() {
      // Rediriger vers la page d'ajout d'employé
      this.$router.push('/add-employees');
    }
  }
};
</script>

