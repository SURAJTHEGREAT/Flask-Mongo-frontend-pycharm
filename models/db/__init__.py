import six
import mongoengine
import os
from logger import log as logging

# GENERATE THE LOG PATH FROM CURRENT FILE NAME
logpath = os.path.splitext(os.path.basename(__file__))[0] + '.log'
LOG = logging.getLogger(__name__)

#https://dbader.org/blog/meaning-of-underscores-in-python

def _db_connect(db_name, db_host, db_port, username=None, password=None):

#check this https://code.cognizant.com/avm-chatops/stackstorm-file-changes/blob/master/stackstorm/st2/lib/python2.7/site-packages/st2common/models/db/__init__.py









