from django.contrib import admin
from django import forms
from django.utils.html import format_html, mark_safe
from .models import HeroSection, Category, FeaturedTheme, ShowcaseCategory, WhyChooseUs, UI, Core, TeamMember, FAQ, ContactCard

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "item_count", "preview_icon")

    def preview_icon(self, obj):
        return format_html('<i class="{}" style="font-size:24px;"></i>', obj.icon)

    preview_icon.short_description = "Icon"

@admin.register(FeaturedTheme)
class FeaturedThemeAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "rating", "sales")
    
class ShowcaseCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "item_count", "image_preview")
    search_fields = ("title", "description")

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" style="border-radius:6px;">')
        return "-"
    
    image_preview.short_description = "Preview"

admin.site.register(ShowcaseCategory, ShowcaseCategoryAdmin)
# ------------------
# Why choose us ADMIN
# ------------------
class WhyChooseUsForm(forms.ModelForm):
    class Meta:
        model = WhyChooseUs
        fields = "__all__"
        widgets = {
            "bg_color": forms.TextInput(attrs={"type": "color"}),
            "text_color": forms.TextInput(attrs={"type": "color"}),
        }


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    form = WhyChooseUsForm
    list_display = ("title", "bg_color", "text_color")

# ------------------
# UI ADMIN
# ------------------

class UIForm(forms.ModelForm):
    class Meta:
        model = UI
        fields = "__all__"
        widgets = {
            "bg_color": forms.TextInput(attrs={"type": "color"}),
            "text_color": forms.TextInput(attrs={"type": "color"}),
        }


@admin.register(UI)
class UIAdmin(admin.ModelAdmin):
    form = UIForm
    list_display = ("title", "bg_color", "text_color")


# ------------------
# CORE ADMIN
# ------------------

class CoreForm(forms.ModelForm):
    class Meta:
        model = Core
        fields = "__all__"
        widgets = {
            "bg_color": forms.TextInput(attrs={"type": "color"}),
            "text_color": forms.TextInput(attrs={"type": "color"}),
        }


@admin.register(Core)
class CoreAdmin(admin.ModelAdmin):
    form = CoreForm
    list_display = ("title", "bg_color", "text_color")


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = "__all__"
        widgets = {
            "bg_color": forms.TextInput(attrs={"type": "color"}),
            "text_color": forms.TextInput(attrs={"type": "color"}),
        }

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberForm
    list_display = ("name", "designation", "order")
    list_editable = ("order",)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order")
    list_editable = ("order",)

@admin.register(ContactCard)
class ContactCardAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
