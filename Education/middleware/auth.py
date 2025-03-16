from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 0.排除那些不需要登录就能访问的页面
        # request.path_info 获取当前用户请求的URL /login/
        if request.path_info == "/login/":
            return
        # 1.读取当前访问的用户的session信息，如果能读到，说明已登陆过，就可以继续向后走
        info_dict = request.session.get("info")
        # print(info_dict)
        if info_dict:
            return
        # 2.没有登录过，重新回到登录页面
        # 如果方法中没有返回值（返回None），继续向后走
        # 如果有返回值 HttpResponse、render、redirect
        # return HttpResponse("无权访问")
        return redirect("/login/")
