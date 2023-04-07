# 코드 작성 - 게시판

- **1) 가상 환경**
    1. 가상 환경 등록
        
        1️⃣ 폴더 생성
        
        2️⃣ 가상환경 생성 : `python -m venv venv`
        
        3️⃣ 가상환경 활성화 : `source ./venv/Scripts/activate`
        
        4️⃣ 가상환경 장고 다운 : `pip install django==3.2.18`
        `pip install ipython` , `pip install django-extensions` , `pip install pillow`
        
        5️⃣ `pip freeze > requirements.txt`
        
    
    ---
    
    1. 초기 설정
        
        1️⃣ 프로젝트 생성 : `django-admin startproject config .`
        
        2️⃣ 서버 실행 : `python manage.py runserver`
        
        3️⃣ `.gitignore` 생성 : `.gitignore` , 템플릿 → [gitignore.io](http://gitignore.io)
        
        4️⃣ 어플 생성 : `python manage.py startapp appname`
        
        5️⃣ 어플 등록 : `settings.py` 파일 내 `INSTALLED_APPS` 리스트에 어플 이름 추가
        
    
    ---
    
    1. `settings.py`
        
        1️⃣ 어플 등록 : `INSTALLED_APPS` 리스트에 어플 이름 추가
        
        2️⃣ TEMPLATE : `TEMPLATES` 리스트 `'DIRS': [BASE_DIR / 'templates'],`
        
        3️⃣ STATIC : `STATIC_URL = '/static/'` , `STATICFILES_DIRS = [ BASE_DIR / 'static', ]`
        
    
    ---
    
- **2) 폴더, 파일 형성**
    1. 가장 바깥 폴더
        
        `templates/` - `base.html`
        
        `static/` - `css/`, `images/`
        
    
    ---
    
    1. app 내부
        
        `templates/articles/` - `index.html`, `detail.html`, `update.html`, `create.html`
        
        `urls.py`
        
        `forms.py`
        
    
    ---
    
    1. `templates/base.html`
        
        ```html
        {% load static %}
        
        <!DOCTYPE html>
        <head>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
          <link rel="stylesheet" href="{% static 'css/base.css' %}">
          <title>Articles</title>
        </head>
        <body>
          {% block content %}
          
          {% endblock content %}
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
        </body>
        </html>
        ```
        
    
    ---
    
- **3) model**
    1. `articles/models.py`
        
        ```python
        from django.db import models
        
        class Article(models.Model):
            title = models.CharField(max_length=30)
            content = models.TextField()
            image = models.ImageField(blank=True)
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
        
            def __str__(self):
                return f'{self.id}번째 글 - {self.title}'
        ```
        
    
    ---
    
    1. makemigrations, migrate
        
        1️⃣ `python manage.py makemigrations`
        
        2️⃣ `python manage.py migrate`
        
    
    ---
    
- **4) Form**
    1. `articles/forms.py`
        
        ```python
        from django import forms
        from .models import Article
        
        class ArticleForm(forms.ModelForm):
            class Meta:
                model = Article
                fields = '__all__'
        
            def clean_title(self):
                title = self.cleaned_data['title'] 
                if 'django' in title:
                    return True
                return False
        ```
        
    
    ---
    
- **5) url**
    1. `config/urls.py`
        
        ```python
        from django.contrib import admin
        from django.urls import path, include
        
        urlpatterns = [
            path('articles/', include('articles.urls')),
        ]
        ```
        
    
    ---
    
    1. `articles/urls.py`
        
        ```python
        from django.urls import path
        from . import views
        
        app_name = 'articles'
        urlpatterns = [
            path('', views.index, name='index'),
            path('<int:pk>/', views.detail, name='detail'),
            path('create/', views.create, name='create'),
            path('<int:pk>/update/', views.update, name='update'),
        ]
        ```
        
    
    ---
    
- **6) index**
    1. `articles/views.py`
        
        ```python
        from django.shortcuts import render, redirect
        from .models import Article
        
        def index(request):
            articles = Article.objects.all()
            context = {'articles':articles}
            return render(request, 'articles/index.html', context)
        ```
        
    
    ---
    
    1. `articles/index.html`
        
        ```html
        {% extends 'base.html' %}
        
        {% block content %}
          <h1>INDEX</h1>
          <a href="{% url 'articles:create' %}">CREATE</a>
          <hr>
        
          {% for article in articles %}
            <p>Number : {{article.id}}</p>
            <p>
              <a href="{% url 'articles:detail' article.pk %}">Title : {{article.title}}</a>
            </p>
            <p>Content : {{article.content}}</p>
            <hr>
          {% endfor %}
        {% endblock content %}
        ```
        
    
    ---
    
