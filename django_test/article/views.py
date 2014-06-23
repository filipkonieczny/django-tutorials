from django.shortcuts import render_to_response
from article.models import Article


def articles(request):
	return render_to_response('article/articles.html',
							 {'articles': Article.objects.all()})


def article(request, article_id=1):
	return render_to_response('article/article.html',
							 {'article': Article.objects.get(id=article_id)})






from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView


# Create your views here.
def hello(request):
	name = "filip"
	html = "<html><body>Hi, my name is %s!</body></html>" % name
	
	return HttpResponse(html)


def hello_template(request):
	name = "filip"
	surname = "konieczny"

	t = get_template('article/hello.html')
	html = t.render(Context({'name': name, 'surname': surname}))

	return HttpResponse(html)


# same as hello_template, but simplier
def hello_template_simple(request):
	name = 'filip'
	surname = 'konieczny'
	return render_to_response('article/hello.html', {'name': name, 'surname': surname})


class HelloTemplate(TemplateView):
	template_name = 'article/hello_class.html'

	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = 'filip'
		context['surname'] = 'konieczny'
		return context