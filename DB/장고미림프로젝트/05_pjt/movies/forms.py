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

class DateInput(forms.DateInput):
    input_type: 'date'

class MovieForm(forms.ModelForm):
    genre = forms.ChoiceField(choices=Genre_choice)
    score = forms.ChoiceField(choices=Score_choice)
    release_date = forms.DateField(widget = forms.SelectDateWidget, input_formats=["%Y-%m-%d"])
    class Meta:
        model = Movie
        fields = '__all__'

