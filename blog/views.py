from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

def blog_index(request):
    # query set containing all the posts from the database
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    #  In this case, we only want posts whose categories contain the category 
    # with the name corresponding to that given in the argument of the view function. Again, you’re using order_by() to order posts starting with the most recent.
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    # here we get the posts having a specific primary key 
    post = Post.objects.get(pk=pk)
    
    # here we create a new instance of the CommentForm class
    form = CommentForm()
    # suppose that we have posted the form then we retrieve the data
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # suppose that the form has non empty entries
        if form.is_valid():
            # then you create a new model instance 
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    
    # now you retrieve the new list of comments after having saved
    # the previous list of comments 
    comments = Comment.objects.filter(post=post)
    # you create a new context using the variables you have previously
    # just defined 
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    # then you can reder the html page using the given context which is
    # used as far as I see ot pass variables to the view
    return render(request, "post_detail.html", context)