<template>
  <section>
    <div v-if="isLoggedIn" id="logout">
      <p>Информационная система по анализу публикационной активности.</p>
      <p>Вы можете:</p>
      <p id="logout">
      <ul>
        <li>
          <router-link class="nav-link" to="/all" style="color: #0d6efd;">
            Просмотреть все статьи
          </router-link>
        </li>
        <li>
          <router-link class="nav-link" to="/allAuthors" style="color: #0d6efd;">
            Просмотреть всех авторов
          </router-link>
        </li>
      </ul>
      </p>
    </div>
    <div v-else>
      <p>Информационная система для отправки статей.</p>
      <p>Вы можете:</p>
      <ul>
        <li>
          <router-link class="nav-link" to="/dashboard" style="color: #0d6efd;">
            Создать статью
          </router-link>
        </li>
        <li>
          <a href="/login">Войти</a>
        </li>
      </ul>
    </div>
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
