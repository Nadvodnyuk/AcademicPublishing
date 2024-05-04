<template>
  <div>
    <section>
      <h3 v-if="showModal == true" class="mod">Статья отправлена!</h3>
      <h1>Создать статью</h1>
      <hr />
      <br />
      <form @submit.prevent="submit">
        <p><strong> СВЕДЕНИЯ ОБ АВТОРАХ </strong></p>
        <p class="details">Всего в работе может быть до 4 авторов. Чтобы добавить автора нажмите на кнопку "Добавить
          автора" в конце формы.Чтобы удалить автора кликните 2 раза на подпись "АВТОР".</p>
        <br />
        <div>
          <div class="mb-3" v-for="(a, key, index) in authors" :key="key">
            <div class="mb-3" @dblclick="deleteAuthor(key)">
              АВТОР {{ index + 1 }}
            </div>
            <div>
              <div class="mb-3">
                <label for="full_name" class="form-label">Полные фамилия, имя, отчество (при наличии)</label>
                <input type="text" name="full_name" v-model="authors[key].full_name" class="form-control"
                  @click="showModal = false" />
              </div>
              <div class="mb-3">
                <label for="short_name" class="form-label">Краткая форма имени</label>
                <input type="text" name="short_name" v-model="authors[key].short_name" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="code" class="form-label">Код научного автора</label>
                <input type="text" name="code" v-model="authors[key].code" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="a_status" class="form-label">Статус автора</label>
                <p class="details">2 курс, факультет ФКТИ; специалист 2 года подготовки по специальности «Компьютерная
                  безопасность»; магистрант 2 года подготовки по специальности «Лингвистика»; доцент кафедры микро- и
                  наноэлектроника и т.д.</p>
                <input type="text" name="a_status" v-model="authors[key].a_status" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="a_country" class="form-label">Страна автора</label>
                <input type="text" name="a_country" v-model="authors[key].a_country" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="a_city" class="form-label">Город автора</label>
                <input type="text" name="a_city" v-model="authors[key].a_city" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="a_index" class="form-label">Индекс организации автора</label>
                <input type="text" name="a_index" v-model="authors[key].a_index" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="a_adress" class="form-label">Полный адрес организации автора</label>
                <input type="text" name="a_adress" v-model="authors[key].a_adress" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="a_org" class="form-label">Организация автора (без указания ФГБОУ ВО и т.п.)</label>
                <input type="text" name="a_org" v-model="authors[key].a_org" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="a_sub_org" class="form-label">Подразделение организации автора</label>
                <p class="details">При наличии</p>
                <input type="text" name="a_sub_org" v-model="authors[key].a_sub_org" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="phone" class="form-label">Номер телефона автора</label>
                <input type="text" name="phone" v-model="authors[key].phone" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="email" class="form-label">Рабочий e-mail автора</label>
                <input type="email" name="email" v-model="authors[key].email" class="form-control" />
              </div>
            </div>
          </div>
        </div>
        <div class="mb-3" v-if="Object.keys(authors).length < 4">
          <input type="button" class="btn btn-primary" value="Добавить автора" @click="addAuthor()" />
        </div>

        <p class="data">
          <strong> СВЕДЕНИЯ О РАБОТЕ </strong>
        </p>

        <div class="mb-3">
          <label for="field" class="form-label">УДК</label>
          <p class="details"> <a href="https://www.triumph.ru/html/serv/udk.html">Классификатор УДК</a>. Если
            затрудняеетесь, то выберете УДК из выпадающего списка</p>
          <input type="text" list="datalistOptions" name="field" v-model="work.field" class="form-control" />
          <datalist id="datalistOptions">
            <option value="0. Общий отдел. Наука и знание. Информация.Публикации в целом."></option>
            <option value="1. Философия. Психология."></option>
            <option value="2. Религия. Богословие."></option>
            <option value="3. Общественные науки."></option>
            <option value="5. Математика. Естественные науки."></option>
            <option value="6. Прикладные науки. Медицина. Технология."></option>
            <option value="7. Искусство. Фотография. Музыка. Игры. Спорт."></option>
            <option value="8. Языкознание. Лингвистика. Художественная литература. Литературоведение."></option>
            <option value="9. География. Биографии. История."></option>
          </datalist>
        </div>
        <div class="mb-3">
          <label for="title" class="form-label">Название научной работы</label>
          <input type="text" name="title" v-model="work.title" class="form-control uppercase-input" />
        </div>
        <div class="mb-3">
          <label for="event" class="form-label">Событие</label>
          <p class="details">Официальное название события, для которого подготовлена научная работа. Если работа
            подготовлена не к событию, то введите "Нет"</p>
          <input type="text" name="event" v-model="work.event" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="status" class="form-label">Статус статьи</label>
          <p class="details">Если статья не была нигде опубликована или представлена, то выберете статус "Препринт"</p>
          <select class="form-select" v-model="work.status">
            <option v-for="option in statuses" :key="option.value" :value="option.label">
              {{ option.label }}
            </option>
          </select>
        </div>
        <div class="mb-3">
          <label for="year" class="form-label">Год написания научной работы</label>
          <input type="text" name="year" v-model="work.year" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="org" class="form-label">Организации авторов (без указания ФГБОУ ВО и т.п.)</label>
          <p class="details">Если их несколько, то перечислять через запятую</p>
          <input type="text" name="org" v-model="work.org" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="sub_org" class="form-label">Подразделение</label>
          <p class="details">При наличии. Если их несколько, то перечислять через запятую</p>
          <input type="text" name="sub_org" v-model="work.sub_org" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="country" class="form-label">Страна</label>
          <input type="text" name="country" v-model="work.country" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="city" class="form-label">Город</label>
          <input type="text" name="city" v-model="work.city" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="index" class="form-label">Индекс</label>
          <input type="text" name="index" v-model="work.index" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="mentor" class="form-label">Научные руководители</label>
          <p class="details">При наличии. Если их несколько, то перечислять через запятую</p>
          <input type="text" name="mentor" v-model="work.mentor" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="consultant" class="form-label">Научные консультанты</label>
          <p class="details">При наличии. Если их несколько, то перечислять через запятую</p>
          <input type="text" name="consultant" v-model="work.consultant" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="abstract" class="form-label">Аннотация</label>
          <p class="details">Изложение сути работы, до 50 слов </p>
          <textarea name="abstract" v-model="work.abstract" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="key_words" class="form-label">Ключевые слова</label>
          <p class="details">До 10 слов или словосочетаний, которые отражают тему, предмет и результаты исследования</p>
          <input type="text" name="key_words" v-model="work.key_words" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="intro" class="form-label">Введение</label>
          <textarea name="intro" v-model="work.intro" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="aim" class="form-label">Цель</label>
          <textarea name="aim" v-model="work.aim" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="materials_methods" class="form-label">Материалы и методы</label>
          <textarea name="materials_methods" v-model="work.materials_methods" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="results" class="form-label">Результаты</label>
          <textarea name="results" v-model="work.results" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="conclusion" class="form-label">Заключение</label>
          <textarea name="conclusion" v-model="work.conclusion" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="literature" class="form-label">Список источников</label>
          <p class="details">Список использованных источников должен быть выполнен в соответствии с
            <a
              href="https://sgugit.ru/science-and-innovations/dissertation-councils/normative-documents/Гост%20Р%207.0.100-2018%20по%20оформлению%20списка%20литературы..pdf">
              ГОСТ Р7.0.100-2018 «Библиографическая запись. Библиографическое описание. Общие требования и правила
              составления»</a>
          </p>
          <textarea name="literature" v-model="work.literature" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>
      </form>
    </section>

    <br /><br />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { mapGetters, mapActions } from "vuex";

