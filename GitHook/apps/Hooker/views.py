# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ProjectInfo
import os


@csrf_exempt
def git_hook_view(request, pname):
    info = None
    try:
        info = ProjectInfo.objects.get(name=pname, is_active=True)

        if not os.path.exists(info.project_path):
            os.system("mkdir " + info.project_path)
        if os.path.exists(info.project_dir):
            os.system("cd %s && git pull" % info.project_dir)
        else:
            os.system("cd %s && yes | git clone %s" % (info.project_path, info.git_url))
        return HttpResponse("success")
    except Exception:
        pass
    return HttpResponse("failed")
