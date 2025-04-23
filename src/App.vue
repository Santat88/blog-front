<template>
  <div>
    <header class="app-header">
      <h1>Блог Ганичев А. 2-МГВ-2</h1>
    </header>
    <main class="app-main">
      <PostList :posts="posts" />
    </main>
    <footer class="app-footer">
      <p>&copy; 2025 Блог Ганичев А. 2-МГВ-2. Все права защищены.</p>
    </footer>
  </div>
</template>

<script>
import PostList from './components/PostList.vue'
import axios from 'axios';

export default {
  name: 'App',
  components: {
    PostList
  },
  data() {
    return {
      posts: []
    }
  },
  created() {
    this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      try {
        const response = await axios.get('http://localhost:8088/api/v1/posts');
        this.posts = response.data;
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
    }
  }
}
</script>

<style>
/* Add some basic styling */
.app-header {
  background-color: #4CAF50;
  color: white;
  text-align: center;
  padding: 1rem;
}

.app-main {
  padding: 2rem;
}

.app-footer {
  background-color: #f1f1f1;
  text-align: center;
  padding: 1rem;
  margin-top: 2rem;
  border-top: 1px solid #ccc;
}
</style>