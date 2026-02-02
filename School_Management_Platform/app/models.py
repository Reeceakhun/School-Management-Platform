"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Student(models.Model):

    last_name = models.CharField(max_length=30, help_text="Enter your last name"),
    first_name = models.CharField(max_length=30),
    middle_name = models.CharField(max_length=30, null=True),
    email_address = models.EmailField(),
    enrollment_date = models.DateTimeField("Enrollment Date")

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Course(models.Model):
    """ Create the Couse model. Add data to the database table"""
    course_id = models.AutoField(primary_key=True),
    title = models.CharField(max_length=50),
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.title} with {self.credits}"



class Enrollment(models.Model):

    enrollment_id = models.AutoField(primary_key=True),
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='Enrollment'),

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='Enrollment'

        )
    grade = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.student} in {self.course}"


