Module Base Attachment
----------------------


Add dependency of the module Base Attachment in your module __manifest__.py file :
----------------------------------------------------------------------------------
'depends': ['base', 'base_attachment'],


Add One2many fields to your module class :
------------------------------------------

attachment_ids = fields.One2many( comodel_name='max.base.multi.attachment', inverse_name='owner_id', string='Attachments', domain=lambda self: [('owner_model', '=', self._name), ('owner_field', '=', 'attachment_ids')], copy=True)


Add fields to your module View :
--------------------------------
#<field name="attachment_ids" context="{'default_owner_model': 'your.model.name', 'default_owner_id': id, 'default_owner_field': 'attachment_ids',}"/>


