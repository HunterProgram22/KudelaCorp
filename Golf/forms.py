from django import forms

from .models import Round, Course

class RoundForm(forms.ModelForm):

    class Meta:
        model = Round
        fields = ('course', 'date', 'holesplayed', 'strokes', 'putts',
                  'fairways_hit', 'gir', 'equistrokes')


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('course', 'rating', 'slope', 'par')
