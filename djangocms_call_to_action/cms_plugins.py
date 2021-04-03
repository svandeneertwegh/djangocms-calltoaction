from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from . import models


class CallToActionPlugin(CMSPluginBase):
    model = models.CallToAction
    name = 'Call to action'
    admin_preview = True
    render_template = 'djangocms_call_to_action/plugins/calltoaction.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CallToActionPlugin)
