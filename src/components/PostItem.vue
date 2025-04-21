<template>
    <div class="post-item">
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
        <h3>Comments:</h3>
        <comment
            v-for="comment in post.comments"
            :key="comment.id"
            :comment="comment"
        ></comment>
    </div>
</template>

<script>
import Comment from './PostComment.vue';
export default {
    name: 'PostItem',
    components: {
        Comment
    },
    props: {
        post: {
            type: Object,
            required: true
        }
    }
};
</script>

<style scoped>
.post-item {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px 0;
}
.post-item h2 {
    margin: 0 0 10px;
}
.post-item h3 {
    margin: 10px 0 5px;
}
.post-item p {
    margin: 5px 0;
}
.post-item .comment {
    margin-left: 20px;
}
.post-item .comment p {
    margin: 0;
}
</style>