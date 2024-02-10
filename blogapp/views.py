from http.client import HTTPResponse
from django.shortcuts import render,redirect

from .models import Post
from blogapp.forms import CommentForm, ContactForm
# from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse

# from contact.forms import ContactForm


# Create your views here.
def frontpage(request):
    posts = Post.objects.all()
    contact = ContactForm(request.POST)
    if contact.is_valid():
        # フォームからデータを取得
        name = contact.cleaned_data.get('name')
        email = contact.cleaned_data.get('email')
        message = contact.cleaned_data.get('message')

        # お問い合わせメールの送信処理（例として、自分自身にメールを送る設定）
        subject = f"お問い合わせ from {name}"
        message = f"{message}"
        from_email = email
        # "poaro.doil.poaro@gmail.com"  # 送信元のメールアドレス
        recipient_list = ["poaro.doil.poaro@gmail.com"]  # 受信者のメールアドレスリスト

        msg = EmailMessage(
            subject=subject, body=message, from_email=from_email, to=recipient_list
        )
        
        msg.send()
        contact.save()
        contact = ContactForm()
        return render(request, 'blogapp/frontpage.html', {"posts": posts, "contact": contact} )
    
    else:
        contact = ContactForm()
    return render(request, "blogapp/frontpage.html", {"posts": posts, "contact": contact} )

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    # slug から番号を抽出 (例: "post-01" から "01" を抽出)
    slug_number = slug.split('-')[-1]

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('post_detail', kwargs={'slug': post.slug}))
    else:
        form = CommentForm()

    # テンプレート名を動的に生成
    template_name = f"blogapp/post-{slug_number}.html"

    return render(request, template_name, {"post": post, "form": form})

