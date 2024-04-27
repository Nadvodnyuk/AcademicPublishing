<template>
  <section>
    <p>Веб-приложение для отправки статей.</p>

    <div v-if="isLoggedIn" id="logout">
      <p>Вы можете</p>
      <p id="logout">
      <ul>
        <li>
          <router-link class="nav-link" to="/dashboard" style="color: #0d6efd;">
            Создать статью
          </router-link>
        </li>
        <li>
          <router-link class="nav-link" to="/all" style="color: #0d6efd;">
            Просмотреть все статьи
          </router-link>
        </li>
      </ul>


      </p>
    </div>
    <p v-else>
      <span><a href="/register">Зарегистрироваться</a></span>
      <span> или </span>
      <span><a href="/login">Войти</a></span>
    </p>
  </section>
</template>
<script>

import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    }
  },
});
</script>
