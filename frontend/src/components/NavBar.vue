<template>
  <header>
    <nav class="navbar navbar-expand-md navbar-dark " style="background-color: #2c3e50;">
      <div class="container" style=" margin-left: 42px;">
        <router-link class="navbar-brand" to="/">Статьи
        </router-link>
        <button class="navbar-toggler" 
        type="button" 
        data-bs-toggle="collapse" 
        data-bs-target="#navbarCollapse"
        aria-controls="navbarCollapse" 
        aria-expanded="false" 
        aria-label="Toggle navigation">
          <span class="navbar-toggler-icon">
          </span>
        </button>
        <div 
          class="collapse navbar-collapse" 
          id="navbarCollapse"  
          style="flex-grow: 0;">
          <ul v-if="isLoggedIn" class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/dashboard">Создать статью
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/all">Все статьи
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/profile">Мой профиль
              </router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" @click="logout">Выйти
              </a>
            </li>
          </ul>
          <ul v-else class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Главная
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/register">Зарегистрироваться
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/login">Войти
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'NavBar',
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    async logout() {
      await this.$store.dispatch('logOut');
      this.$router.push('/login');
    }
  },
});
</script>

<style scoped>
a {
  cursor: pointer;
}
</style>
