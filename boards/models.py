from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Board(models.Model):
    """Our project is a discussion board (a forum).

    The whole idea is to maintain several boards,
    which will behave like categories.
    """

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        """The String represention.

        Should display the Boards name
        """
        return self.name


class Topic(models.Model):
    """Inside a specific board,user can start a new discussion by creating topic"""

    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')

    def __str__(self):
        """Should display the Topic Subject"""
        return self.subject


class Post(models.Model):
    """Users can engage in the discussion posting replies."""

    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        """Should display the Post Message"""
        return self.message
