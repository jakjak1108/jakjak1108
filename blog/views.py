from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Hello, django!")

def html_response(request):
    html = \
    """
<html>
    <head>
    </head>
    <body>
        <h1>Hello, django!</h1>
        <p>HTML 문서를 응답으로 보내줍니다.</p>
    </body>
</html>
    """
    return HttpResponse(html)