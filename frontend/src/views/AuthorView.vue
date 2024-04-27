<template>
    <div v-if="author">
        <p><strong> {{ author.full_name }} </strong></p>
        <p> {{ author.short_name }} </p>
        <p>Введение: {{ author.code }}</p>
        <p>Код: {{ author.a_status }}</p>
        <p>Адрес: {{ author.a_country }}, {{ author.a_city }}</p>
        <p>{{ author.a_index }}, {{ author.a_adress }}</p>
        <p>Организация: {{ author.a_org }}</p>
        <p v-if="author.a_sub_org">Подразделение: {{ author.a_sub_org }}</p>
        <p>Телефон: {{ author.phone }}</p>
        <p>E-mail: {{ author.email }}</p>

        <p>
            <button @click="removeAuthor()" class="btn btn-secondary">
                Удалить статью
            </button>
        </p>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
    name: 'AuthorC',
    props: ['id'],
    async created() {
        try {
            await this.viewAuthor(this.id);
        } catch (error) {
            console.error(error);
            this.$router.push('/all');
        }
    },
    computed: {
        ...mapGetters({ author: 'stateAuthor' }),
    },
    methods: {
        ...mapActions([
            'viewAuthor',
            'deleteAuthor',
            'deleteAuthorsWorksByAuthorId'
        ]),

        async removeAuthor() {
            try {
                await this.deleteAuthor(this.id);
                await this.deleteAuthorsWorksByAuthorId(this.id);
                this.$router.push('/all');
            } catch (error) {
                console.error(error);
            }
        },
    },
});
</script>