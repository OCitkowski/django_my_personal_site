from django.test import TestCase
from handbook.models import Source, Note, Owner


class TestFildEqual(TestCase):

    def setUp(self):
        self.owner1 = Owner.objects.create(name='Test1', comment='test_comment1')
        self.source1 = Source.objects.create(name='TestSource1', comment='testSource_comment1')
        self.note1 = Note.objects.create(owner=self.owner1, source=self.source1, status='A',
                                         text='765uyhf8967786895jhfgkfkjgouigi', comment='testSource_comment1')

    def test_owner(self):
        self.assertEqual('Test1', self.owner1.name, 'owner not equal to owner fild name')
        self.assertEqual('test_comment1', self.owner1.comment, 'comment not equal to owner fild comment')

    def test_source(self):
        self.assertEqual('TestSource1', self.source1.name, 'owner not equal to Source fild name')
        self.assertEqual('testSource_comment1', self.source1.comment, 'comment not equal to Source fild comment')

    def test_note(self):
        self.assertEqual(self.owner1, self.note1.owner, 'owner not equal to note fild owner')
        self.assertEqual(self.source1, self.note1.source, 'source not equal to note fild source')
        self.assertEqual('A', self.note1.status, 'status not equal to note fild status')
        self.assertEqual('765uyhf8967786895jhfgkfkjgouigi', self.note1.text, 'text not equal to note fild text')
        self.assertEqual('testSource_comment1', self.note1.comment, 'comment not equal to note fild comment')
