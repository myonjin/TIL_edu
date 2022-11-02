<template>
  <div>
    <li>
      {{todo.title}}
      <button @click="deleteTodo">XX</button>
    </li>
  </div>
</template>

<script>

export default {
  name : 'TodoListItem',
  props: {
    todo : Object,
  },
  methods:{
    deleteTodo: function () {
      this.$emit('delete-todo', this.todo)
    }
  }
}
</script>

<style>

</style>