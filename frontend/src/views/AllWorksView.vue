<template>
  <!-- Вывод всех работ списком, возможно сделать фильтрацию -->
  <div>
    <section>
      <h1>Статьи</h1>
      <hr /><br />

      <div v-if="works.length">
        <div v-for="work in works" :key="work.id" class="works">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <p><strong> {{ work.title }} </strong></p>
              <p>Авторы:</p>
              <!-- 
              нужно придумать, как их выводить
              можно: сначала их найти в списке авторыработы, потом их поочередно добавлять в здешний массив
              можно:
                получить список авторыработы через workID, потом дость все ID авторов и вызвать 
                функцию, которая на бэке будет получать список ID, и возвращать список авторов
              -->
              <!-- <ul>
                <li v-for="" :key="">
                  <router-link :to="{ name: 'AuthorC', params: { id: authors.id } }">{{ }}</router-link>
                </li>
              </ul> -->
              <router-link :to="{ name: 'WorkC', params: { id: work.id } }">Посмотреть полностью</router-link>
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
import { mapGetters} from 'vuex'; //, mapActions 

export default defineComponent({
  name: 'AllWorks',
  data() {
    return {
      authors: {

      },
    };
  },

  created: function () {
    return this.$store.dispatch('getWorks');
  },

  computed: {
    ...mapGetters({
      works: 'stateWorks',
      authors: 'stateAuthors',
      authorsWorksByWork: 'stateAuthorsWorksByWork'
    }),
  },

  methods: {
    // ...mapActions([' ']),
  },
});
</script>