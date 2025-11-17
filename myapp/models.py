from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class HeroSection(models.Model):
    # Text Fields
    title = models.CharField(max_length=200)
    highlight_text = models.CharField(max_length=100)
    subtitle = models.TextField()
    badge_text = models.CharField(max_length=200, blank=True, null=True)
    search_placeholder = models.CharField(max_length=200, default="Search templates...")

    # Images
    image1 = models.ImageField(upload_to="hero/")
    image2 = models.ImageField(upload_to="hero/")
    image3 = models.ImageField(upload_to="hero/")
    image4 = models.ImageField(upload_to="hero/")

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Homepage Hero Section"

ICON_CHOICES = [
    ("fa-solid fa-code", "Code"),
    ("fa-solid fa-cart-shopping", "Ecommerce"),
    ("fa-solid fa-blog", "Blog"),
    ("fa-solid fa-briefcase", "Business"),
    ("fa-solid fa-camera", "Camera"),
    ("fa-solid fa-bullhorn", "Marketing"),
    ("fa-solid fa-mobile-screen-button", "Mobile"),
    ("fa-solid fa-stopwatch", "Technology"),
    ("fa-solid fa-store", "Shop"),
]
class Category(models.Model):
    title = models.CharField(max_length=100)
    item_count = models.PositiveIntegerField(default=0)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    icon_bg = models.CharField(max_length=20, default="#4F46E5")  # hex color

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class FeaturedTheme(models.Model):
    
    COLLECTION_CHOICES = [
        ("trending", "Trending Collection"),
        ("new", "New Arrivals"),
        ("bestseller", "Bestseller"),
    ]

    CATEGORY_CHOICES = [
        ("business", "Business Theme"),
        ("portfolio", "Portfolio Theme"),
        ("blog", "Blog Theme"),
        ("ecommerce", "E-Commerce Theme"),
    ]

    TEMPLATE_CHOICES = [
        ("html", "HTML Templates"),
        ("landing", "Landing Page Templates"),
        ("ui", "UI Kits"),
    ]

    DISPLAY_CHOICES = (
        ("week", "This Week"),
        ("month", "This Month"),
    )

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sales = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)  # 1–5 stars
    image = models.ImageField(upload_to="featured_themes/")
    preview_url = models.URLField()

    display = models.CharField(max_length=20, choices=DISPLAY_CHOICES, blank=True, null=True, help_text="Where should this theme appear?")
    collection = models.CharField(max_length=20, choices=COLLECTION_CHOICES, null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True, blank=True)
    template_type = models.CharField(max_length=20, choices=TEMPLATE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title


class ShowcaseCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="showcase/")
    item_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class WhyChooseUs(models.Model):
    ICON_CHOICES = [
        ("shield", "Quality Guaranteed"),
        ("download", "Instant Downloads"),
        ("headset", "24/7 Support"),
        ("refresh", "Regular Updates"),
        ("award", "Elite Authors"),
        ("dollar", "Great Value"),
    ]

    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        help_text="Select icon for this feature"
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    order = models.PositiveIntegerField(default=0)
    bg_color = models.CharField(
        max_length=20,
        default="#DFFFE3",
        help_text="Pick background color"
    )

    text_color = models.CharField(
        max_length=20,
        default="#84CC16",
        help_text="Pick text color"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]

class UI(models.Model):
    ICON_CHOICES = [
    ("users", "Active Users"),
    ("chart-line", "Downloads"),
    ("award", "Products"),
    ("globe", "Countries"),
]


    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        help_text="Select icon for this feature"
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    bg_color = models.CharField(
        max_length=20,
        default="#DFFFE3",
        help_text="Pick background color"
    )

    text_color = models.CharField(
        max_length=20,
        default="#84CC16",
        help_text="Pick text color"
    )
    def __str__(self):
        return self.title

class Core(models.Model):
    ICON_CHOICES = [
    ("bullseye", "Our Mission"),
    ("eye", "Our Vision"),
    ("gears", "Our Impact"),
]



    icon = models.CharField(
        max_length=50,
        choices=ICON_CHOICES,
        help_text="Select icon for this feature"
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    bg_color = models.CharField(
        max_length=20,
        default="#D8E9FF",
        help_text="Pick background color"
    )

    text_color = models.CharField(
        max_length=20,
        default="#13157c",
        help_text="Pick text color"
    )

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="team/")
    bg_color = models.CharField(
        max_length=20,
        default="#0A3574",   # your navy-blue footer background
        help_text="Background color under the image"
    )
    text_color = models.CharField(
        max_length=20,
        default="#FFFFFF",   # white text
        help_text="Name/Designation text color"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.question

class ContactCard(models.Model):
    ICON_CHOICES = [
        ("envelope", "Email Icon"),
        ("phone", "Phone Icon"),
        ("comment", "Live Chat Icon"),
    ]

    icon = models.CharField(max_length=20, choices=ICON_CHOICES)
    title = models.CharField(max_length=100)
    line1 = models.CharField(max_length=200, blank=True, null=True)
    line2 = models.CharField(max_length=200, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
class Theme(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="themes/")

    def __str__(self):
        return self.title


class Cart(models.Model):
    session_key = models.CharField(max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def items(self):
        return self.cartitem_set.all()

    @property
    def total_price(self):
        return sum(item.total for item in self.items)

    def __str__(self):
        return f"Cart {self.session_key}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    theme = models.ForeignKey(FeaturedTheme, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return self.theme.price * self.quantity

    def __str__(self):
        return f"{self.theme.title} (x{self.quantity})"
