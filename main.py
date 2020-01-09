from dotenv import load_dotenv
from google.cloud import ndb

from models import AModel, BModel, CModel

load_dotenv()

if __name__ == "__main__":
    client = ndb.Client()

    with client.context():
        k_amodel = AModel(s_foo="test").put()
        k_bmodel = BModel(s_bar="test", k_amodel=k_amodel).put()
        CModel(s_foobar="test", k_bmodel=k_bmodel).put()
