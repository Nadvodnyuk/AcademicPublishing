<template>
  <div>
    <section>
      <h1>Статьи</h1>
      <hr /><br />
      <div class="input-group">
        <input type="search" class="form-control rounded" placeholder="Введите запрос" aria-label="Search"
          aria-describedby="search-addon" v-model="query" />
        <button type="button" class="btn btn-outline-primary rounded" @click="search()">
          Поиск
        </button>
      </div>

      <div class="row">
        <div style="width:150px">
          Выберите годы
        </div>
        <div class="col">
          <input type="text" class="form-control rounded" v-model="start_year" @change="filterFlag = false">
        </div>
        <div class="col">
          -
        </div>
        <div class="col">
          <input type="text" class="form-control rounded" v-model="end_year" @change="filterFlag = false">
        </div>
      </div>
      <br />
      <div class="filter">
        <div style="width:150px"> УДК </div>
        <div class="flex">
          <div class="UDC">
            <select class="form-select" v-model="field_value" @change="filterFlag = false">
              <option value=""></option>
              <option v-for="option in fieldRange" :key="option.value" :value="option.label">
                {{ option.label }}
              </option>
            </select>
          </div>
          <div class="col">
            <button type="button" class="btn btn-outline-primary" @click="buttonAction()"
              style="width: 110px;">
              {{ !filterFlag ? 'Применить' : 'Сбросить' }}
            </button>
          </div>
          <!-- <div class="col">
            <button type="button" class="btn btn-outline-primary" @click="undo()" style="width: 110px;">
              Сбросить
            </button>
          </div> -->
        </div>
      </div>
      <hr />
      <div class="select">
        <select class="form-select" v-model="yearValue" @change="sorting();">
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
      query: localStorage.getItem('query') || '',
      queryFlag: false,
      yearValue: 0,
      yearRange: [
        { value: 0, label: 'Год по умолчанию', },
        { value: 1, label: 'По возрастанию', },
        { value: 2, label: 'По убыванию', }
      ],
      fieldRange: [
        { value: 0, label: '0. Общий отдел. Наука и знание. Информация.Публикации в целом.', },
        { value: 1, label: '1. Философия. Психология.', },
        { value: 2, label: '2. Религия. Богословие.', },
        { value: 3, label: '3. Общественные науки.', },
        { value: 5, label: '5. Математика. Естественные науки.', },
        { value: 6, label: '6. Прикладные науки. Медицина. Технология.', },
        { value: 7, label: '7. Искусство. Фотография. Музыка. Игры. Спорт.', },
        { value: 8, label: '8. Языкознание. Лингвистика. Художественная литература. Литературоведение.', },
        { value: 9, label: '9. География. Биографии. История.', },
      ],
      start_year: 0,
      end_year: new Date().getFullYear(),
      field_value: '',
      filterFlag: false,
    };
  },

  created: function () {
    localStorage.setItem('query', this.query);
    localStorage.setItem('start_year', this.start_year);
    localStorage.setItem('end_year', this.end_year);
    localStorage.setItem('field_value', this.field_value);
    return this.$store.dispatch('searchWorks', {
      query: this.query,
      start_year: this.start_year,
      end_year: this.end_year,
      field_value: this.field_value
    });
  },

  computed: {
    ...mapGetters({
      works: 'stateWorks',
      authorsWorksByWork: 'stateAuthorsWorksByWork'
    }),
  },

  methods: {
    ...mapActions(['searchWorks']),

    async buttonAction() {
      this.filterFlag = !this.filterFlag;
      console.log(this.filterFlag)
      if (this.filterFlag == true) {
        await this.search();
      } else {
        await this.undo();
      }
    },

    async search() {
      localStorage.setItem('query', this.query);
      localStorage.setItem('start_year', this.start_year);
      localStorage.setItem('end_year', this.end_year);
      localStorage.setItem('field_value', this.field_value);
      await this.$store.dispatch('searchWorks', {
        query: this.query,
        start_year: this.start_year,
        end_year: this.end_year,
        field_value: this.field_value
      });

    },

    async sorting() {
      switch (this.yearValue) {
        case 0:
          await this.$store.dispatch('searchWorks', {
            query: this.query,
            start_year: this.start_year,
            end_year: this.end_year,
            field_value: this.field_value
          });
          break;

        case 1:
          this.works.sort((a, b) => { return a.year - b.year; });
          break;

        case 2:
          this.works.sort((a, b) => { return b.year - a.year; });
          break;
      }
    },
    async undo() {
      this.start_year = 0;
      this.end_year = new Date().getFullYear();
      this.field_value = '';
      localStorage.setItem('query', this.query);
      localStorage.setItem('start_year', this.start_year);
      localStorage.setItem('end_year', this.end_year);
      localStorage.setItem('field_value', this.field_value);
      await this.$store.dispatch('searchWorks', {
        query: this.query,
        start_year: this.start_year,
        end_year: this.end_year,
        field_value: this.field_value
      });
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
  max-width: 290px;
  margin-top: 40px;
  margin-bottom: 40px;
}

.UDC {
  display: flex;
  justify-content: center;
  max-width: 338px;
}

.col {
  display: flex;
  justify-content: center;
  max-width: 120px;
  flex: none;
}

.filter {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.flex {
  width: 83%;
  display: flex;
  justify-content: space-between;
}
</style>