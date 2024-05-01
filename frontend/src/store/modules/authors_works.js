import axios from "axios";

const state = {
  authorsWorksAll: null,
  authorsWorksByAuthor: null,
  authorsWorksByWork: null,
  authorsWorks: null,
  createdAuthorsWorksId: null,
};

const getters = {
  stateAuthorsWorksAll: (state) => state.authorsWorksAll,
  stateAuthorsWorks: (state) => state.authorsWorks,
  stateAuthorsWorksByAuthor: (state) => state.authorsWorksByAuthor,
  stateAuthorsWorksByWork: (state) => state.authorsWorksByWork,
  stateCreatedAuthorsWorksId: (state) => state.createdAuthorsWorksId,
};

const actions = {
  async createAuthorsWorks({ commit, dispatch }, authorsWorksData) {
    try {
      const response = await axios.post("authors_works", authorsWorksData);
      const createdAuthorsWorks = response.data; // Получаем весь объект связи автор-работа из ответа
      const createdAuthorsWorksId = createdAuthorsWorks.id; // Извлекаем ID из объекта связи
      commit("setCreatedAuthorsWorksId", createdAuthorsWorksId); // Сохраняем ID в состояние хранилища
      await dispatch("getAuthorsWorksAll");
      return createdAuthorsWorksId;
    } catch (error) {
      console.error("Failed to create authors works:", error);
      throw error;
    }
  },

  async getAuthorsWorksAll({ commit }) {
    try {
      let { data } = await axios.get("authors_works");
      commit("setAuthorsWorksAll", data);
    } catch (error) {
      console.error("Failed to get authors works:", error);
      throw error;
    }
  },

  async getAuthorsWorksByAuthorId({ commit }, authorId) {
    try {
      let { data } = await axios.get(`authors_works/author/${authorId}`);
      commit("setAuthorsWorksByAuthor", data);
    } catch (error) {
      console.error(
        `Failed to get authors works by author ID ${authorId}:`,
        error
      );
      throw error;
    }
  },

  async getAuthorsWorksByWorkId({ commit }, workId) {
    try {
      let { data } = await axios.get(`authors_works/work/${workId}`);
      commit("setAuthorsWorksByWork", data);
    } catch (error) {
      console.error(`Failed to get authors works by work ID ${workId}:`, error);
      throw error;
    }
  },

  async getAuthorsWorksById({ commit }, authorsWorksId) {
    try {
      let { data } = await axios.get(`authors_works/id/${authorsWorksId}`);
      commit("setAuthorsWorks", data);
    } catch (error) {
      console.error(
        `Failed to get authors works by ID ${authorsWorksId}:`,
        error
      );
      throw error;
    }
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteAuthorsWorksByAuthorId({}, authorId) {
    try {
      await axios.delete(`authors_works/author/${authorId}`);
    } catch (error) {
      console.error(
        `Failed to delete authors works by author ID ${authorId}:`,
        error
      );
      throw error;
    }
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteAuthorsWorksByWorkId({}, workId) {
    try {
      await axios.delete(`authors_works/work/${workId}`);
    } catch (error) {
      console.error(
        `Failed to delete authors works by work ID ${workId}:`,
        error
      );
      throw error;
    }
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteAuthorsWorksById({}, authorsWorksId) {
    try {
      await axios.delete(`authors_works/id/${authorsWorksId}`);
    } catch (error) {
      console.error(
        `Failed to delete authors works by ID ${authorsWorksId}:`,
        error
      );
      throw error;
    }
  },
};

const mutations = {
  setAuthorsWorksAll(state, authorsWorksAll) {
    state.authorsWorksAll = authorsWorksAll;
  },
  setAuthorsWorks(state, authorsWorks) {
    state.authorsWorks = authorsWorks;
  },
  setAuthorsWorksByAuthor(state, authorsWorksByAuthor) {
    state.authorsWorksByAuthor = authorsWorksByAuthor;
  },
  setAuthorsWorksByWork(state, authorsWorksByWork) {
    state.authorsWorksByWork = authorsWorksByWork;
  },
  setCreatedAuthorsWorksId(state, createdAuthorsWorksId) {
    state.createdAuthorsWorksId = createdAuthorsWorksId;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
