import axios from "axios";

const state = {
  authors: null,
  author: null,
  createdAuthorId: null,
  graphs: [],
  uniqueYears:{},
};

const getters = {
  stateAuthors: (state) => state.authors,
  stateAuthor: (state) => state.author,
  stateCreatedAuthorId: (state) => state.createdAuthorId,
  stateGraphs: (state) => state.graphs,
  stateUniqueYears: (state) => state.uniqueYears,
};

const actions = {
  async createAuthor({ commit, dispatch }, authorData) {
    try {
      const response = await axios.post("authors", authorData);
      const createdAuthor = response.data; // Получаем весь объект автора из ответа
      const createdAuthorId = createdAuthor.id; // Извлекаем ID из объекта автора
      commit("setCreatedAuthorId", createdAuthorId); // Сохраняем ID в состояние хранилища
      await dispatch("getAuthors");
      return createdAuthorId;
    } catch (error) {
      console.error("Failed to create author:", error);
      throw error;
    }
  },

  async getAuthors({ commit }) {
    try {
      let { data } = await axios.get("authors");
      commit("setAuthors", data);
    } catch (error) {
      console.error(error);
      throw error;
    }
  },

  async viewAuthor({ commit }, id) {
    try {
      let { data } = await axios.get(`author/${id}`);
      commit("setAuthor", data);
    } catch (error) {
      console.error("Failed to view author:", error);
      throw error;
    }
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteAuthor({}, id) {
    try {
      await axios.delete(`author/${id}`);
    } catch (error) {
      console.error(`Failed to delete author with ID ${id}:`, error);
      throw error;
    }
  },
  async searchAuthors({ commit }, query) {
    try {
      console.log(query);
      let { data } = await axios.get("authors/search", { params: { query } });
      commit("setAuthors", data);
    } catch (error) {
      console.error(`Failed to get authors with query ${query}:`, error);
      throw error;
    }
  },
  async viewGraphs({ commit }, id) {
    try {
      let { data } = await axios.get(`authors/graphs/${id}`);
      const imagePaths = data.map(path => axios.defaults.baseURL + 'static/' + path.replace(/\\/g, '/'));
      commit("setGraphs", imagePaths);
      const unique = [...new Set(data.map(path => path.split('_')[1].split('.')[0]))];
      const uniqueYears = unique.map((year, index) => ({ key: index, year }))
      commit("setUniqueYears", uniqueYears);
      console.log(uniqueYears)
    } catch (error) {
      console.error("Failed to view graphs:", error);
      throw error;
    }
  },
};

const mutations = {
  setAuthors(state, authors) {
    state.authors = authors;
  },
  setAuthor(state, author) {
    state.author = author;
  },
  setCreatedAuthorId(state, createdAuthorId) {
    state.createdAuthorId = createdAuthorId;
  },
  setGraphs(state, graphs) {
    state.graphs = graphs;
  },
  setUniqueYears(state, uniqueYears) {
    state.uniqueYears = uniqueYears;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
