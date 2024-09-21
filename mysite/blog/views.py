from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from blog.models import Post,Category,Comment,Tag,Contact
# from .forms import CommentForm
from django.shortcuts import reverse
# from .forms import ContactForm
from django.http import JsonResponse
from .models import Contact  
from django.views.decorators.csrf import csrf_exempt





def home(request):
    posts = Post.objects.all()
    print(posts, "posts>>>>>>>>>>>>>..")
    return render(request, 'home.html', context={'posts':posts})


def about(request):
    return render(request,'about.html')

# def index(request):
#     posts = Post.objects.all()
#     print(posts, "posts>>>>>>>>>>>>>..")
#     return render(request, 'index.html', {'posts': posts})


# def blog(request):
#     return render(request, "blog/blog.html", {'blogs': blogs})

def blog(request):
    slug = request.GET.get('slug')
    if slug:
        posts = Post.objects.filter(tags__slug=slug)
    else:
        posts = Post.objects.all()
    # comments = Comment.objects.filter()
    # posts = posts.object.filter(tags=tags)
    return render(request, 'blog.html', {'posts': posts})

def blog_details(request, slug):
    # def blog_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print(Comment.objects.filter(post=post))
    parent_id = request.POST.get('commentid', None)
    
    if request.method == "POST":
        parent_id = request.POST.get('commentid', None)
        print(parent_id, "parent id>>>>>>>>>>>>>>>>>>>>>")

        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        message = request.POST.get('message', None)
        print(name,email,message, "rpkxdsfdsfdfdfd")

        if parent_id:
            parent_comment = Comment.objects.filter(id=int(parent_id)).first()
            Comment.objects.create(name=name, email=email, message=message, post=post, parent=parent_comment)
        else:
            Comment.objects.create(name=name, email=email, message=message, post=post)

        return redirect(reverse('blog_details', kwargs={'slug': slug}))

   
    tags = Tag.objects.all()
    category = Category.objects.all()[:3]
    post = Post.objects.filter(slug=slug).first()
    print(post, "post>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    latest_posts = Post.objects.order_by('-created_at')[:3]
    comments = Comment.objects.filter(post=post, parent__isnull=True)
    print(comments, "dssdsdfsdfdsfdsfdsfdsfds")
    all_reply = Comment.objects.filter(id=parent_id)
    print(all_reply, "all")
    return render(request, 'blog_details.html', {'post':post,'latest_posts': latest_posts, 'category':category, 'comments':comments,'tags':tags,})


def blog_view(request):
    return render(request, 'blog.html')  # Make sure this template exists

def tag_detail(request, slug):
    posts = Post.objects.filter(tags__slug=slug)
    tagDetail = get_object_or_404(Tag, slug=slug)
    return render(request, 'tag.html', {'posts': posts, 'tagDetail':tagDetail})

def category_detail(request, slug):
    categoryDetail = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category = categoryDetail)
    return render(request, 'category.html', {'posts': posts, 'categoryDetail':categoryDetail})

# def contact(request):
#     error_message = None
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         # Check if all required fields are filled
#         if name and email and phone and subject and message:
#             # Create and save the contact instance
#             Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
#             return render(request, 'contact.html', {'success': True})
    
#         else:
#             error_message = "Please fill in all required fields."
#     return render(request, 'contact.html', {'error_message': error_message})




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        
        return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
    
    # return JsonResponse({'success': False, 'message': 'Invalid request method.'})
    return render(request, 'contact.html', {'error_message': 'error_message'})