export default defineComponent({
  name: "DashboardComp",
  data() {
    return {
      work: {
        field: "",
        title: "",
        event: "",
        status: "",
        year: "",
        org: "",
        sub_org: "",
        country: "",
        city: "",
        index: "",
        mentor: "",
        consultant: "",
        abstract: "",
        key_words: "",
        intro: "",
        aim: "",
        materials_methods: "",
        results: "",
        conclusion: "",
        literature: "",
      },

      form: {
        author_id_id: 0,
        work_id_id: 0,
      },

      authors: {
        1: {
          full_name: "",
          short_name: "",
          code: "",
          a_status: "",
          a_country: "",
          a_city: "",
          a_index: "",
          a_adress: "",
          a_org: "",
          a_sub_org: "",
          phone: "",
          email: "",
        },
      },
      authorIterator: 1,
      showModal: false,
      statuses: [
        { value: 0, label: 'Препринт', },
        { value: 1, label: 'Тезис', },
        { value: 2, label: 'Доклад', },
        { value: 3, label: 'Журнал', },
        { value: 4, label: 'Печать', },
        { value: 5, label: 'Энциклопедия', },
      ],
    };
  },
  created: function () { },
  computed: {
    ...mapGetters({
      works: "stateWorks",
      work_id_id: "stateCreatedWorkId",
      author_id_id: "stateCreatedAuthorId",
    }),
  },
  methods: {
    ...mapActions(["createWork", "createAuthor", "createAuthorsWorks"]),
    async submit() {
      await this.createWork(this.work);

      for (const author of Object.values(this.authors)) {
        author.full_name = author.full_name.trim();
        author.code = author.code.trim();
        await this.createAuthor(author);
        let authorsWorksData = {
          author_id_id: this.$store.getters.stateCreatedAuthorId,
          work_id_id: this.$store.getters.stateCreatedWorkId,
        };
        await this.createAuthorsWorks(authorsWorksData);
      }

      this.showModal = true;
      setTimeout(() => {
        this.showModal = false;
      }, 20000);
      this.scrollToTop();
      this.scrap();
    },
    addAuthor() {
      this.authorIterator++;
      this.authors[this.authorIterator] = {
        full_name: "",
        short_name: "",
        code: "",
        a_status: "",
        a_country: "",
        a_city: "",
        a_index: "",
        a_adress: "",
        a_org: "",
        a_sub_org: "",
        phone: "",
        email: "",
      };
    },
    deleteAuthor(id) {
      if (Object.keys(this.authors).length <= 1) {
        return;
      }
      delete this.authors[id];
    },
    scrollToTop() {
      window.scrollTo(0, 0);
    },
    scrap() {
      this.work = {
        field: "",
        title: "",
        event: "",
        status: "",
        year: "",
        org: "",
        sub_org: "",
        country: "",
        city: "",
        index: "",
        mentor: "",
        consultant: "",
        abstract: "",
        key_words: "",
        intro: "",
        aim: "",
        materials_methods: "",
        results: "",
        conclusion: "",
        literature: "",
      };

      this.authors = {
        1: {
          full_name: "",
          short_name: "",
          code: "",
          a_status: "",
          a_country: "",
          a_city: "",
          a_index: "",
          a_adress: "",
          a_org: "",
          a_sub_org: "",
          phone: "",
          email: "",
        },
      };
      this.authorIterator = 1;
    },
  },
});
</script>

<style>
.data {
  margin-top: 50px;
}

.mod {
  color: green;
  margin-bottom: 25px;
}

.details {
  font-size: 12.5px;
}

.uppercase-input {
  text-transform: uppercase;
}
</style>
