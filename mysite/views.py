#coding: utf-8
from django.shortcuts import render_to_response

# def index(request):
# 	username = request.session.get('username', None)
# 	if username:
# 		return render_to_response('index.html', {'username': username})
# 	else:
# 		username = request.POST.get('username', None)
# 	if username:
# 		request.session['username'] = username
# 		return render_to_response('index.html', {'username': username})
# 	else:
# 		return render_to_response('index.html')
