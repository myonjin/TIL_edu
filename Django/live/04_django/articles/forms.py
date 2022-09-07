from cProfile import label
from django import forms

from articles.models import Article
from .models import Article

# class ArticleForm(forms.Form):
#     NATION_A = 'kr'   # 서버가 받는 키값
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATIONS_CHOICES=[
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)
class ArticleForm(forms.ModelForm): 
    title = forms.CharField( #위젯을 쓰려면 홈필드 안에서
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'Enter the title',
                'maxlength': 10,
            }
        ),

    )
    content = forms.CharField(   #core arguments
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder' : 'Enter the content',
                'rows':5,
                'cols' : 50,

            }
        ),
        error_messages={
            'required':'Please enter your content'
        }
    )

    class Meta:
        model = Article #어떤 모델을 기반으로 할지
        fields = '__all__' #어떤 모델필드 중 어떤것을 출력할지
