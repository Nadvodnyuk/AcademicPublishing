<template>
  <section>
    <h1>Отредактиковать статью</h1>
    <hr /><br />

    <form @submit.prevent="submit">
      <div class="mb-3">
        <p>{{ work.title }}</p>
        <label for="status" class="form-label">Статус:</label>
        <input type="text" name="status" v-model="form.status" class="form-control" />
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
