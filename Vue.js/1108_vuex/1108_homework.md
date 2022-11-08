# HomeWork

### Vuex
다음은 Vuex로 구성된 하나의 숫자를 counting하는 store이다.
(a), (b), (c)에 들어갈 코드를 작성하시오.
- NUMBER_INCREMENT mutation handler가 호출되면 state의 count를 1만큼 증가시킨다.

```javascript
export default new __(a)__({
  state: {
    count: 0,
  },
  mutations: {
    NUMBER_INCREMENT: function (state) {
      __(b)__
    }
  },
  actions: {
    numberIncrement: function (context) {
      __(c)__
    }
  }
})
```

a) Vue.Store		b)`context.commit('NUMBER_NVREMENT')`		 c) state.count+=1





### AJAX with vuex

아래 예시의 함수는 서버로부터 데이터를 가져 온 뒤, 응답 값을 state에 저장하기 위하여 mutations를 호출하는 로직을 수행한다.
이와 같이 비동기 API 및 mutations 호출에 적합한 store의 속성 (a)를 작성하시오.

```javascript
__(a)__: {
  fetchTodoList: function({ commit }) {
    const requestUrl = 'http://localhost:8000/api/v1/todos/'

    axios.get(resuqestUrl)
    .then((response) => {
      // API 요청 성공 처리
      commit('TODO_LIST_SUCCESS', response)
    })
    .catch((error) => {
      // API 요청 실패 처리
      commit('TODO_LIST_FAILURE', error)
    })
  }
}
```

a) actions



### Vuex mutations

store에 정의한 state를 직접 변경하지 않고, mutations를 통해 변경해야 하는 이유를 Vuex 공식문서를 참고하여 작성하시오.

- mutations를 통해 변경하는 이유는 state 변화를 추척하기 위해서 입니다. state 변화를 추척할 수 있기 때문에 디버깅이 편해집니다.