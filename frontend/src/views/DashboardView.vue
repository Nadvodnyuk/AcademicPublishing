<template>
  <!-- 
    Здесь должны записываться авторы и статья 
    максимум 4 формы с авторами, одна статья
    поочередно: создать авторов и вернуть их id
    получить id статьи
    я должна здесь взять id авторов и id статьи
    потом в таблицу статьи авторы записать их
  -->
  <div>
    <section>
      <h1>
        Создать статью
      </h1>
      <hr /><br />
      <h3 v-if="showModal" style="color:green; margin-bottom: 25px;">
        Статья отправлена!
      </h3>
      <form @submit.prevent="submit">


        <!-- Автор -->

        <div>
          <div class="mb-3">
            <label for="full_name" class="form-label">Полное имя:</label>
            <input type="text" name="full_name" v-model="author.full_name" class="form-control"
              @click="showModal = false" />
          </div>
          <div class="mb-3">
            <label for="short_name" class="form-label">Краткая форма имени:</label>
            <input type="text" name="short_name" v-model="author.short_name" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="code" class="form-label">Код:</label>
            <input type="text" name="code" v-model="author.code" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="a_status" class="form-label">Статус:</label>
            <input type="text" name="a_status" v-model="author.a_status" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="a_country" class="form-label">Страна:</label>
            <input type="text" name="a_country" v-model="author.a_country" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="a_city" class="form-label">Город:</label>
            <input type="text" name="a_city" v-model="author.a_city" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="a_index" class="form-label">Индекс:</label>
            <input type="text" name="a_index" v-model="author.a_index" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="a_adress" class="form-label">Адрес:</label>
            <input type="text" name="a_adress" v-model="author.a_adress" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="a_org" class="form-label">Организация:</label>
            <input type="text" name="a_org" v-model="author.a_org" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="a_sub_org" class="form-label">Подразделение:</label>
            <input type="text" name="a_sub_org" v-model="author.a_sub_org" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="phone" class="form-label">Телефон:</label>
            <input type="text" name="phone" v-model="author.phone" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email:</label>
            <input type="email" name="email" v-model="author.email" class="form-control" />
          </div>
        </div>



        <!-- Работа -->



        <div class="mb-3">
          <label for="field" class="form-label">Сфера работы:</label>
          <input type="text" name="field" v-model="work.field" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="title" class="form-label">Название статьи:</label>
          <input type="text" name="title" v-model="work.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="event" class="form-label">Событие:</label>
          <input type="text" name="event" v-model="work.event" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="status" class="form-label">Статус:</label>
          <input type="text" name="status" v-model="work.status" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="year" class="form-label">Год:</label>
          <input type="text" name="year" v-model="work.year" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="org" class="form-label">Организация:</label>
          <input type="text" name="org" v-model="work.org" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="sub_org" class="form-label">Подразделение:</label>
          <input type="text" name="sub_org" v-model="work.sub_org" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="country" class="form-label">Страна:</label>
          <input type="text" name="country" v-model="work.country" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="city" class="form-label">Город:</label>
          <input type="text" name="city" v-model="work.city" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="index" class="form-label">Индекс:</label>
          <input type="text" name="index" v-model="work.index" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="mentor" class="form-label">Научный руководитель:</label>
          <input type="text" name="mentor" v-model="work.mentor" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="consultant" class="form-label">Консультант:</label>
          <input type="text" name="consultant" v-model="work.consultant" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="abstract" class="form-label">Аннотация:</label>
          <textarea name="abstract" v-model="work.abstract" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="key_words" class="form-label">Ключевые слова:</label>
          <input type="text" name="key_words" v-model="work.key_words" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="intro" class="form-label">Введение:</label>
          <textarea name="intro" v-model="work.intro" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="aim" class="form-label">Цель:</label>
          <textarea name="aim" v-model="work.aim" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="materials_methods" class="form-label">Материалы и методы:</label>
          <textarea name="materials_methods" v-model="work.materials_methods" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="results" class="form-label">Результаты:</label>
          <textarea name="results" v-model="work.results" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="conclusion" class="form-label">Заключение:</label>
          <textarea name="conclusion" v-model="work.conclusion" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="literature" class="form-label">Литература:</label>
          <textarea name="literature" v-model="work.literature" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">
          Отправить
        </button>
      </form>
    </section>

    <br /><br />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'DashboardComp',
  data() {
    return {
      work: {
        field: '',
        title: '',
        event: '',
        status: '',
        year: '',
        org: '',
        sub_org: '',
        country: '',
        city: '',
        index: '',
        mentor: '',
        consultant: '',
        abstract: '',
        key_words: '',
        intro: '',
        aim: '',
        materials_methods: '',
        results: '',
        conclusion: '',
        literature: '',
      },

      author: {
        full_name: '',
        short_name: '',
        code: '',
        a_status: '',
        a_country: '',
        a_city: '',
        a_index: '',
        a_adress: '',
        a_org: '',
        a_sub_org: '',
        phone: '',
        email: '',
      },
      form: {
        author_id_id: 0,
        work_id_id: 0
      },
      showModal: false,
    };
  },
  created: function () {
  },
  computed: {
    ...mapGetters({
      works: 'stateWorks',
      work_id_id: 'stateCreatedWorkId',
      author_id_id: 'stateCreatedAuthorId'
    }),

  },
  methods: {
    ...mapActions(['createWork', 'createAuthor', 'createAuthorsWorks']),
    async submit() {
      await this.createAuthor(this.author);
      await this.createWork(this.work);

      let authorsWorksData = {
        author_id_id: this.$store.getters.stateCreatedAuthorId,
        work_id_id: this.$store.getters.stateCreatedWorkId
      };
      await this.createAuthorsWorks(authorsWorksData);
      this.showModal = true;
    },
  },
});
</script>