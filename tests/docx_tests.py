from nose.tools import istest, assert_equal

from mammoth import docx, documents
from mammoth.xmlparser import element as xml_element, text as xml_text
from .testing import test_path

@istest
class ReadTests(object):
    @istest
    def can_read_document_with_single_paragraph_with_single_run_of_text(self):
        with open(test_path("single-paragraph.docx")) as fileobj:
            result = docx.read(fileobj=fileobj)
            expected_document = documents.Document([
                documents.Paragraph([
                    documents.Run([
                        documents.Text("Walking on imported air")
                    ])
                ])
            ])
            assert_equal(expected_document, result.value)


@istest
class ReadXmlElementTests(object):
    @istest
    def text_from_text_element_is_read(self):
        element = _text_element("Hello!")
        assert_equal(documents.Text("Hello!"), docx.read_xml_element(element))
    
    @istest
    def can_read_text_within_run(self):
        element = _run_element_with_text("Hello!")
        assert_equal(
            documents.Run([documents.Text("Hello!")]),
            docx.read_xml_element(element)
        )
    
    @istest
    def can_read_text_within_paragraph(self):
        element = _paragraph_element_with_text("Hello!")
        assert_equal(
            documents.Paragraph([documents.Run([documents.Text("Hello!")])]),
            docx.read_xml_element(element)
        )
    
    @istest
    def can_read_text_within_paragraph(self):
        element = _paragraph_element_with_text("Hello!")
        assert_equal(
            documents.Paragraph([documents.Run([documents.Text("Hello!")])]),
            docx.read_xml_element(element)
        )
    
    @istest
    def can_read_text_within_document(self):
        element = _document_element_with_text("Hello!")
        assert_equal(
            documents.Document([documents.Paragraph([documents.Run([documents.Text("Hello!")])])]),
            docx.read_xml_element(element)
        )


def _document_element_with_text(text):
    return xml_element("w:document", {}, [
        xml_element("w:body", {}, [_paragraph_element_with_text(text)])
    ])


def _paragraph_element_with_text(text):
    return xml_element("w:p", {}, [_run_element_with_text(text)])


def _run_element_with_text(text):
    return xml_element("w:r", {}, [_text_element(text)])


def _text_element(value):
    return xml_element("w:t", {}, [xml_text(value)])
    