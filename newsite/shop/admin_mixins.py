import csv
from django.db.models.options import Options
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse


class ExportAsMixinCsv:
    """ This class for export all objects in csv(Exel) file """

    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        meta: Options = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}-export.csv'
        csv_writer = csv.writer(response)
        csv_writer.writerow(field_names)

        for obj in queryset:
            csv_writer.writerow([getattr(obj, field) for field in field_names])

        return response
