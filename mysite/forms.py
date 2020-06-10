import logging
from django import forms
from .models import Contents

logger = logging.getLogger(__name__)

class ContentsForm(forms.ModelForm):
    """コンテンツ用のフォーム"""
    message = forms.CharField(
        label='メッセージ',
        widget=forms.Textarea
    )
    
    class Meta:
        model = Contents
        fields = ('message',)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 3:
            raise forms.ValidationError('%(min_length)s 文字以上で入力してください', params={'min_length': 3})
        return message
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs['class'] = 'form-control col-9'
        self.fields['message'].widget.attrs['placeholder'] = 'ここにメッセージを入力してください'
        