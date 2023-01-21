
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import reverse


# 如果未登录则转到登陆页面
def login(func):
    def login_fun(request, *args, **kwargs):
        if 'user_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect(reverse("df_user:login"))
            red.set_cookie('url', request.get_full_path())
            # 保证用户再登陆验证之后仍点击到希望的页面
            return red
    return login_fun
