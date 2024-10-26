from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100,null=False)
    roll_number=models.IntegerField(null=False)
    class_name=models.CharField(max_length=2,null=False)
    student_id=models.CharField(max_length=10,null=False)

    def __str__(self):
        return self.student_id

class Books(models.Model):
    name=models.CharField(max_length=100,null=False)
    author_name=models.CharField(max_length=100,null=False)
    book_id=models.CharField(max_length=10,null=False)

    def __str__(self):
        return self.book_id

class Library(models.Model):
    student=models.ForeignKey(Students,on_delete=models.CASCADE)
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    issue_date=models.DateField(null=False)
    renewal_date=models.DateField(null=True)
    fine=models.IntegerField(default=0)

    def __str__(self):
        return self.student.name+'-'+self.book.name