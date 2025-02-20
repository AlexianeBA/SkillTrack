import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginForm from '../views/LoginForm.vue'
import Dashboard from '@/views/Dashboard.vue'
import Register from '@/views/Register.vue'
import Logout from '@/views/Logout.vue'
import EmployeeSkillSearch from '@/views/SearchEmployeeSkill.vue'
import SearchEmployeeByName from '@/views/SearchEmployeeByName.vue'
import ListEmployees from '@/views/ListEmployees.vue'
import AddEmployees from '@/views/AddEmployees.vue'
import EmployeeProfile from '@/views/EmployeeProfile.vue';
import AddSkills from '@/views/AddSkills.vue'
import ListOfSkills from '@/views/ListOfSkills.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: LoginForm
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      meta: { requiresAuth: true }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      
    },
    {
      path: '/search-by-skill',
      name: 'EmployeeSkillSearch',
      component: EmployeeSkillSearch,
      
    },
    {
      path: '/add-skills',
      name: 'AddSkills',
      component: AddSkills,
      
    },
    {
      path: '/list-skills',
      name: 'ListOfSkills',
      component: ListOfSkills,
      
    },
    {
      path: '/search-by-name',
      name: 'SearchEmployeeByName',
      component: SearchEmployeeByName,
      
    },
    {
      path: '/list-employees',
      name: 'ListEmployees',
      component: ListEmployees,
      
    },
    {
      path: '/add-employees',
      name: 'AddEmployees',
      component: AddEmployees,
      
    },
    {
      path: '/logout',
      name: 'logout',
      component: Logout
    },
    {
      path: '/employee/:id',
      name: 'EmployeeProfile',
      component: EmployeeProfile,
    },
  ],
})
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  
  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else {
    next()
  }
})

export default router

