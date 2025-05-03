import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    userId: localStorage.getItem('user_id') || null,
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    login(token, userId) {
      this.token = token;
      this.userId = userId;
      localStorage.setItem('token', token);
      localStorage.setItem('user_id', userId);
    },
    logout() {
      this.token = null;
      this.userId = null;
      localStorage.removeItem('token');
      localStorage.removeItem('user_id');
    },
  },
});