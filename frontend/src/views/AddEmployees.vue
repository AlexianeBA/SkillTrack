<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div class="max-w-7xl mx-auto bg-white shadow-lg rounded-lg p-8">
      <h1 class="text-3xl font-bold mb-8 text-center">Ajouter un employé</h1>
      <form @submit.prevent="addEmployee" enctype="multipart/form-data">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="first_name">
            Prénom
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="first_name" type="text" v-model="first_name" required>
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="last_name">
            Nom
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="last_name" type="text" v-model="last_name" required>
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
            Email
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="email" v-model="email" required>
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="position">
            Poste
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="position" type="text" v-model="position" required>
        </div>
        <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="skills">
                Compétences
            </label>
            <select 
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" 
                id="skills" 
                v-model="selectedSkill"
                required
            >
                <option v-for="skill in skills" :key="skill.id" :value="skill.id">
                {{ skill.name }}
                </option>
            </select>
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="salary">
            Salaire
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="salary" type="number" v-model="salary" required>
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="hire_date">
            Date d'embauche
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="hire_date" type="date" v-model="hire_date" required>
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="cv">
            CV
          </label>
          <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="cv" type="file" @change="handleFileUpload" required>
        </div>
        <div class="flex items-center justify-between">
          <button class="btn btn-primary" type="submit">
            Ajouter
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      first_name: '',
      last_name: '',
      email: '',
      position: '',
      selectedSkill: [],
      skills: '',
      salary: '',
      hire_date: '',
      cv: null
    };
  },
  mounted() {
    this.fetchSkills();
  },
  methods: {
    handleFileUpload(event) {
      this.cv = event.target.files[0];
    },
    async fetchSkills() {
      try {
        const response = await fetch('http://localhost:8000/api/skills/');
        if (!response.ok) {
          throw new Error(`Erreur HTTP: ${response.status}`);
        }
        this.skills = await response.json();
      } catch (error) {
        console.error('Erreur lors du chargement des compétences:', error);
      }
    },
    async addEmployee() {
      try {
        const formData = new FormData();
        formData.append('first_name', this.first_name);
        formData.append('last_name', this.last_name);
        formData.append('email', this.email);
        formData.append('position', this.position);
        formData.append('salary', this.salary);
        formData.append('hire_date', this.hire_date);
        formData.append('cv', this.cv);

        this.selectedSkills.forEach(skillId => {
          formData.append('skills', skillId);
        });


        console.log('FormData:', ...formData); // Log pour déboguer

        const response = await fetch('http://localhost:8000/api/employees/', {
          method: 'POST',
          body: formData
        });
        if (response.ok) {
          this.$router.push('/list-employees');
        } else {
          const errorData = await response.json();
          console.error('Error adding employee:', response.statusText, errorData);
        }
      } catch (error) {
        console.error('Error adding employee:', error);
      }
    }
  }
};
</script>

<style scoped>

</style>