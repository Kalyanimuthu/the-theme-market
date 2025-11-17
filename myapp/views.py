from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import HeroSection, Category, FeaturedTheme, ShowcaseCategory, WhyChooseUs, UI, Core, TeamMember, FAQ, ContactCard, Theme, Cart, CartItem
from .utils import get_or_create_cart

def theme(request):

    # Sort dropdown values
    sort_options = [
        "Best Sellers",
        "Most Popular",
        "Newest First",
        "Price Low → High",
        "Price High → Low",
    ]

    # Filters with radio options
    filters = {
    "Category": ["Business", "Portfolio", "Blog", "E-Commerce", "Landing Page"],
    "Price": ["500-1000", "1500-1800", "2000-2250", "2250-3225"],
    "Rating": ["5 Stars", "4+ Stars", "3+ Stars"],
    "Features": ["Responsive Design", "One Page", "Dark Mode", "Page Builder", "WooCommerce"],
    "Compatibility": ["WordPress 6.0+", "WordPress 5.8+", "Gutenberg", "Classic Editor"]
}


    # FULL themes list
    themes = FeaturedTheme.objects.all()

    testimonials = [
        {"name": "Sarah Johnson", "role": "Web Developer"},
        {"name": "Michael Chen", "role": "Agency Owner"},
        {"name": "Emily Rodriguez", "role": "Freelance Designer"},
    ]

    return render(
        request,
        "myapp/theme.html",
        {
            "filter_items": filters,
            "themes": themes,
            "sort_options": sort_options,
            "testimonials": testimonials,
        },
    )
def home(request):
    
    hero = HeroSection.objects.first()    
    categories = Category.objects.all()
    featured = FeaturedTheme.objects.all()[:6]
    showcase = ShowcaseCategory.objects.all()
    week_items = FeaturedTheme.objects.filter(display="WEEK")[:3]
    month_items = FeaturedTheme.objects.filter(display="MONTH")[:3]
    
    # COLLECTION FILTERS
    trending_items = FeaturedTheme.objects.filter(collection="trending")[:6]
    new_items = FeaturedTheme.objects.filter(collection="new")[:6]
    bestseller_items = FeaturedTheme.objects.filter(collection="bestseller")[:6]

    # THEME CATEGORIES
    business_themes = FeaturedTheme.objects.filter(category="business")[:6]
    portfolio_themes = FeaturedTheme.objects.filter(category="portfolio")[:6]
    blog_themes = FeaturedTheme.objects.filter(category="blog")[:6]
    ecommerce_themes = FeaturedTheme.objects.filter(category="ecommerce")[:6]

    # TEMPLATE CATEGORIES
    html_templates = FeaturedTheme.objects.filter(template_type="html")[:6]
    landing_templates = FeaturedTheme.objects.filter(template_type="landing")[:6]
    ui_kits = FeaturedTheme.objects.filter(template_type="ui")[:6]
    why_items = WhyChooseUs.objects.all()

    context = {
        "hero": hero,
        "categories":categories,
        "featured": featured,
        "showcase": showcase,
        "week_items": week_items,
        "month_items": month_items,
        # COLLECTION FILTERS
        "trending_items": trending_items,
        "new_items": new_items,
        "bestseller_items": bestseller_items,

        # THEME CATEGORIES
        "business_themes": business_themes,
        "portfolio_themes": portfolio_themes,
        "blog_themes": blog_themes,
        "ecommerce_themes": ecommerce_themes,

        # TEMPLATE TYPES
        "html_templates": html_templates,
        "landing_templates": landing_templates,
        "ui_kits": ui_kits,

        "why_items": why_items,
    }
    return render(request, "myapp/home.html", context)

def templates(request):
    ui_kits = FeaturedTheme.objects.filter(template_type="ui")[:3]
    weekly_bestsellers = FeaturedTheme.objects.filter(display="week", collection="bestseller")[:6]
    bestseller_items = FeaturedTheme.objects.filter(collection="bestseller")[:3]
    context = {
        "ui_kits": ui_kits,
        "weekly_bestsellers": weekly_bestsellers,
        "bestseller_items": bestseller_items,
    }
    return render(request, 'myapp/templates.html', context)

def about(request):
    ui = UI.objects.all()
    core = Core.objects.all()
    team = TeamMember.objects.all()
    context = {
        "ui": ui,
        "core": core,
        "team": team,
    }
    return render(request, 'myapp/about.html', context)

def contact(request):
    fqs = FAQ.objects.all()
    cards = ContactCard.objects.all()
    context ={
        "faqs": fqs,
        "cards": cards,
    }
    return render(request, "myapp/contact.html", context)

# Add item to cart
def add_to_cart_ajax(request, theme_id):
    cart = get_or_create_cart(request)
    theme = get_object_or_404(FeaturedTheme, id=theme_id)

    item, created = CartItem.objects.get_or_create(cart=cart, theme=theme)
    if not created:
        item.quantity += 1
    item.save()

    return JsonResponse({"success": True})

# View Cart
def cart(request):
    cart = get_or_create_cart(request)
    Cart.objects.filter(session_key__isnull=True).delete()

    cart_items = cart.items.all()
    total_price = sum(item.total for item in cart_items)

    return render(request, "myapp/cart.html", {
        "cart": cart,
        "cart_items": cart_items,
        "total_price": total_price,
    })



# Update quantity +/-
def update_cart(request, item_id, action):
    item = get_object_or_404(CartItem, id=item_id)

    if action == "plus":
        item.quantity += 1

    elif action == "minus":
        item.quantity -= 1
        if item.quantity < 1:
            item.delete()
            return redirect("cart")

    item.save()
    return redirect("cart")


# Remove item
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect("cart")


# Empty cart
def empty_cart(request):
    cart = get_or_create_cart(request)
    cart.delete()
    return redirect("cart")

def clear_cart_ajax(request):
    cart = get_or_create_cart(request)
    cart.delete()
    return JsonResponse({"success": True})


# Checkout placeholder
def checkout(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()

    subtotal = sum(item.total for item in cart_items)

    # convert float to Decimal
    discount = Decimal("6.00") if subtotal > 100 else Decimal("0.00")
    handling_fee = Decimal("0.00")

    total = subtotal - discount + handling_fee

    return render(request, "myapp/checkout.html", {
        "cart": cart,
        "cart_items": cart_items,
        "subtotal": subtotal,
        "discount": discount,
        "handling_fee": handling_fee,
        "total": total,
    })