- **7) detail**
    1. `articles/views.py`
        
        ```python
        from django.shortcuts import render, redirect
        from .models import Article
        
        def detail(request, pk):
            article = Article.objects.get(pk=pk)
            context = {'article' : article}
            return render(request, 'articles/detail.html', context)
        ```
        
    
    ---
    
    1. `articles/detail.html`
        
        ```html
        {% extends 'base.html' %}
        
        {% block content %}
        <h1>DETAIL</h1>
        <hr>
        
        <p>Title : {{article.title}}</p>
        <p>Content : {{article.content}}</p>
        <p>Created : {{article.created_at}}</p>
        <p>Updated : {{article.updated_at}}</p>
        <hr>
        
        <a href="{% url 'articles:index' %}">Index</a>
        <a href="{% url 'articles:update' article.pk %}">Update</a>
        {% endblock content %}
        ```
        
    
    ---
    
- **8) create**
    1. `articles/views.py`
        
        ```python
        from django.shortcuts import render, redirect
        from .models import Article
        from .forms import ArticleForm
        
        def create(request):
            if request.method == 'POST':
                form = ArticleForm(request.POST, request.FILES)
                if form.is_valid():
                    article = form.save()
                    return redirect('articles:detail', article.pk)
        
            else:
                form = ArticleForm()
        
            context = {'form':form, }
            return render(request, 'articles/create.html', context)
        ```
        
    
    ---
    
    1. `articles/create.html`
        
        ```html
        {% extends 'base.html' %}
        
        {% block content %}
        <h1>Create</h1>
        <hr>
        
        <form action="{% url 'articles:create' %}" method="POST">
          {% csrf_token %}
          {{form.as_p}}
          <input type="submit">
        </form>
        
        {% endblock content %}
        ```
        
    
    ---
    
- **9) update**
    1. `articles/views.py`
        
        ```python
        from django.shortcuts import render, redirect
        from .models import Article
        from .forms import ArticleForm
        
        def update(request, pk):
            article = Article.objects.get(pk=pk)
            if request.method == 'POST':
                form = ArticleForm(request.POST, instance=article)
                if form.is_valid():
                    form.save()
                    return redirect('articles:detail', article.pk)
            else:
                form = ArticleForm(instance=article)
        
            context = {'form': form, 'article': article}
            return render(request, 'articles/update.html', context)
        ```
        
    
    ---
    
    1. `articles/update.html`
        
        ```html
        {% extends 'base.html' %}
        
        {% block content %}
          <h1>Update</h1>
          <hr>
        
          <form action="{% url 'articles:update' article.pk %}" method="POST">
            {% csrf_token %}
            {{form.as_p}}
            <input type="submit">
          </form>
        
          <hr>  
          <a href="{% url 'articles:detail' article.pk%}">Return to Detail</a>
        {% endblock content %}
        ```
        
    
    ---
    
