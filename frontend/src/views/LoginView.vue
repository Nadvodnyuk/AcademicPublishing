<template>
  <section>
    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="username" class="form-label">Логин:</label>
        <input type="text" name="username" v-model="form.username" class="form-control" autocomplete="username"/>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Пароль:</label>
        <input type="password" name="password" v-model="form.password" class="form-control" autocomplete="current-password"/>
      </div>
      <button type="submit" class="btn btn-primary">Войти</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
  name: 'LoginC',
  data() {
    return {
      form: {
        username: '',
        password: '',
      }
    };
  },
  methods: {
    ...mapActions(['logIn']),
    async submit() {
      const User = new FormData();
      User.append('username', this.form.username);
      User.append('password', this.form.password);
      await this.logIn(User);
      this.$router.push('/');
    }
  }
});
</script>
