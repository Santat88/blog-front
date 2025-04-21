<template>
  <div class="comment">
    <p><strong>{{ comment.author }} </strong> <br> {{ comment.content }}</p>
  </div>
</template>

<script>
    export default {
        name: 'PostComment',
        props: {
            comment: {
                type: Object,
                required: true
            }
        }
    }
</script>