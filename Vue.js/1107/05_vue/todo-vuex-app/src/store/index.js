import Vue from 'vue'
import Vuex from 'vuex'
import createPersisterdState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersisterdState(),
  ],
  state: {
    todos:[ 
    ],
  },//state 값을 변화해서 새값으로 
  getters: {
    allTodosCount(state){
      return state.todos.length
    },
    completedTodosCount(state){
      //1완료된 거만 모든 새로운 배열 만들고
      const completedTodos = state.todos.filter((todo) =>{
        return todo.isCompleted === true
      })
      //2길이 세고
      return completedTodos.length
    },
    unCompletedTodosCount(state,getters){
      return getters.allTodosCount - getters.completedTodosCount
    }
    },//state 값을 변경하는 
  mutations: {
    CREATE_TODO(state, todoItem){
      state.todos.push(todoItem)
    },
    DELETE_TODO(state,todoItem){
      console.log(state)
      console.log(state.todos)
      const index = state.todos.indexOf(todoItem) // 인덱스 번호찾아줌
      state.todos.splice(index,1)
    },
    UPDATE_TODO_STATUS(state,todoItem){
      // console.log(todoItem)
      //todos 배열에서 선택된 todo의 is_completed값만 토글한후
      // 업데이트 된 todos배열로 되어야 함
      state.todos= state.todos.map((todo) => {
        if (todo === todoItem){
          todo.isCompleted = !todo.isCompleted
        }
        return todo 
      })
    },
    LOAD_TODOS(state){
      const localStorageTodos= localStorage.getItem('todos')
      const parsedTodos = JSON.parse(localStorageTodos)
      state.todos=parsedTodos
    }
  },
  actions: {
    createTodo(context, todoTitle){
      const todoItem = {
        title: todoTitle,
        isCompleted: false,

      }
      // console.log(todoItem)
      // (뮤테이션함수, 본인이 만든객체 전달)
      context.commit('CREATE_TODO',todoItem)
      context.dispatch('saveTodosToLocalStorage')  
      
    },
    deleteTodo(context,todoItem){
      context.commit('DELETE_TODO',todoItem)
      context.dispatch('saveTodosToLocalStorage')  
      
    },
    updateTodoStatus(context,todoItem){
      context.commit('UPDATE_TODO_STATUS', todoItem)
      context.dispatch('saveTodosToLocalStorage')  
    },
    saveTodosToLocalStorage(context){
      const jsonTodos = JSON.stringify(context.state.todos)
      // localStorage.setItem(키,값) 키는 별로 의미없음
      localStorage.setItem('todos',jsonTodos)

    },
    loadTodos(context){
      context.commit('LOAD_TODOS')
    }
  },

  modules: {
  }
})
