# HomeWork
### CSS flex-direction
Flex box의 주축을 변경하는 flex-direction의 4가지 값과 각각의 특징을 작성하시오.
- 'row' : 메인축을 가로로 설정 (기본값)
- 'column' : 메인축을 세로로 설정

- 'row-reverse' : 메인축을 가로로 설정하되 오른쪽에서 왼쪽으로 설정
- 'column-reverse' : 메인축을 세로로 설정하되 아래에서 위로 설정


### Bootstrap flex-direction
flex-direction의 4가지 요소와 대응하는 bootstrap 클래스를 작성하시오.
- 왼쪽 : CSS 속성, 오른쪽 : bootstrap
- 'row' : class = 'flex-row'
- 'column' : 'flex-column'

- 'row-reverse' : 'flex-row-reverse'
- 'column-reverse' : 'flex-colunm-reverse'



### align-items
align-items 속성의 4가지 값과 각각의 특징을 작성하시오.
- 'flex-start' : 교차축 방향의 시작선에 정렬
- 'flex-end' : 교차축 방향의 끝선에 정렬
- 'center' : 공간의 가운데 정렬
- 'stretch' : felx 컨테이너의 최대 높이로 설정



### flex-flow
flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것을 고르시오.
```
(1) flex-direction, flex-wrap
```


```html
<div class=" (a) ">
  <div class=" (b) ">
    <div class="col- (c) - (d) "></div>
  </div>
</div>
```

### Bootstrap Grid System
상단 코드에 Bootstrap Grid System을 적용시키고자한다.
(a), (b) 각각에 입력해야 할 클래스 이름을 작성하시오.
- A : `container`
- B : `row`

### Breakpoint prefix (5번 문제 연계)
Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단 코드와 같은 형태로 클래스 이름을 지정해야 한다.
1) (c) 에 들어갈 수 있는 값들과 그 값들이 가지는 의미를 작성하시오.
- `sm`, `md`, `lg`, `xl`, `xxl`
2) (d) 에 들어갈 수 있는 값들과 그 값들이 가지는 의미를 작성하시오.
- 12 이하의 정수 : row 클래스가 부여된 부모의 컨테이너를 12개의 공간으로 분리하여 분배 할 수 있는 숫자를 의미