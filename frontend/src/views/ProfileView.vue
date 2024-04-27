<template>
  <section>
    <h1>Ваш профиль</h1>
    <hr /><br />
    <div>
      <p><strong>Полное имя:</strong> <span>{{ user.name }}</span></p>
      <p><strong>Логин:</strong> <span>{{ user.username }}</span></p>
      <p><button @click="deleteAccount()" class="btn btn-primary">Удалить аккаунт</button></p>
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'ProfileC',
  created: function () {
    return this.$store.dispatch('viewMe');
  },
  computed: {
    ...mapGetters({ user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['deleteUser']),
    async deleteAccount() {
      try {
        await this.deleteUser(this.user.id);
        await this.$store.dispatch('logOut');
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    }
  },
});
</script>
