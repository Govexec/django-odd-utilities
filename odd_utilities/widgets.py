from django.forms.widgets import Select
from django.forms.util import flatatt
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from django.utils.safestring import mark_safe


class IconSelect(Select):
    class Media:
        js = ("admin/odd_utilities/js/icon_select.js",)
        css = {
            "all": ("admin/odd_utilities/css/icon_select.css",)
        }

    def __init__(self, attrs=None, choices=(), related_images=()):
        super(IconSelect, self).__init__(attrs, choices)

        self.related_images = related_images

    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select class="icon-select"%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append(u'</select>')
        output.append(u'<div class="icon-select-image-display"></div>')
        return mark_safe(u'\n'.join(output))

    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_unicode(option_value)
        if option_value in selected_choices:
            selected_html = u' selected="selected"'
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''

        # Add related image path to option's data
        related_image = self.related_images.get(option_value, None)
        if not related_image:
            if option_value == "":
                related_image = self.related_images.get("empty", None)
            else:
                related_image = self.related_images.get("default", None)

        if related_image:
            related_image_html = ' data-related-image="%s"' % related_image
        else:
            related_image_html = ''

        return u'<option value="%s"%s%s>%s</option>' % (
            escape(option_value), selected_html, related_image_html,
            conditional_escape(force_unicode(option_label)))

    def render_options(self, choices, selected_choices):
        return super(IconSelect, self).render_options(choices, selected_choices)