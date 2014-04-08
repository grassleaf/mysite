#coding: utf-8
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response,redirect
from django.template import loader,RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from accounts.forms import RegisterForm
from gallery.forms import PhotoForm
from gallery.models import Item, Photo
from django.core.files.base import ContentFile
from cms.models import Category, Story

def index(request):
	username = request.session.get('username', None)
	if username:
		return render_to_response('index.html', {'username': username})
	else:
		username = request.POST.get('username', None)
	if username:
		request.session['username'] = username
		return render_to_response('index.html', {'username': username})
	else:
		return render_to_response('index.html')
	return render_to_response('index.html')

def register(request):
	'''注册视图'''
	template_var = {}
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST.copy())
		if form.is_valid():
			username = form.cleaned_data["username"]
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			user = User.objects.create_user(username,email,password)
			user.save()
			_login(request,username,password)#注册完毕 直接登陆
			return HttpResponseRedirect("")
	template_var["form"] = form
	return render_to_response("accounts/register.html",template_var,\
						context_instance = RequestContext(request))
	# if request.method == 'POST':
	# 	form = UserCreationForm(request.POST) # 系统注册表单
	# 	if form.is_valid():
	# 		new_user = form.save()
	# 		return HttpResponseRedirect("/")
	# else:
	# 	form = UserCreationForm()
	# return render_to_response("account/register.html", {
	# 	'form': form,
	# })
	# return render_to_response('account/register.html')

def _login(request,username,password):
	'''登陆核心方法'''
	ret = False
	user = authenticate(username=username,password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			ret = True
		else:
			messages.add_message(request, messages.INFO, _(u'用户没有激活'))
	else:
		messages.add_message(request, messages.INFO, _(u'用户不存在'))
	return ret

@csrf_exempt
def login(request):
	return render_to_response("accounts/login.html")

@csrf_exempt
def login_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			auth_login(request, user)
			request.session['username'] = user.username
			print request.user
			# return render_to_response("index.html", {'user': user}, context_instance=RequestContext(request))
			return redirect("/", {'username': username})
			# c = RequestContext(request, {'user': user})
		else:
			print '没有这个用户'
	else:
		return HttpResponseRedirect("/login/")
	# user = auth.authenticate(username=username, password=password)
	# if user is not None and user.is_active:
	# 	# Correct password, and the user is marked "active"
	# 	auth.login(request, user)
	# 	# Redirect to a success page.
	# 	return HttpResponseRedirect("/")
	# else:
	# 	# Show an error page
	# 	return HttpResponseRedirect("/login_view/")

@csrf_exempt
def logout(request):
	auth_logout(request)
	request.session['username'] = None
	return HttpResponseRedirect("/")

@csrf_exempt
def add_photo(request):
	if request.method == 'POST':
		# 往数据表中添加一行记录，并保存文件
		form = PhotoForm(request.POST,request.FILES)
		if form.is_valid():
			#往数据表中添加一行记录
			item_id = request.POST['item'] #获取item的id值
			title = request.POST['title']
			caption = request.POST['caption']
			slug = request.POST['slug']
			image = 'photos/%s' % request.FILES['image']
			photo = Photo(item_id=item_id, title=title, image=image, caption=caption, slug=slug)
			photo.save()
			# 保存文件到本地计算机
			obj = Photo.objects.get(id=item_id)
			file_content = ContentFile(request.FILES['image'].read())
			obj.image.save(request.FILES['image'].name, file_content)
		return HttpResponseRedirect('/gallery/items/')
	else:
		return render_to_response('add_photo.html')

@csrf_exempt
def add_item(request):
	if request.method == 'POST':
		slug = request.POST['slug']
		item = Item(name=request.POST['name'], description=request.POST['description'], \
			slug=slug) #输入中文会报错
		item.save();
		return HttpResponseRedirect("/gallery/items/")
	else:
		return render_to_response('add_item.html')

@csrf_exempt
def add_category(request):
	if request.method == 'POST':
		label = request.POST['label']
		slug = request.POST['slug']
		category = Category(label=label, slug=slug)
		category.save()
		return HttpResponseRedirect("/cms/")
	else:
		return render_to_response('add_category.html')

@csrf_exempt
def add_story(request):
	if request.method == 'POST':
		print request.POST
		title = request.POST['title']
		slug = request.POST['slug']
		category_id = request.POST['category']
		markdown_content = request.POST['markdown_content']
		owner = request.POST['owner']
		story = Story(title=title, slug=slug, category_id=category_id,\
		markdown_content=markdown_content, owner_id=owner,status=3) #使用外键Category,可以用category_id标识,owner也一样.
		story.save()
		return HttpResponseRedirect('/cms/%s' % slug)
	else:
		return render_to_response('add_story.html')