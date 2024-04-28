<template>
  <!-- Вывод всех работ списком, сделать фильтрацию -->
  <div>
    <section>
      <h1>Авторы</h1>
      <hr /><br />
      <div class="input-group">
        <input type="search" class="form-control rounded" placeholder="Search" aria-label="Search"
          aria-describedby="search-addon" v-model="query"/>
        <button type="button" class="btn btn-outline-primary" @click="search">search</button>
      </div>
      <div v-if="authors">
        <div v-for="author in authors" :key="author.id" class="authors">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <p><strong> {{ author.full_name }} </strong></p>
              <router-link :to="{ name: 'AuthorC', params: { id: author.id } }">
                Посмотреть автора
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
  name: 'AllAuthors',
  data() {
    return {
      query: '',
      queryFlag: false,
    };
  },

  created: function () {
    return this.$store.dispatch('searchAuthors', this.query);
  },

  computed: {
    ...mapGetters({
      authors: 'stateAuthors',
      authorsAuthorsByAuthor: 'stateAuthorsAuthorsByAuthor'
    }),
  },

  methods: {
   ...mapActions(['searchAuthors']),
   async search() {
      await this.$store.dispatch('searchAuthors', this.query);
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