import json

from flask import Blueprint
from flask_restful import Resource, Api

from app.adapters import InvoiceAdapter
from app.core.repository import InvoiceRepository


class InvoiceResource(Resource):
    default_length = 100

    def __init__(self, *args, **kwargs):
        self.super().__init__(*args, **kwargs)
        self.adapter = InvoiceAdapter(InvoiceRepository())

    def get(self, number=None):
        if number:
            return self.get_one(number)
        return self.get_list()

    def get_one(self, number):
        invoice = self.adapter.get_list({'number': number})
        return json.dumps(invoice)

    def get_list(self):
        invoices = self.adapter.get_list()
        return json.dumps(invoices)


api = Blueprint('api', __name__)

invoice_api = Api(api)
invoice_api.add_resource(InvoiceResource, '/invoices/<int:number>', '/invoices')
