<template>
  <!-- Вывод всех работ списком, сделать фильтрацию -->
  <div>
    <section>
      <h1>Авторы</h1>
      <hr /><br />

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
import { mapGetters } from 'vuex'; //, mapActions 

export default defineComponent({
  name: 'AllAuthors',
  data() {
    return {
    };
  },

  created: function () {
    return this.$store.dispatch('getAuthors');
  },

  computed: {
    ...mapGetters({
      authors: 'stateAuthors',
      authorsAuthorsByAuthor: 'stateAuthorsAuthorsByAuthor'
    }),
  },

  methods: {
    // ...mapActions([' ']),
  },
});
</script>