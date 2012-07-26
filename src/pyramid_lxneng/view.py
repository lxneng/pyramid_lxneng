# -*- coding: utf-8 -*-


class BasicView(object):

    def __init__(self, context, request):
        self.request = request
        self.context = context

    def __call__(self):
        return {}


class BasicFormView(BasicView):

    form_class = None

    def __init__(self, context, request):
        super(BasicFormView, self).__init__(context, request)
        if self.request.method == 'POST':
            self.form = self.form_class(self.request.POST, obj=self.context,
                                        **self.default_data())
        else:
            self.form = self.form_class(
                obj=self.context, **self.default_data())

    def default_data(self):
        return {}

    def do_post(self):
        raise NotImplementedError()

    def __call__(self):
        if self.request.method == 'POST':
            response = self.do_post()
            if response is not None:
                return response
        return {'form': self.form}