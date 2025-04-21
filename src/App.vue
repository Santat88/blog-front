<template>
  <div>
    <PostList :posts="posts" />
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
      posts: [
      ]
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