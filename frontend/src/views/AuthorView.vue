<template>
  <div v-if="author">
    <h1>{{ author.full_name }}</h1>
    <hr /><br />
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
        <td><a :href="'tel:' + author.phone" class="link">{{ author.phone }}</a></td>
      </tr>
      <tr>
        <td class="label-cell"><strong>E-mail</strong></td>
        <td><a :href="'mailto:' + author.email" class="link">{{ author.email }}</a></td>
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
      Посмотреть данные об авторе за:
    </p>
    <div v-if="graphs">
      <select v-model="selectedYear" class="form-select">
        <option v-for="year in years" :key="year.key" :value="year.key">
          {{ year.year }} год
        </option>
      </select>
      <br />
      <div class="graphs">
        <img v-if="graphs" :src="graphs[selectedYear]" alt="График статей" class="graphsImg">
        <p v-else> Работы {{ author.short_name }} не представлены на этом сайте.</p>
      </div>
    </div>
    <hr /><br />
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
  data() {
    return {
      selectedYear: null,
      src: ''
    };
  },
  async created() {
    try {
      await this.viewAuthor(this.id);
      await this.viewGraphs(this.id);
      this.selectedYear = this.years[this.years.length - 1].key;
    } catch (error) {
      console.error(error);
      this.$router.push('/all');
    }
  },
  computed: {
    ...mapGetters({
      author: 'stateAuthor',
      graphs: 'stateGraphs',
      years: 'stateUniqueYears'
    }),
  },
  methods: {
    ...mapActions([
      'viewAuthor',
      'deleteAuthor',
      'deleteAuthorsWorksByAuthorId',
      'viewGraphs'
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

.table {
  margin-bottom: 50px;
}

.graphs {
  display: flex;
  justify-content: center;

}

.graphsImg {
  display: flex;
  justify-content: center;
  width: 830px;
  height: auto;
}

.table> :not(caption)>*>* {
  padding: 0;
}
</style>