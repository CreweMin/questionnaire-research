#注意这里必须先引入model

from dbmodels.usermodel import User
from dbmodels.securitymodel import Security
from dbmodels.secretmodel import Secret
from dbmodels.rolemodel import Role
from dbmodels.questionnairemodel import Questionnaire
from dbmodels.classifymodel import Classify 
from dbmodels.subjectmodel import Subject
from dbmodels.optiontablemodel import Optiontable
from dbmodels.interlocutionmodel import Interlocution
from dbmodels.usertokenmodel import Usertoken
from dbmodels.searchlogmodel import Searchlog
from orml.dbbase import engine
from orml.dbbase import Base
from orml.dbbase import DBSession
Base.metadata.create_all(engine)
import orml.createvalue
