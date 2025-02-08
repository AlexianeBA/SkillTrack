<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
      <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
        <h2 class="text-2xl font-bold text-center">Inscription</h2>
        <form @submit.prevent="register">
          <div class="form-control">
            <label class="label">
              <span class="label-text">Email</span>
            </label>
            <input 
              type="email" 
              v-model="email" 
              placeholder="Email" 
              class="input input-bordered" 
              required
            />
          </div>
          <div class="form-control">
            <label class="label">
              <span class="label-text">Mot de passe</span>
            </label>
            <input 
              type="password" 
              v-model="password" 
              placeholder="Mot de passe" 
              class="input input-bordered" 
              required 
            />
          </div>
          <div class="form-control">
            <label class="label">
              <span class="label-text">Prénom</span>
            </label>
            <input 
              type="text" 
              v-model="firstName" 
              placeholder="Prénom" 
              class="input input-bordered" 
              required 
            />
          </div>
          <div class="form-control">
            <label class="label">
              <span class="label-text">Nom</span>
            </label>
            <input 
              type="text" 
              v-model="lastName" 
              placeholder="Nom" 
              class="input input-bordered" 
              required 
            />
          </div>
          <div class="form-control">
            <label class="label">
              <span class="label-text">Rôle</span>
            </label>
            <select 
              v-model="role" 
              class="select select-bordered" 
              required 
            >
              <option value="" disabled selected>Choisissez un rôle</option>
              <option value="admin">Admin</option>
              <option value="user">User</option>
              <option value="rh">RH</option>
            </select>
          </div>
          <div v-if="error" class="text-red-500 text-sm mt-2">
            {{ error }}
          </div>
          <div class="form-control mt-6">
            <button 
              type="submit" 
              class="btn btn-primary"
              :disabled="loading"
            >
              {{ loading ? 'Inscription...' : "S'inscrire" }}
            </button>
          </div>
        </form>
      </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const email = ref('');
const password = ref('');
const firstName = ref('');
const lastName = ref('');
const role = ref('');
const error = ref('');
const loading = ref(false);

const register = async () => {
  loading.value = true;
  error.value = '';

  try {
    const response = await fetch('http://localhost:8000/api/users/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
        first_name: firstName.value,
        last_name: lastName.value,
        role: role.value,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || 'Erreur lors de la création du compte');
    }

    // Stockage du token JWT
    localStorage.setItem('token', data.token);
    
    // Si vous avez besoin des informations utilisateur
    if (data.user) {
      localStorage.setItem('user', JSON.stringify(data.user));
    }

    // Redirection vers le tableau de bord
    router.push('/dashboard');
    
  } catch (error) {
    console.error('Erreur de connexion:', error);
    error.value = error.message || 'Une erreur est survenue lors de la connexion';
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
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

.btn {
  width: 100%;
  padding: 0.5rem;
  transition: all 0.2s;
}

.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.label-text {
  font-size: 0.875rem;
  color: #4b5563;
  margin-bottom: 0.25rem;
}
</style>