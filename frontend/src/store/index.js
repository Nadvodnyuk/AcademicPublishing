import { createStore } from "vuex";

import works from './modules/works';
import users from './modules/users';
import authors from './modules/authors';
import authors_works from './modules/authors_works';

export default createStore({
  modules: {
    works,
    users,
    authors,
    authors_works,
  }
});