- **10) image**
    1. `settings.py`
        
        ```python
        MEDIA_URL = '/media/'
        MEDIA_ROOT = BASE_DIR / 'media'
        ```
        
        가장 상위 폴더에 `media/` 생성
        
    
    ---
    
    1. `config/urls.py`
        
        ```
        from django.urls import path, include
        from django.conf import settings
        from django.conf.urls.static import static
        
        urlpatterns = [
            path('articles/', include('articles.urls')),
        
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
        
    
    ---
    
    1. `articles/views.py`
        
        ```python
        def create(request):
            if request.method == 'POST':
                form = ArticleForm(request.POST, request.FILES)
        ```
        
        ```python
        def update(request, pk):
            article = Article.objects.get(pk=pk)
            if request.method == 'POST':
                form = ArticleForm(request.POST, request.FILES, instance=article)
        ```
        
        `request.FILES` 추가
        
    
    ---
    
    1. `articles/create.html` , `articles/update.html`
        
        ```html
        {% extends 'base.html' %}
        
        {% block content %}
        <h1>Create</h1>
        <hr>
        
        <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
          {% csrf_token %}
          {{form.as_p}}
          <input type="submit">
        </form>
        
        {% endblock content %}
        ```
        
        `enctype` 추가
        
    
    ---
    
    1. `articles/detail.html`
        
        ```html
        {% extends 'base.html' %}
        
        {% block content %}
        <h1>DETAIL</h1>
        <hr>
        
        <p>Title : {{article.title}}</p>
        <p>Content : {{article.content}}</p>
        <p>Created : {{article.created_at}}</p>
        <p>Updated : {{article.updated_at}}</p>
        <img src="{{article.imagemodelname.url}}" alt="{{article.image}}"> 
        <hr>
        
        <a href="{% url 'articles:index' %}">Index</a>
        <a href="{% url 'articles:update' article.pk %}">Update</a>
        {% endblock content %}
        ```
        
        `img` 태그 추가
        
    
    ---
    
- **11) login&out**
    1. `accounts/models.py`
        
        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser
        
        class User(AbstractUser):
            pass
        ```
        
    
    ---
    
    1. `crud/settings.py`
        
        ```python
        AUTH_USER_MODEL = 'accounts.User'
        ```
        
    
    ---
    
    1. `accounts/admin.py`
        
        ```python
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from .models import User
        
        admin.site.register(User, UserAdmin)
        ```
        
    
    ---
    
    1. `accounts` 생성 및 등록
        
        ```python
        # crud/settings.py
        INSTALLED_APPS = [
            'articles',
            'accounts',
        			.
        			.
        			.
        ]
        ```
        
    
    ---
    
    1. url 분리 및 매핑
        
        ```python
        # crud/urls.py
        urlpatterns = [
            path('accounts/', include('accounts.urls')),
        ]
        ```
        
    
    ---
    
    1. `accounts/urls.py`
        
        ```python
        from django.urls import path
        from . import views
        
        app_name = 'accounts'
        urlpatterns = [
            path('login', views.login, name='login'),
            path('logout', views.logout, name='logout'),
        ]
        ```
        
    
    ---
    
    1. `accounts/views.py`
        
        ```python
        from django.shortcuts import render, redirect
        from django.contrib.auth.forms import AuthenticationForm
        from django.contrib.auth import login as auth_login
        from django.contrib.auth import logout as auth_logout
        
        def login(request):
            if request.user.is_authenticated: # 이미 로그인 한 유저라면
                return redirect('articles:index')
        
            if request.method == 'POST': # DB를 조작하는 요청이므로 POST
                # 로그인 처리
                form = AuthenticationForm(request, request.POST) # 유저가 입력한 데이터가 채워진 폼
                if form.is_valid():
                    auth_login(request, form.get_user()) # 유저 이름 가져옴 -> 로그인 처리
                    return redirect('articles:index')
            else:
                # 로그인 화면, 빈 폼 제공
                form = AuthenticationForm()
            
            context = {'form' : form, }
            return render(request, 'accounts/login.html', context)
        
        def logout(request):
            auth_logout(request) # 해당 세션 삭제
            return redirect('articles:index')
        ```
        
    
    ---
    
    1. `accounts/login.html`
        
        ```html
        {% extends 'base.html' %}
        
        {% block content %}
          <h1>Login</h1>
          <form action="{% url 'accounts:login' %}" method="POST">
            {% csrf_token %}
            {{form.as_p}}
            <input type="submit" value="로그인">
          </form>
        {% endblock content %}
        ```
        
    
    ---
    
    1. `superuser` 등록
        
        ```
        $ python manage.py createsuperuser
        Username: admin
        Email address: admin@admin.kr
        Password:
        ```
        
    
    ---
    
    1. `templates/base.html`
        
        ```html
        <body>
        	{% if user.is_authenticated %}
        	  <h3>Hello, {{ user }}</h3>
        	  <form action="{% url 'accounts:logout' %}" method="POST">
        	    {% csrf_token %}
        	    <input type="submit" value="Logout">
        	  </form>
        		<hr>
        		{% else %}
        	  <a href="{% url 'accounts:login' %}">Login</a>
        		<hr>
        	{% endif %}
        
          {% block content %}
          {% endblock content %}
        </body>
        ```
        
    
    ---
    
    1. `templates/base.html`
        
        로그인 한 유저, 안 한 유저가 보이는 창 구별
        
        ```html
        <body>
          {% if user.is_authenticated %}
            <p>Hello {{ user }}</p>
            <a href="{% url 'accounts:update' %}">USER UPDATE</a>
            <form action="{% url 'accounts:logout' %}" method="POST">
              {% csrf_token %}
              <input type="submit" value="LOGOUT">
            </form>
          {% else %}
            <a href="{% url 'accounts:login' %}">LOGIN</a>
            <a href="{% url 'accounts:signup' %}">SIGNUP</a>
          {% endif %}
          <hr>
          {% block content %}
            
          {% endblock content %}
        </body>
        ```
        
    
    ---
    
    1. `articles/index.html`
        
        로그인 한 유저만 생성 가능
        
        ```html
        {% if request.user.is_authenticated %}
            <a href="{% url 'articles:create' %}">create</a>
          {% else %}
            <a href="{% url 'accounts:login' %}">Login to create</a>
          {% endif %}
        ```
        
    
    ---
    
    1. 로그인 한 유저만 수정 가능
        1. `articles/views.py`
            
            ```python
            from django.contrib.auth.decorators import login_required
            
            @login_required
            def update(request, pk):
            ```
            
        2. `accounts/views.py`
            
            ```python
            def login(request):
                if request.method == 'POST':
            				    ...
                    return redirect(request.GET.get('next') or 'articles:index')
            ```
            
    
    ---
    
