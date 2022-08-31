from pathlib import Path

from django import template, forms
from django.templatetags.static import static

from firstproject.settings import BASE_URL

register = template.Library()

# Menu Constants
MENU_TYPES = {
    1: ['dashboard'],
}


@register.simple_tag()
def get_file_name(val):
    return Path(val).name


# Use this tag to set variable value in templates
@register.simple_tag()
def set_value(val):
    return val


# Use this tag to select menu for current url
@register.simple_tag()
def get_menu_selected_class(current_url, menu_type):
    if current_url in MENU_TYPES.get(menu_type):
        return 'active'
    return ''


# @register.simple_tag()
# def get_secondary_lang():
#     return get_secondary_languages()


@register.simple_tag()
def get_dynamic_form_field(form: forms.Form, code: str, val: str):
    name = '{0}_{1}'.format(code, val)
    return form.fields.get(name).get_bound_field(form, name)


@register.simple_tag()
def get_dynamic_form_field_error(form: forms.Form, code: str, val: str):
    name = '{0}_{1}'.format(code, val)
    return form.fields.get(name).get_bound_field(form, name).errors


@register.simple_tag()
def get_image_or_placeholder(image):
    if image:
        if Path(image.path).exists():
            return image.url
    return static("firstproject/images/dummy-img.jpeg")


@register.filter(name='get_required_label')
def get_required_label(field):
    if field.field.required:
        return '<span class="required_fields">*</span>'
    return ''


@register.simple_tag()
def get_cms_url(val):
    return '{0}{1}'.format(BASE_URL, val)


@register.simple_tag()
def get_image_for_email(image):
    image_url = "firstproject/images/{0}".format(image)
    return '{0}'.format(BASE_URL) + static(image_url)


@register.simple_tag()
def get_permission_list(user, code):
    if user.is_superuser:
        return True
    if user.user_staff_profile.role.permissions.filter(code=code):
        return True
    return False