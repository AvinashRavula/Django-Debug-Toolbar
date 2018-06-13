from __future__ import absolute_import, unicode_literals

from collections import OrderedDict

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.views.debug import get_safe_settings
import os
from debug_toolbar.panels import Panel


class SysInfoPanel(Panel):
    """
    A panel to display all variables in django.conf.settings
    """
    template = 'debug_toolbar/panels/sysinfo.html'

    nav_title = _("SysInfo")

    def title(self):
        return _("SysInfo")

    def generate_stats(self, request, response):
        my_sysinfo = dict()
        import psutil

        processes = [proc for proc in psutil.process_iter()]
        try:
            processes.sort(key=lambda proc:proc.memory_info()[4])
        except Exception:
            pass
        for proc in processes:
            my_sysinfo[proc.name()] = proc.pid

        # os.system("wmic process get executablepath,ProcessId > c:\Python36-32\Lib\site-packages\debug_toolbar\log.txt")
        # with open("log.txt") as file:
        #
        #     for data in file.readlines():
        #         data = data.replace("\x00",'')
        #         d = data.split(".exe")
        #         try:
        #             d[0] = d[0] + ".exe"
        #             d[1] = d[1].strip()
        #             d[1] = d[1].replace(" ",'')
        #             my_sysinfo[d[0]] = d[1]
        #         except Exception:
        #             continue
        self.record_stats({
            'settings': OrderedDict(my_sysinfo.items()),
        })

