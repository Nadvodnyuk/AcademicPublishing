<template>
  <!-- 
  Что-то об авторах
  -->

  <!-- 
  нужно придумать, как их выводить
  можно: сначала их найти в списке авторыработы, потом их поочередно добавлять в здешний массив
  можно:
    получить список авторыработы через workID, потом дость все ID авторов и вызвать 
    функцию, которая на бэке будет получать список ID, и возвращать список авторов
  -->

  <div v-if="work">
    <p><strong> {{ work.title }} </strong></p>
    <p>{{ work.year }}</p>

    <p>Организация: {{ work.org }}</p>
    <p v-if="work.sub_org">Подразделение: {{ work.sub_org }}</p>

    <p v-if="work.mentor">Научные руководители: {{ work.mentor }}</p>
    <p v-if="work.consultant">Научные консультанты: {{ work.consultant }}</p>

    <p><strong>Аннотация</strong></p>
    <p>{{ work.abstract }}</p>

    <p><strong>Ключевые слова</strong></p>
    <p>{{ work.key_words }}</p>

    <p><strong>Введение</strong></p>
    <p>{{ work.intro }}</p>

    <p><strong>Цель</strong></p>
    <p>{{ work.aim }}</p>

    <p><strong>Материалы и методы</strong></p>
    <p>{{ work.materials_methods }}</p>

    <p><strong>Результаты и обсуждение</strong></p>
    <p>{{ work.results }}</p>

    <p><strong>Заключение</strong></p>
    <p>{{ work.conclusion }}</p>

    <p><strong>Список источников</strong></p>
    <p>{{ work.literature }}</p>

    <p><strong>О работе</strong></p>
    <p v-if="work.field">УДК: {{ work.field }}</p>
    <p v-if="work.event">Подготовлено для: {{ work.event }}</p>
    <p v-if="work.status">Статус работы: {{ work.status }}</p>

    <p>
      <router-link :to="{ name: 'EditWork', params: { id: work.id } }" class="btn btn-primary">
        Редактировать статус
      </router-link>
    </p>
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'WorkC',
  props: ['id'],
  async created() {
    try {
      await this.viewWork(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/all');
    }
  },
  computed: {
    ...mapGetters({ work: 'stateWork' }),
  },
  methods: {
    ...mapActions([
      'viewWork',
      'deleteWork',
      'deleteAuthorsWorksByWorkId'
    ]),

    async removeWork() {
      try {
        await this.deleteWork(this.id);
        await this.deleteAuthorsWorksByWorkId(this.id);
        this.$router.push('/all');
      } catch (error) {
        console.error(error);
      }
    },
  }
});
</script>
