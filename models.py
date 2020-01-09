from google.cloud import ndb


class AModel(ndb.Model):
    s_foo = ndb.StringProperty()


class BModel(ndb.Model):
    s_bar = ndb.StringProperty()
    k_amodel = ndb.KeyProperty(kind="AModel", indexed=True)


class CModel(ndb.Model):
    s_foobar = ndb.StringProperty()
    k_bmodel = ndb.KeyProperty(kind="BModel", indexed=True)
    k_amodel = ndb.ComputedProperty(
        lambda self: self.k_bmodel.get().k_amodel if self.k_bmodel else None,
    )
