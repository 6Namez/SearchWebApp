from unittest import TestCase

from back_end.document_process.documents import TransformedDocument
from back_end.indexing.tf_idf_index import TfIdfIndex

class TestTfIdfIndex(TestCase):
    def test_add_document(self):
        doc = TransformedDocument(doc_id='1', terms=['some', 'terms', 'terms'])
        index = TfIdfIndex()
        index.add_document(doc)
        self.assertEqual({'some': 1, 'terms': 1}, index.doc_counts)
        self.assertEqual({'1': {'some': 1, 'terms': 2}}, index.id_to_term_counts)

        doc = TransformedDocument(doc_id='2', terms=['some', 'some', 'terms'])
        index.add_document(doc)
        self.assertEqual({'some': 2, 'terms': 2}, index.doc_counts)
        self.assertEqual(
            {
                '1': {'some': 1, 'terms': 2},
                '2': {'some': 2, 'terms': 1}
            }, index.id_to_term_counts)
