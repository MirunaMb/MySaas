<template>
    <div>
      <h1>Hello, Saas</h1>
  
      <v-form @submit.prevent="addTask">
        <v-text-field
          v-model="newTask"
          label="Introduceți un nou task"
          append-icon="mdi-plus"
          @click:append="addTask"
        ></v-text-field>
      </v-form>
  
      <v-list>
        <v-list-item v-for="(task, index) in tasks" :key="task.id || index">
          {{ task.task }}
        </v-list-item>
      </v-list>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Home',
    data() {
      return {
        newTask: '',
        tasks: []
      };
    },
    methods: {
      async fetchTasks() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/tasks');
          this.tasks = response.data;
        } catch (error) {
          console.error('Error fetching tasks:', error);
        }
      },
      async addTask() {
        if (this.newTask.trim() === '') return;
        try {
          await axios.post('http://127.0.0.1:8000/tasks', { task: this.newTask });
          this.newTask = '';
          this.fetchTasks();
        } catch (error) {
          console.error('Error adding task:', error);
        }
      }
    },
    mounted() {
      this.fetchTasks();
    }
  };
  </script>
  
  <style scoped>
  .home-container {
    background-color: white;
    height: 100vh;
    padding: 20px;
  }
  
  h1 {
    color: black;
    font-size: 24px;
    text-align: center;
  }
  
  input {
    margin-bottom: 10px;
    padding: 5px;
    width: calc(100% - 22px);
  }
  
  button {
    margin-left: 10px;
    padding: 5px 10px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    display: flex;
    justify-content: space-between;
    padding: 5px 0;
  }
  </style>