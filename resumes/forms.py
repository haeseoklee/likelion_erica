from .models import Resume
from django import forms

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('document',)

    def clean(self):
        FILE_TYPE_ONLY = ['pdf']
        try:
            document = self.cleaned_data['document']
            if document:
                file_type = str(document).split('.')[1]
                if not file_type in FILE_TYPE_ONLY:
                    raise forms.ValidationError("pdf 파일만 가능합니다.")
                if document.name == '':
                    raise forms.ValidationError("잘못된 파일 이름입니다.")
            return self.cleaned_data
        except:
            raise forms.ValidationError("선택된 파일이 없습니다.")
