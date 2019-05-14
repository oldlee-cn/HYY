from django.shortcuts import render

from django.views.generic.base import View

from .models import Category
from repair.models import Repair
from region.models import Region
from .forms import RepairForm


class RepairView(View):
    def get(self,request):
        #实例化RegisterForm类
        register_form = RepairForm()
        category_names = Category.objects.all()

        region_name = Region.objects.all()
        repair_names = Repair.objects.all()
        #对register.html页面返回register_form
        return render(request,'demo.html',{
            'category_names':category_names,
            'region_name':region_name,
            'repair_names':repair_names,
            'register_form':register_form})

    def post(self,request):
        register_form = RepairForm(request.POST)
        category_names = Category.objects.all()

        region_name = Region.objects.all()
        repair_names = Repair.objects.all()
        # 判断用户post的数据的合法性，判断条件是form.py文件的RegisterForm类里定义的
        if register_form.is_valid():
            name = request.POST.get('name', '')
            username = request.POST.get('username','')
            userage = request.POST.get('userage','')
            repairregion = request.POST.get('repairregion','')
            repaircategory = request.POST.get('repaircategory','')
            repairimg = request.POST.get('repairimg','')
            repaircontent = request.POST.get('repaircontent','')

            # 实例化model里的用户表类
            repair_con = Repair()
            # 并将上面post到的用户提交的数据进行向表字段填充
            repair_con.name = name
            repair_con.username = username
            repair_con.userage = userage
            repair_con.repairregion = repairregion
            repair_con.repaircategory = repaircategory
            repair_con.repairimg = repairimg
            repair_con.repaircontent = repaircontent
            # 最后保存
            repair_con.save()
            # 数据保存后，发送邮件
            # 返回到登录页面，无报错
            return render(request,'demo.html')
        else:
            # 返回在注册页面，报错form文件的验证错误
            return render(request, 'demo.html', {
                'category_names':category_names,
                'region_name':region_name,
                'repair_names':repair_names,
                'register_form':register_form,
                'msg': "出错了，请刷新页面重试！ "})

