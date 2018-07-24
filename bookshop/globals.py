def get_context(request):
    context = dict()
    context['site_title'] = "BookShop Sys"
    context["site_title_long"] = " BookShop System "
    context["site_author"] = "Jerry Shikanga"
    context["site_description"] = "This is a bookshop management web app"

    return context


class ModelGetFieldsMixin(object):
    def get_fields(self):
        field_list = [[field.name, field.value_to_string(self)] for field in self._meta.fields if field.name is not "id"]
        return field_list
