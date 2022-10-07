# 💡PJT05_DB를 활용한 웹 페이지 구현

------

### BootStrap5 적용 방법

1. BootStrap5 설치

   ```bash
   $ pip install django-bootstrap-v5==1.0.11
   ```

2. [settings.py](http://settings.py) - INSTALLED_APPS 에 bootstrap5 app 추가

   ```python
   # settings.py
   
   INSTALLED_APPS = [
       'movies',
       'bootstrap5',
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   ```

### BootStrap5 활용하여 form에 bootstrap 적용하기

1. [views.py](http://views.py) 에서 .html 로, context에 form 가져오기

   ```python
   def create(request):
       if request.method == 'POST':
           form = MovieForm(request.POST)
           if form.is_valid():
               movie = form.save()
               return redirect('movies:detail', movie.pk)
       else:
           form = MovieForm()
       context = {
           'form': form,
       }
       return render(request, 'movies/create.html', context)
   ```

2. .html 파일에서 파일 상단에 bootstrap5 load 한 후, bootstrap_form으로 form 출력

   ```html
   {% extend 'base.html' %}
   {% load bootstrap5 %}
   
   ...
   
   {% bootstrap_form form %}
   ```

### ModelForm의 표시 형태

```python
from django import forms
from .models import Movie

# 장르
Genre_1 = '코미디'
Genre_2 = '공포'
Genre_3 = '로맨스'
Genre_4 = '액션'
Genre_5 = 'SF'
Genre_choice = [
    (Genre_1, '코미디'),
    (Genre_2, '공포'),
    (Genre_3, '로맨스'),
    (Genre_4, '액션'),
    (Genre_5, 'SF'),
]
# 스코어
Score_choice = [
    ('0', 0),
    ('0.5', 0.5),
    ('1.0', 1),
    ('1.5', 1.5),
    ('2.0', 2),
    ('2.5', 2.5),
    ('3.0', 3),
    ('3.5', 3.5),
    ('4.0', 4),
    ('4.5', 4.5),
    ('5.0', 5),
]

class MovieForm(forms.ModelForm):
    genre = forms.ChoiceField(choices=Genre_choice)
    score = forms.ChoiceField(choices=Score_choice)
    release_date = forms.DateField(widget = forms.SelectDateWidget, input_formats=["%Y-%m-%d"])
    class Meta:
        model = Movie
        fields = '__all__'
```

1. 장르 / 스코어 선택하여 입력 받기 → `forms.ChoiceField`
2. 개봉일 날짜 선택하여 입력 받기 → `forms.DateField(widget = forms.SelectDateWidget)`