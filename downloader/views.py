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
    def get(self, request, id):
        dl_file = get_object_or_404(DlModel, pk=id)
        if request.user in dl_file.users.all():
            return render(request, self.template_name, {"id":dl_file.id})
        return render(request, self.template_name, {"mes":"You Don't Have Acses"})


class FileDownloadView(LoginRequiredMixin, View):
    def get(self, request, id):
        obj = get_object_or_404(DlModel, pk=id)
        if request.user in obj.users.all():
            file_handle = obj.dl_file.path
            document = open(file_handle, 'rb')
            response = HttpResponse(FileWrapper(document), content_type='application/msword')
            response['Content-Disposition'] = 'attachment; filename="%s"' % obj.dl_file.name
            return response
        return redirect("/")