import axios from "axios";

const state = {
  works: null,
  work: null,
  createdWorkId: null,
};

const getters = {
  stateWorks: (state) => state.works,
  stateWork: (state) => state.work,
  stateCreatedWorkId: (state) => state.createdWorkId,
};

const actions = {
  async createWork({ commit, dispatch }, workData) {
    try {
      const response = await axios.post("works", workData);
      const createdWork = response.data; // Получаем весь объект работы из ответа
      const createdWorkId = createdWork.id; // Извлекаем ID из объекта работы
      commit("setCreatedWorkId", createdWorkId); // Сохраняем ID в состояние хранилища
      await dispatch("getWorks");
      return createdWorkId;
    } catch (error) {
      console.error("Failed to create work:", error);
      throw error;
    }
  },

  async getWorks({ commit }) {
    try {
      let { data } = await axios.get("works");
      commit("setWorks", data);
    } catch (error) {
      console.error(error);
      throw error;
    }
  },

  async viewWork({ commit }, id) {
    try {
      let { data } = await axios.get(`work/${id}`);
      commit("setWork", data);
    } catch (error) {
      console.error("Failed to view work:", error);
      throw error;
    }
  },
  // eslint-disable-next-line no-empty-pattern
  async updateWork({}, work ) {
    try {
      await axios.patch(`work/${state.work.id}`, work.form);
    } catch (error) {
      console.error(`Failed to update work with ID ${work.id}:`, error);
      throw error;
    }
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteWork({}, id) {
    try {
      await axios.delete(`work/${id}`);
    } catch (error) {
      console.error(`Failed to delete work with ID ${id}:`, error);
      throw error;
    }
  },

  async searchWorks({ commit }, {query, start_year, end_year, field_value}) {
    try {
      console.log(query, start_year, end_year, field_value);
      let { data } = await axios.get("works/search", {
        params: { query, start_year, end_year, field_value }
      });
      commit("setWorks", data);
    } catch (error) {
      console.error(`Failed to get works with query ${query}:`, error);
      throw error;
    }
  },
};

const mutations = {
  setWorks(state, works) {
    state.works = works;
  },
  setWork(state, work) {
    state.work = work;
  },
  setCreatedWorkId(state, createdWorkId) {
    state.createdWorkId = createdWorkId;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
