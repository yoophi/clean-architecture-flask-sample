from typing import Iterable, ContextManager

from app.core.domain import Invoice


class InvoiceRepository:
    def get_list(self, filters) -> Iterable[Invoice]:
        raise NotImplementedError()

    def atomic(self) -> ContextManager:
        raise NotImplementedError()

    def save(self, invoice: Invoice) -> Invoice:
        raise NotImplementedError()