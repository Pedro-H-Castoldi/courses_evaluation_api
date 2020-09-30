from django.db import models

class Base(models.Model):

    creation = models.DateTimeField('criation', auto_now_add=True)
    update = models.DateTimeField('update', auto_now=True)
    active = models.BooleanField('active?', default=True)

    class Meta:
        abstract= True

class Course(Base):

    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

class Evaluation(Base):

    course = models.ForeignKey(Course, related_name='evaluation', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    commentary = models.TextField(blank=True, default='')
    grade = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'
        unique_together = ['course', 'email']

    def __str__(self):
        return f'{self.name} rated the course {self.course} with the grade {self.grade}'
