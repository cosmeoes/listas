from django.shortcuts import render,redirect
from pytube import YouTube
from django.http import StreamingHttpResponse, HttpResponse
import requests, mimetypes, json, urllib, re

from .models import Download

def human_readable(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


# Create your views here.
def index(request):
    return render(request, 'youtube/index.html')

def list_formats(request):
    response = {}
    if request.method == 'POST':
        url = request.POST['url']
        try:
            m = re.match('^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$', url)
            if not m:
                raise Exception

            yt = YouTube(url)
            title = yt.title
            streams_list = []
            for stream in yt.streams.filter(progressive=True).all():
                st = stream.__dict__
                st['filesize'] = stream.filesize
                st['url'] = "download/{}/{}/{}/{}".format(stream.mime_type.replace("/","_"), stream.filesize, urllib.parse.quote_plus(title),urllib.parse.quote_plus(stream.url))
                streams_list.append(st)
            response['title'] = title
            response['streams'] = streams_list
        except Exception as e:
            response['error'] = 'Invalid video url'

    return HttpResponse(json.dumps(response), content_type='application/json')




def download(request, mime, filesize, title, url):
    mime = mime.replace('_', '/')
    print(mime, url)
    r = requests.get(url, stream=True)
    response = StreamingHttpResponse(
        (chunk for chunk in r.iter_content(512 * 1024)),
        content_type=mime)

    title = urllib.parse.unquote_plus(title)
    disposition = "attachment; filename={}{}".format(title.replace(' ', '_'),mimetypes.guess_extension(mime))
    response['Content-Disposition'] = disposition
    response['Content-Length'] = filesize
    model, created = Download.objects.get_or_create(url=url, title=title, mime=mime, filesize=filesize )
    if not created:
        model.num_downloads += 1

    model.save()
    return response
