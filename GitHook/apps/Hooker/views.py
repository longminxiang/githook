# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ProjectInfo
from .hook import add_rsa_key, git_clone_or_pull


@csrf_exempt
def git_hook_view(request, pname):
    info = None
    try:
        info = ProjectInfo.objects.get(name=pname, is_active=True)

        if info.use_rsa:
            add_rsa_key(info.git_host, info.rsa_pri_key)

        git_clone_or_pull(info.project_path, info.name, info.git_url)
        return HttpResponse("success")
    except Exception:
        pass
    return HttpResponse("failed")
