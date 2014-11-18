from app import app, db
from models import *
from flask import Flask, flash, redirect, url_for, request, render_template, g, abort
from flask.ext.admin import Admin, expose, BaseView, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
import urllib
from datetime import datetime
import time
from operator import itemgetter
import logging
from sqlalchemy import func

FRONTEND_HOST = app.config['FRONTEND_HOST']
API_HOST = app.config['API_HOST']

logger = logging.getLogger(__name__)

@app.context_processor
def inject_paths():
    return dict(FRONTEND_HOST=FRONTEND_HOST)

@app.template_filter('add_commas')
def jinja2_filter_add_commas(quantity):
    out = ""
    quantity_str = str(quantity)
    while len(quantity_str) > 3:
        tmp = quantity_str[-3::]
        out = "," + tmp + out
        quantity_str = quantity_str[0:-3]
    return quantity_str + out


class MyIndexView(AdminIndexView):
    @expose("/")
    def index(self):

        record_counts = {
            'committee': Organisation.query.filter_by(type="committee").count(),
            }

        return self.render('admin/my_index.html', record_counts=record_counts)


class MyModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True


class CommitteeView(MyModelView):

    form_ajax_refs = {
        'events': {
            'fields': ('date', 'title', EventType.name),
            'page_size': 25
        }
    }
    column_list = ('name', 'house')
    column_sortable_list = ('name', ('house', 'house.name'))
    column_searchable_list = ('name', )
    form_columns = ('name', 'house')

    def on_model_change(self, form, model, is_created):
        if is_created:
            # set some default values when creating a new record
            model.type = "committee"
            model.version = 0

    def get_query(self):
        """
        Add filter to return only non-deleted records.
        """

        return self.session.query(self.model) \
            .filter(self.model.type == "committee")

    def get_count_query(self):
        """
        Add filter to count only non-deleted records.
        """

        return self.session.query(func.count('*')).select_from(self.model) \
            .filter(self.model.type == "committee")

admin = Admin(app, name='PMG-CMS', base_template='admin/my_base.html', index_view=MyIndexView(name='Home'), template_mode='bootstrap3')

admin.add_view(CommitteeView(Organisation, db.session, name="Committee", endpoint='committee', category="Committees"))
admin.add_view(MyModelView(CommitteeInfo, db.session, name="Committee Info", endpoint='committee-info', category="Committees"))

admin.add_view(MyModelView(Member, db.session, name="Member Profile", endpoint='member', category="Members"))
admin.add_view(MyModelView(Membership, db.session, name="Membership", endpoint='membership', category="Members"))
admin.add_view(MyModelView(MembershipType, db.session, name="Membership Type", endpoint='membership-type', category="Members"))

