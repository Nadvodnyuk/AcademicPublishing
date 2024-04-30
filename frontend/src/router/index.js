import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue';
import RegisterView from '@/views/RegisterView.vue';
import LoginView from '@/views/LoginView.vue';
import DashboardView from '@/views/DashboardView.vue';
import ProfileView from '@/views/ProfileView.vue';
import WorkView from '@/views/WorkView.vue';
import AuthorView from '@/views/AuthorView.vue';
import EditWorkView from '@/views/EditWorkView.vue';
import AllWorksView from '@/views/AllWorksView.vue';
import AllAuthorsView from '@/views/AllAuthorsView.vue';
import store from '@/store';


const routes = [
  {
    path: '/',
    name: "Home",
    component: HomeView,
  },
  {
    path: '/register',
    name: 'RegisterC',
    component: RegisterView,
  },
  {
    path: '/login',
    name: 'LoginC',
    component: LoginView,
  },
  {
    path: '/dashboard',
    name: 'DashboardComp',
    component: DashboardView,
    // meta: { requiresAuth: true },
  },
  {
    path: '/all',
    name: 'AllWorks',
    component: AllWorksView,
    meta: { requiresAuth: true },
  },
  {
    path: '/allAuthors',
    name: 'AllAuthors',
    component: AllAuthorsView,
    meta: { requiresAuth: true },
  },
  {
    path: '/profile',
    name: 'ProfileC',
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: '/work/:id',
    name: 'WorkC',
    component: WorkView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/author/:id',
    name: 'AuthorC',
    component: AuthorView,
    // meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/editwork/:id',
    name: 'EditWork',
    component: EditWorkView,
    meta: { requiresAuth: true },
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;
