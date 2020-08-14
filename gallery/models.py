from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length =50)

    @classmethod
    def tag_articles(cls):
        tags = cls.objects.all()
        return tags

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =50,null=True,blank=True#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
)


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'uploads/')
    description = models.TextField()
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,name, description , image_location, image_category):
        update = cls.objects.filter(id = id).update(name = name, description = description ,image_location = image_location,image_category = image_category)
        # return update

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def search_by_category(cls,image_category):
        images = Image.objects.filter(image_category__name__icontains=image_category)
        return images

    @classmethod
    def filter_by_location(cls, image_location):
        images_location = cls.objects.filter(image_location__id=image_location)
        return images_location

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']