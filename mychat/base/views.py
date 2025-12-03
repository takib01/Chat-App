from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time 


def getToken(request):
    appId = '4851850cf0b144318c00d18116cfc150'
    appCertificate  =  '094ef700c05d4bf5af5bef590b8e6371'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 255)
    expirationTimeInSeconds = 3600*24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid }, safe=False)
def lobby(request):
    return render(request, 'base/lobby.html')
def room(request):
    return render(request, 'base/room.html')