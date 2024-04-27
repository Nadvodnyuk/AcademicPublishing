<template>
  <div v-if="author">
    <table class="table">
      <tr>
        <td class="label-cell"><strong>Полное имя</strong></td>
        <td>{{ author.full_name }}</td>
      </tr>
      <tr>
        <td class="label-cell"><strong>Краткое имя</strong></td>
        <td>{{ author.short_name }}</td>
      </tr>
      <tr>
        <td class="label-cell"><strong>Код</strong></td>
        <td>{{ author.code }}</td>
      </tr>
      <tr>
        <td class="label-cell"><strong>Статус</strong></td>
        <td>{{ author.a_status }}</td>
      </tr>
      <tr>
        <td class="label-cell"><strong>Город</strong></td>
        <td>{{ author.a_city }}, {{ author.a_country }}</td>
      </tr>
      <tr>
        <td class="label-cell"><strong>Адрес</strong></td>
        <td>{{ author.a_index }}, {{ author.a_adress }}</td>
      </tr>
      <tr>
        <td class="label-cell"><strong>Организация</strong></td>
        <td>{{ author.a_org }}</td>
      </tr>
      <tr v-if="author.a_sub_org">
        <td class="label-cell"><strong>Подразделение</strong></td>
        <td>{{ author.a_sub_org }}</td>
      </tr>
      <tr>
        <td class="label-cell"><strong>Телефон</strong></td>
        <td>{{ author.phone }}</td>
      </tr>
      <tr>
        <td class="label-cell"><strong>E-mail</strong></td>
        <td>{{ author.email }}</td>
      </tr>
    </table>
    <p>
      Статьи автора:
    </p>
    <ul>
      <li v-for="(work, index) in author.work" :key="index">
        <router-link :to="{ name: 'WorkC', params: { id: work.work_id.id } }">
          {{ work.work_id.title }}
        </router-link>
      </li>
    </ul>
    <p>
      <button @click="removeAuthor()" class="btn btn-secondary">
        Удалить автора
      </button>
    </p>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'AuthorC',
  props: ['id'],
  async created() {
    try {
      await this.viewAuthor(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/all');
    }
  },
  computed: {
    ...mapGetters({ author: 'stateAuthor' }),
  },
  methods: {
    ...mapActions([
      'viewAuthor',
      'deleteAuthor',
      'deleteAuthorsWorksByAuthorId'
    ]),

    async removeAuthor() {
      try {
        await this.deleteAuthor(this.id);
        this.$router.push('/all');
      } catch (error) {
        console.error(error);
      }
    },
  },
});
</script>
<style>
.label-cell {
  width: 150px;
}
.table{
  margin-bottom: 50px;
}
</style>