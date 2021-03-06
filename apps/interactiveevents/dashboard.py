from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from adhocracy4.dashboard import DashboardComponent
from adhocracy4.dashboard import ModuleFormSetComponent
from adhocracy4.dashboard import components

from . import forms
from . import views


class LiveStreamComponent(DashboardComponent):
    identifier = 'live_stream'
    weight = 20
    label = _('Live Stream')

    def is_effective(self, module):
        module_app = module.phases[0].content().app
        return module_app == 'a4_candy_interactive_events'

    def get_progress(self, module):
        return 0, 0

    def get_base_url(self, module):
        return reverse('a4dashboard:interactiveevents-livestream', kwargs={
            'organisation_slug': module.project.organisation.slug,
            'module_slug': module.slug,
        })

    def get_urls(self):
        return [(
            r'^modules/(?P<module_slug>[-\w_]+)/livestream/$',
            views.LiveStreamDashboardView.as_view(component=self),
            'interactiveevents-livestream'
        )]


class ModuleAffiliationsComponent(ModuleFormSetComponent):
    identifier = 'affiliations'
    weight = 13
    label = _('Affiliations')

    form_title = _('Edit affiliations')
    form_class = forms.AffiliationFormSet
    form_template_name = \
        'a4_candy_interactive_events/includes/module_affiliations_form.html'

    def is_effective(self, module):
        module_app = module.phases[0].content().app
        return module_app == 'a4_candy_interactive_events'


components.register_module(LiveStreamComponent())
components.register_module(ModuleAffiliationsComponent())
