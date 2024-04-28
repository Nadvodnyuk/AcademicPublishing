<template>
  <!-- Вывод всех работ списком, сделать фильтрацию -->
  <div>
    <section>
      <h1>Статьи</h1>
      <hr /><br />
      <div class="input-group">
        <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search"
          aria-describedby="search-addon" v-model="query" />
        <button type="button" class="btn btn-outline-primary" @click="search">search</button>
      </div>
      <div class="select">
        <select class="form-select" aria-label="nameValue" v-model="yearValue" @change="sorting">
          <option v-for="option in yearRange" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>
      <div v-if="works">
        <div v-for="work in works" :key="work.id" class="works">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <p><strong> {{ work.title }} </strong></p>
              <ul>
                <li v-for="(author, index) in work.author" :key="index">
                  <router-link :to="{ name: 'AuthorC', params: { id: author.author_id.id } }">
                    {{ author.author_id.short_name }}
                  </router-link>
                </li>
              </ul>
              <router-link :to="{ name: 'WorkC', params: { id: work.id } }">
                Посмотреть полностью
              </router-link>
            </div>
          </div>
          <br />
        </div>
      </div>

      <div v-else>
        <p>Здесь нет статей.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'AllWorks',
  data() {
    return {
      query: '',
      queryFlag: false,
      yearValue: 0,
      yearRange: [
        { value: 0, label: 'Год по умолчанию', },
        { value: 1, label: 'По возрастанию', },
        { value: 2, label: 'По убыванию', }
      ]
    };
  },

  created: function () {
    return this.$store.dispatch('searchWorks', this.query);
  },

  computed: {
    ...mapGetters({
      works: 'stateWorks',
      authorsWorksByWork: 'stateAuthorsWorksByWork'
    }),
  },

  methods: {
    ...mapActions(['searchWorks']),
    async search() {
      await this.$store.dispatch('searchWorks', this.query);
    },

    async sorting() {
      switch (this.yearValue) {
        case 0:
          await this.$store.dispatch('searchWorks', this.query);
          break;

        case 1:
          this.works.sort((a, b) => { return a.year - b.year; });
          break;

        case 2:
          this.works.sort((a, b) => { return b.year - a.year; });
          break;
      }
    },
  },
  watch: {
    query(newValue) {
      if (newValue.trim() == '') {
        this.search();
      }
    }
  }
});
</script>

<style>
.input-group {
  margin-bottom: 40px;
}

.select {
  display: flex;
  justify-content: center;
  width: 290px;
  margin-top: 40px;
  margin-bottom: 40px;
}
</style>