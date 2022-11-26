from django.db import models

# Create your models here.


# Meals models here.
class Newsletter(models.Model):
    Email=models.EmailField(max_length=100)
    Acknowledge=models.BooleanField(default=False)
    
    def __str__(self):
        return self.Email

# Meals models here.
class Meals(models.Model):
    Meal_Name=models.CharField(max_length=255, choices=(('Breakfast', 'Breakfast'),('Lunch', 'Lunch'),('Dinner', 'Dinner')))
    Description=models.TextField()
    Image=models.FileField(upload_to='Images', default="Images/default.jpg")
    
    def __str__(self):
        return self.Meal_Name


# Category models here.
class Category(models.Model):
    Meal_Name=models.ForeignKey(Meals, on_delete=models.CASCADE)
    Category_Name=models.CharField(max_length=255, choices=(('Drinks', 'Drinks'),('Food', 'Food'),('Sandwich', 'Sandwich'),('Snacks', 'Snacks')))
    Description=models.TextField()
    Image=models.FileField(upload_to='Images', default="Images/default.jpg")

    def __str__(self):
        return self.Category_Name


# All Items models here.
class AllItems(models.Model):
    Meal_Name=models.ForeignKey(Meals, on_delete=models.CASCADE)
    Category_Name=models.ForeignKey(Category, on_delete=models.CASCADE)
    Name=models.CharField(max_length=255)
    Price=models.CharField(max_length=255)
    Description=models.TextField()
    Image=models.FileField(upload_to='Images', default="Images/default.jpg")

    def __str__(self):
        return self.Name


# Reservation models here.
class Reservation(models.Model):
    Name=models.CharField(max_length=255)
    Number=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Date=models.DateField()
    Meal_Name=models.ForeignKey(Meals, on_delete=models.CASCADE)
    NumberofPeople=models.CharField(max_length=255, choices=(('Below 10People','Below 10People'), ('10 People','10 People'),('20 People','20 People'), ('50 People','50 People'), ('100 People','100 People'), ('Above 100People','Above 100People')))
    Description=models.TextField()
    
    def __str__(self):
        return self.Name


# Order models here. 
class Order(models.Model):
    Name=models.CharField(max_length=255)
    Number=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Date=models.DateField()
    DeliveringAddress=models.TextField()
    Meal_Name=models.ForeignKey(Meals, on_delete=models.CASCADE)
    Plates=models.IntegerField()
    Description=models.TextField()
    
    def __str__(self):
        return self.Name

# Contact models here.
class Contact(models.Model):
    Name=models.CharField(max_length=255)
    Number=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Subject=models.CharField(max_length=255)
    Message=models.TextField()
    
    def __str__(self):
        return self.Name
