# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from publication.models import Speaker, Subject

@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            data = {}
            data['name'] = request.POST['name']
            data['email'] = request.POST['email']
            data['phone'] = request.POST['phone']
            data['topic'] = request.POST['topic']
            data['message'] = request.POST['message']
            # 首先先判斷此用戶是否有投稿過
            if Speaker.objects.filter(email=data['email']).count() > 0:
                return HttpResponse('您已投稿過!')
            else:
                speaker = Speaker.objects.create(name=data['name'], email=data['email'], phone=data['phone'])
                Subject.objects.create(topic=data['topic'], message=data['message'], uid=speaker.id)
                return HttpResponse('投稿成功請靜候通知')
        except Exception, ex:
            return HttpResponse('投稿出現問題!')
    return render_to_response('index.html')
