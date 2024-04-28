<template>
  <!-- Вывод всех работ списком, сделать фильтрацию -->
  <div>
    <section>
      <h1>Статьи</h1>
      <hr /><br />
      <div class="input-group">
        <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search"
          aria-describedby="search-addon" v-model="query"/>
        <button type="button" class="btn btn-outline-primary" @click="search">search</button>
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
import { mapGetters, mapActions  } from 'vuex';

export default defineComponent({
  name: 'AllWorks',
  data() {
    return {
      query: '',
      queryFlag: false,
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
.input-group{
  margin-bottom: 40px;
}
</style>