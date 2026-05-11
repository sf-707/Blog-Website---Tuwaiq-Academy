from django.db import models

class User(models.Model):
    UserName = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.UserName
class Category(models.Model):
    Name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.Name

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Date = models.DateField()

    def __str__(self):
        return self.Title

class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Content = models.TextField()
    Date = models.DateField()

    def __str__(self):
        return f"Comment by {self.User.UserName} on {self.Post.Title}"