- **12) User CRUD**
    1. `accounts/models.py`
        
        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser
        
        class User(AbstractUser):
            pass
        ```
        
    
    ---
    
    1. `accounts/forms.py`
        
        ```python
        from django.contrib.auth.forms import UserCreationForm, UserChangeForm
        from django.contrib.auth import get_user_model
        
        class CustomUserCreationForm(UserCreationForm):
        
            class Meta(UserCreationForm.Meta): # Meta도 상속받기 때문에
                model = get_user_model() # settings - auth user model에서 가져옴, 현재 프로젝트에서 활성화된 User 모델을 리턴
        
        class CustomUserChangeForm(UserChangeForm):
        
            class Meta(UserChangeForm.Meta): # Meta도 상속받기 때문에
                model = get_user_model() # settings - auth user model에서 가져옴
        				fields = ('username', 'email', 'first_name', 'last_name', ) # 원하는 정보만 가져옴
        ```
        
    
    ---
    
    1. `accounts/admin.py`
        
        ```python
        from django.contrib import admin
        from django.contrib.auth.admin import UserAdmin
        from .models import User
        
        admin.site.register(User, UserAdmin)
        ```
        
    
    ---
    
    1. `accounts/urls.py`
        
        ```python
        from django.urls import path
        from . import views
        
        app_name = 'accounts'
        urlpatterns = [
        			...
            path('signup/', views.signup, name='signup'),
            path('delete/', views.delete, name='delete'),
            path('update/', views.update, name='update'),
            path('pw/', views.pw, name='pw'),
        ]
        ```
        
    
    ---
    
    1. `accounts/views.py`
        
        ```python
        from django.shortcuts import render, redirect
        from django.contrib.auth.forms import PasswordChangeForm
        from django.contrib.auth import login as auth_login
        from django.contrib.auth import logout as auth_logout
        from django.contrib.auth import update_session_auth_hash
        from .forms import CustomUserCreationForm, CustomUserChangeForm
        
        def signup(request):
            if request.method == 'POST':
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    auth_login(request, user)
                    return redirect('articles:index')
            else:
                form = CustomUserCreationForm()
        
            context={
                'form' : form,
            }
            return render(request, 'accounts/signup.html', context)
        
        def delete(request):
            request.user.delete()
            auth_logout(request)
            return redirect('articles:index')
        
        def update(request):
            if request.method == 'POST':
                form = CustomUserChangeForm(request.POST, instance=request.user)
                if form.is_valid():
                    form.save()
                    return redirect('articles:index')
            else:
                form = CustomUserChangeForm(instance=request.user)
            context={
                'form' : form
            }
            return render(request, 'accounts/update.html', context)
        
        def pw(request):
            if request.method == 'POST':
                form = PasswordChangeForm(request.user, request.POST)
                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user)
                    return redirect('articles:index')
            else:
                form = PasswordChangeForm(request.user)
            context = {
                'form' : form,
            }
            return render(request, 'accounts/pw.html', context)
        ```
        
    
    ---
    
    1. templates
        1. `accounts/signup.html`
            
            ```html
            {% extends 'base.html' %}
            
            {% block content %}
              <h1>SIGNUP</h1>
              <hr>
            
              <form action="{% url 'accounts:signup' %}" method="POST">
                {% csrf_token %}
                {{form.as_p}}
                <input type="submit" value="Signup">
              </form>
            {% endblock content %}
            ```
            
        2. `accounts/update.html`
            
            ```html
            {% extends 'base.html' %}
            
            {% block content %}
              <h1>UPDATE</h1>
              <hr>
              <form action="{% url 'accounts:update' %}" method="POST">
                {% csrf_token %}
                {{form.as_p}}
                <input type="submit" value="Update">
              </form>
              <hr>
              <form action="{% url 'accounts:delete' %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="DELETE">
              </form>
            {% endblock content %}
            ```
            
        3. `accounts/pw.html`
            
            ```
            {% extends 'base.html' %}
            
            {% block content %}
              <h1>Change Password</h1>
              <hr>
              <form action="{% url 'accounts:pw' %}" method="POST">
                {% csrf_token %}
                {{form.as_p}}
                <input type="submit" value="Change">
              </form>
            {% endblock content %}
            ```
            
    
    ---