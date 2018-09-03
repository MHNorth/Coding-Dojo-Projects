from django.db import models

##---------- Amadon Model ----------##
class ProductCategory(models.Model):
    """
    Model representing the product categories 
    listed as a dropdown menu

    """
    class Meta:
        verbose_name_plural = "Categories"


    amadon_categories = (
        ('Beauty and Spa', 'Beauty and Spa'),
        ('Soundtrack Music', 'Soundtrack Music'),
        ('Women\'s Clothing', 'Women\'s Clothing'),
        )

    categoryList = models.CharField(
        max_length=100,
        choices = amadon_categories,
        default = "Beauty and Spa",
        )
    
    def __str__(self):
        return self.categoryList
    

class Product(models.Model):
    """
    Model representing product category, 
    name, description and price
    """
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE, 
        )
    productName = models.CharField(max_length = 100)
    description = models.TextField(max_length = 300, blank=True, null = True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return "{} | {} | {} | {}...".format(self.category, self.productName, self.price, self.description[:25])

