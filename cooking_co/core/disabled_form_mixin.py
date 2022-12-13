# class DisabledFormMixin:
#     disabled_fields = ()
#     fields = {}
#
#     def _disable_fields(self):
#         if self.disabled_fields == 'all':
#             fields = self.fields.keys()
#         else:
#             fields = self.disabled_fields
#
#         for field_name in fields:
#             if field_name in self.fields:
#                 field = self.fields[field_name]
#                 field.widget.attrs['disabled'] = 'disabled'
#                 field.required = False
#                 # field.widget.attrs['readonly'] = 'readonly'