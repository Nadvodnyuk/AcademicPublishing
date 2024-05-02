import axios from "axios";

const state = {
  works: null,
  work: null,
  createdWorkId: null,
  pdf:null
};

const getters = {
  stateWorks: (state) => state.works,
  stateWork: (state) => state.work,
  stateCreatedWorkId: (state) => state.createdWorkId,
  statePdf: (state) => state.pdf,
};

const actions = {
  async createWork({ commit, dispatch }, workData) {
    try {
      const response = await axios.post("works", workData);
      const createdWork = response.data;
      const createdWorkId = createdWork.id;
      commit("setCreatedWorkId", createdWorkId);
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
  async getPDF({ commit }, id) {
    try {
      let { data } = await axios.get(`pdf/${id}`, { responseType: 'blob' });
      let blob = new Blob([data], { type: 'application/pdf' });
      let url = window.URL.createObjectURL(blob);
      commit("setPdf", url);
    } catch (error) {
      console.error("Failed to get PFD:", error);
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
  setPdf(state, pdf) {
    state.pdf = pdf;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
