<template>
  <section>
    <h1>Отредактиковать статью</h1>
    <hr /><br />

    <form @submit.prevent="submit">
      <div class="mb-3">
        <p>{{ work.title }}</p>
        <label for="status" class="form-label">Статус:</label>
        <select class="form-select" v-model="form.status">
          <option v-for="option in statuses" :key="option.value" :value="option.label">
            {{ option.label }}
          </option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'EditWork',
  props: ['id'],
  data() {
    return {
      form: {
        status: '',
      },
      statuses: [
        { value: 0, label: 'Препринт', },
        { value: 1, label: 'Тезис', },
        { value: 2, label: 'Доклад', },
        { value: 3, label: 'Журнал', },
        { value: 4, label: 'Печать', },
        { value: 5, label: 'Энциклопедия', },
        { value: 6, label: 'Рецензирование', },
        { value: 7, label: 'Редактирование', },
        { value: 8, label: 'Плагиат', },
      ],
    };
  },
  created: function () {
    this.GetWork();
  },
  computed: {
    ...mapGetters({ work: 'stateWork' }),
  },
  methods: {
    ...mapActions(['updateWork', 'viewWork']),

    async submit() {
      try {
        let work = {
          id: this.id,
          form: this.form,
        };

        console.log(work);
        await this.updateWork(work);
        this.$router.push({ name: 'WorkC', params: { id: this.work.id } });
      } catch (error) {
        console.log(error);
      }
    },

    async GetWork() {
      try {
        await this.viewWork(this.id);
        this.form.status = this.work.status;
      } catch (error) {
        console.error(error);
        this.$router.push('/all');
      }
    }
  },
});
</script>
