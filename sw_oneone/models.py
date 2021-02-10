from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

    def __repr__(self):
        # 主キーとnameを表示させて見やすくする
        # ex) 1: Alice
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__  # __str__にも同じ関数を適用


class Question(models.Model):
    question = models.CharField(max_length=128)
    aChoice = models.CharField(max_length=128)
    dChoice1 = models.CharField(max_length=128)
    dChoice2 = models.CharField(max_length=128)
    dChoice3 = models.CharField(max_length=128)
    dChoice4 = models.CharField(max_length=128)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)

    
    is_past_question = models.BooleanField(default=False)
    number_of_times = models.IntegerField(default=0, blank=True, null=True)
    field = models.IntegerField(default=0, blank=True, null=True)
    number_of_question = models.IntegerField(default=0, blank=True, null=True)