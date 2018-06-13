from __future__ import absolute_import, unicode_literals

from collections import OrderedDict

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.views.debug import get_safe_settings
import os
from debug_toolbar.panels import Panel


class TicTacToePanel(Panel):
    """
    A panel to display all variables in django.conf.settings
    """
    template = 'debug_toolbar/panels/tictactoe.html'

    nav_title = _("TicTacToe")

    def title(self):
        return _("TicTacToe")

    def generate_stats(self, request, response):
        my_sysinfo = dict()
        import psutil

        processes = [proc for proc in psutil.process_iter()]
        processes.sort(key=lambda proc:proc.memory_info()[0])
        for proc in processes:
            my_sysinfo[proc.name()] = proc.pid

        self.record_stats({
            'settings': OrderedDict(my_sysinfo.items()),
        })