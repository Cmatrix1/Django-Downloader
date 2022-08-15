from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DlModel
from wsgiref.util import FileWrapper
from django.http import HttpResponse


class HomeView(LoginRequiredMixin, ListView):
    model = DlModel
    template_name = "downloader/home.html"
    context_object_name = "files"


class DownladPageView(LoginRequiredMixin, View):
    template_name = "downloader/page.html"
    def dispatch(self, request, id):
        self.file = get_object_or_404(DlModel, pk=id)
        if request.user in self.file.users.all():
            return super().dispatch(request, id)
        else:
            return render(request, self.template_name, {"mes":"You Don't Have Acses"})
        
    def get(self, request, id):
        return render(request, self.template_name, {"id":self.file.id})

    def post(self, request, id):
        print("FINd", self.file)
        file_handle = self.file.dl_file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/msword')
        response['Content-Disposition'] = 'attachment; filename="%s"' % self.file.dl_file.name
        return response


