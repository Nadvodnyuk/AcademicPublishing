<template>
  <div>
    <section>
      <h1>Авторы</h1>
      <hr />
      <br />
      <div class="input-group">
        <input type="search" class="form-control rounded" placeholder="Введите запрос" aria-label="Search"
          aria-describedby="search-addon" v-model="query" />
        <button type="button" class="btn btn-outline-primary" @click="search()">
          search
        </button>
      </div>
      <div class="select">
        <select class="form-select" v-model="nameValue" @change="sorting()">
          <option v-for="option in nameRange" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>
      <div v-if="authors">
        <div v-for="author in authors" :key="author.id" class="authors">
          <div class="card" style="width: 18rem">
            <div class="card-body">
              <p>
                <strong> {{ author.full_name }} </strong>
              </p>
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
import { defineComponent } from "vue";
import { mapGetters, mapActions } from "vuex";

export default defineComponent({
  name: "AllAuthors",
  data() {
    return {
      query: "",
      queryFlag: false,
      nameValue: 0,
      nameRange: [
        { value: 0, label: "Имя по умолчанию" },
        { value: 1, label: "А - Я" },
        { value: 2, label: "Я - А" },
      ],
    };
  },

  created: function () {
    return this.$store.dispatch("searchAuthors", this.query);
  },

  computed: {
    ...mapGetters({
      authors: "stateAuthors",
      authorsAuthorsByAuthor: "stateAuthorsAuthorsByAuthor",
    }),
  },

  methods: {
    ...mapActions(["searchAuthors"]),
    async search() {
      await this.$store.dispatch("searchAuthors", this.query);
    },

    async sorting() {
      switch (this.nameValue) {
        case 0:
          await this.$store.dispatch("searchAuthors", this.query);
          break;
        case 1:
          this.authors.sort((a, b) => a.full_name.localeCompare(b.full_name));
          break;

        case 2:
          this.authors.sort((a, b) => b.full_name.localeCompare(a.full_name));
          break;
      }
    },
  },
  watch: {
    query(newValue) {
      if (newValue.trim() == "") {
        this.search();
      }
    },
  },
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
