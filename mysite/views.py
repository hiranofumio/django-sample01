import requests
import logging
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import ContentsForm
from .models import Contents

logger = logging.getLogger(__name__)

class ContentsView(generic.FormView):
    template_name = "pages/contents.html"
    form_class = ContentsForm
    success_url = reverse_lazy('contents')
    
    def get_context_data(self):
        context = super().get_context_data()
        # 現在のメッセージ
        context['contents'] = Contents.objects.order_by('-id')
        # 現在のインスタンスID(ALB検証用)
        context['instance_id'] = requests.get('http://169.254.169.254/latest/meta-data/instance-id').text
        return context
    
    def form_valid(self, form):
        message = form.save(commit=False)
        message.save()
        logger.info('Data saved')
        return super().form_valid(form)
        
