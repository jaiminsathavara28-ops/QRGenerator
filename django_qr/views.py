from django.shortcuts import render
import qrcode
from . forms import QRCodeForm
import os
from django.conf import settings

def gen_qr(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            com_name = form.cleaned_data['company_name']
            url = form.cleaned_data['url']

    #QR code
            qr= qrcode.make(url)
            print(qr)
            file_name = com_name.replace(" ", "_").lower() + '_url.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            #img url
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            

            context={
                'com_name' : com_name,
                'qr_url' :qr_url,
                'file_name' : file_name
            }
            return render(request, 'qr_result.html',context)

    else:
        form = QRCodeForm()
        context={
            'form':form
        }
        return render(request,'gen_qr.html',context)