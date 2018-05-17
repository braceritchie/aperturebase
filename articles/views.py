from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
# Create your views here.
def article_list(request):
    article = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_list.html',{'article':article})

def article_detail(request,slug):
    art1 = Articles.objects.get(slug=slug)
    body = art1.body
    
    di = ['img0','img1','img2','img3','img4','img5','img6','img7','img8','img9']

    
    for i in di:

        a = body.find('!! '+i+" !!")
        #exec('art1.'+body[a+3:a+8]+'.url')
        if(a!=-1):
            b = getattr(art1,i).url
            c =  getattr(art1, i+'cap')
            if(body[a+12:a+15]=="por"):

                

                body = body[:a] + "</p><div class='text-center ' style='margin-left:50px;margin-right:50px;margin-top:1em;margin-bottom:1em;'><img src=" + "'" +b+"'"+" class='img-fluid sizer-por' style='margin: 5 auto;'/><div class='text-center cap'><br><i>"+c+"</i></div></div><p>"+body[a+15:len(body)]
            else:

                body = body[:a] + "</p><div class='text-center ' style='margin-left:50px;margin-right:50px;margin-top:1em;margin-bottom:1em;'><img src=" + "'" +b+"'"+" class='img-fluid sizer ' style='margin: 5 auto;'/><div class='text-center cap'><br><i>"+c+"</i></div></div><p>"+body[a+10:len(body)] 
        else:
            pass
    return render(request, 'articles/article_detail.html',{'art1':art1,'final':body})