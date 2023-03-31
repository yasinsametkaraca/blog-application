from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.user.is_authenticated:  # Eğer kullanıcı giriş yapmışsa home sayfasına yönlendiriyoruz.
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)  # authenticate fonksiyonu ile kullanıcı adı ve şifre doğrulaması yapıyoruz. Eğer doğruysa kullanıcı bilgilerini döndürüyor.
        if user is not None:
            login(request, user)  # login fonksiyonu ile kullanıcıyı sisteme giriş yaptırmış oluyoruz ve tarayıcıya session bilgileri (cookie) oluşturuluyor. Bu sayede kullanıcı giriş yaptıktan sonra her sayfaya girdiğinde otomatik olarak giriş yapmış oluyor.
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "Username or password is incorrect."
            })  # Eğer kullanıcı adı veya şifre yanlışsa hata mesajı gösteriyoruz ve login sayfasında kalıyor.
    return render(request, "account/login.html")


def register_view(request):
    if request.user.is_authenticated:  # Eğer kullanıcı giriş yapmışsa home sayfasına yönlendiriyoruz.
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        if password == repassword:
            if User.objects.filter(username=username).exists(): # Kullanıcı adı daha önce alınmışsa hata mesajı gösteriyoruz ve register sayfasında kalıyor.
                return render(request, "account/register.html", {
                    "error": "Username already exists.",
                    "email": email,     # firstname vesaireyi hatalı durumda tekrar girili olsun diye yolladık.
                    "firstname": firstname,
                    "lastname": lastname
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {  # Eğer email daha önce alınmışsa hata mesajı gösteriyoruz ve register sayfasında kalıyor.
                        "error": "Email already exists.",
                        "username": username,
                        "firstname": firstname,
                        "lastname": lastname
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)  # Kullanıcıyı oluşturuyoruz.
                    user.save()  # Kullanıcıyı kaydediyoruz.
                    return redirect("login")
        else:
            return render(request, "account/register.html", {  # Eğer şifreler eşleşmiyorsa hata mesajı gösteriyoruz ve register sayfasında kalıyor.
                "error": "Passwords do not match.",
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname
            })
    return render(request, "account/register.html")


def logout_view(request):
    logout(request)  # logout fonksiyonu ile kullanıcıyı sistemden çıkış yaptırıyoruz.
    return redirect("login")
