from django.views import View
from django.http.response import JsonResponse
from . import models
from .forms.book import BookForm
from .forms.book import IdCardForm
import json

class BookView(View):
    def get(self,request):
        queryset = models.Book.objects.values("id","title")
        return JsonResponse({
            "code":0,
            "data":list(queryset)
        })



    def post(self,request):
        form = BookForm(json.loads(request.body.decode()))
        title_str = json.loads(request.body.decode())['title']
        print(title_str)
        if models.Book.objects.filter(title = title_str):
            #all_title_dict = {}
            #all_title_str = models.Book.objects.filter(title = title_str)
            all_title_str = models.Book.objects.filter(title = title_str).values("id","title")
            #all_title_str = json.dumps(list(models.Book.objects.filter(title = title_str).values("title","id")))
            #for all_title_new in all_title_str:
                # all_title_id = all_title_new.id
                # all_title_title = all_title_new.title
                # all_title_dict[all_title_id]=all_title_title
                # print(all_title_new.id)
            print(list(all_title_str)[0]["id"])
            return JsonResponse({
                "code": 1,
                "info":"有重复字段",
                #"data": all_title_dict, #str(all_title_id) + all_title_title #all_title_str
                "data":list(all_title_str)

            })

        if form.is_valid():
            instance = form.save()
            return JsonResponse({
                "code": 0,
                "data": f"添加成功，书ID为{instance.pk}"
            })
        else:
            return JsonResponse({
                "code": 1,
                "data": form.errors
            })


class BookDetailView(View):

    def get(self,request,pk):
        return JsonResponse({
                "code": 1,
                "data": "没做"
            })

    def put(self,request,pk):
        instance = models.Book.objects.filter(pk = pk).first()
        if not instance:
            return JsonResponse({
                "code": 1,
                "data": "数据不存在"
            })

        form = BookForm(instance, json.loads(request.body.decode()))
        form.one(instance, json.loads(request.body.decode()))
        if form.is_valid():
            instance = form.one_save()
            return JsonResponse({
                "code": 0,
                "data": f"修改ID为{instance.pk}的书名成功"
            })
        else:
            return JsonResponse({
                "code": 1,
                "data": form.errors
            })


    def delete(self,request, pk):
        models.Book.objects.filter(pk=pk).delete()
        return JsonResponse({
            "code": 0,
            "data": "删除成功"
        })


class MiniPro_Card(View):
    def post(self,request):
        form = IdCardForm(json.loads(request.body.decode()))
        id_repet = json.loads(request.body.decode())['id_repet']
        if id_repet == '0':
#            form = IdCardForm(json.loads(request.body.decode()))
            IdCardForm_name = json.loads(request.body.decode())['name']
            IdCardForm_idnum = json.loads(request.body.decode())['idnum']
            IdCardForm_session = json.loads(request.body.decode())['session']

            if models.IDCard.objects.filter(name=IdCardForm_name,idnum=IdCardForm_idnum,session=IdCardForm_session):
                all_repet = models.IDCard.objects.filter(name=IdCardForm_name,idnum=IdCardForm_idnum,session=IdCardForm_session).values("name","idnum","session","data")
                return JsonResponse({
                    "code": 201,
                    "info": "有重复字段",
                    "data": list(all_repet)
                })

            elif form.is_valid():
                instance = form.save()
                return JsonResponse({
                    "code": 200,
                    "data": f"添加成功，人ID为{instance.pk}"
                })

            else:
                return JsonResponse({
                    "code": 400,
                    "info": "检查提交信息",
                    "data": form.errors
                })


        elif id_repet == '1':
#            form = IdCardForm(json.loads(request.body.decode()))
            if form.is_valid():
                instance = form.save()
                return JsonResponse({
                    "code": 200,
                    "data": f"添加成功，人ID为{instance.pk}"
                })
            else:
                return JsonResponse({
                    "code": 400,
                    "info": "检查提交信息",
                    "data": form.errors
                })

    def get(self,request):
        queryset = models.IDCard.objects.values("name","idnum","session","data")
        return JsonResponse({
            "code":200,
            "data":list(queryset)
        })
