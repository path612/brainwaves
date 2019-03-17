from flask_sqlalchemy import SQLAlchemy
import psycopg2
import datetime
import json


db = SQLAlchemy()


class BaseModel(db.Model):

	__abstract__ = True

	@classmethod
	def findAll(cls, **parameters):
		return cls.query.filter_by(**parameters).all()

	@classmethod
	def find(cls, **filters):
		return cls.query.filter_by(**filters)

	@classmethod
	def findWithOrderBy(cls, orderBy, **filters):
		return cls.query.filter_by(**filters).order_by(orderBy)

	@classmethod
	def findFirst(cls, **parameters):
		return cls.find(**parameters).first()

	def save(self):
		db.session.add(self)
		db.session.commit()
		return self

	def json(self, fields, jsonFields=[]):
		return json.loads(json.dumps(self, cls=new_alchemy_encoder(False, fields, jsonFields), check_circular=False))


class sgSideModel(BaseModel, db.Model):
	__tablename__ = "sgside"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	ourReference = db.Column(db.String(100))
	typeOfOperation = db.Column(db.String(100))
	commonReference = db.Column(db.String(100))
	contractdate = db.Column(db.String(100))
	randoma = db.Column(db.String(100))
	partyA = db.Column(db.String(100))
	partyB = db.Column(db.String(100))
	isdaDate = db.Column(db.String(100))
	valueDate = db.Column(db.String(100))
	exchangeRate = db.Column(db.String(100))
	buyQuant = db.Column(db.String(100))
	settlement1 = db.Column(db.String(100))
	sellQuant = db.Column(db.String(100))
	deliveryAgent1 = db.Column(db.String(100))
	intermediatery = db.Column(db.String(100))
	settlement2 = db.Column(db.String(100))
	beneficiary2 = db.Column(db.String(100))

	
	def __init__(self,ourReference ,typeOfOperation ,commonReference ,contractDate , randoma ,partyA ,partyB , isdaDate,valueDate ,exchangeRate ,buyQuant ,settlement1 ,sellQuant ,deliveryAgent1 ,intermediatery,settlement2 ,beneficiary2):
		self.ourReference = ourReference
		self.typeOfOperation = typeOfOperation
		self.commonReference = commonReference
		self.contractDate = contractDate
		self.randoma = randoma
		self.partyA = partyA
		self.partyB= partyB
		self.isdaDate = isdaDate
		self.valueDate =valueDate  
		self.exchangeRate = exchangeRate
		self.buyQuant = buyQuant
		self.settlement1 = settlement1
		self.sellQuant = sellQuant
		self.deliveryAgent1 = deliveryAgent1
		self.intermediatery = intermediatery
		self.settlement2 = settlement2
		self.beneficiary2 = beneficiary2

	@classmethod
	def insert(cls, ourReference ,typeOfOperation ,commonReference ,contractDate , randoma ,partyA ,partyB , isdaDate,valueDate ,exchangeRate ,buyQuant ,settlement1 ,sellQuant ,deliveryAgent1 ,intermediatery,settlement2 ,beneficiary2):
		data = sgSideModel(ourReference ,typeOfOperation ,commonReference ,contractDate , randoma ,partyA ,partyB , isdaDate,valueDate ,exchangeRate ,buyQuant ,settlement1 ,sellQuant ,deliveryAgent1 ,intermediatery,settlement2 ,beneficiary2)
		return data.save()


class cpSideModel(BaseModel, db.Model):
	__tablename__ = "cpside"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	ourReference = db.Column(db.String(100))
	typeOfOperation = db.Column(db.String(100))
	commonReference = db.Column(db.String(100))
	contractdate = db.Column(db.String(100))
	randoma = db.Column(db.String(100))
	partyA = db.Column(db.String(100))
	partyB = db.Column(db.String(100))
	isdaDate = db.Column(db.String(100))
	valueDate = db.Column(db.String(100))
	exchangeRate = db.Column(db.String(100))
	buyQuant = db.Column(db.String(100))
	settlement1 = db.Column(db.String(100))
	sellQuant = db.Column(db.String(100))
	deliveryAgent1 = db.Column(db.String(100))
	intermediatery = db.Column(db.String(100))
	settlement2 = db.Column(db.String(100))
	beneficiary2 = db.Column(db.String(100))

	
	def __init__(self,ourReference ,typeOfOperation ,commonReference ,contractDate , randoma ,partyA ,partyB , isdaDate,valueDate ,exchangeRate ,buyQuant ,settlement1 ,sellQuant ,deliveryAgent1 ,intermediatery,settlement2 ,beneficiary2):
		self.ourReference = ourReference
		self.typeOfOperation = typeOfOperation
		self.commonReference = commonReference
		self.contractDate = contractDate
		self.randoma = randoma
		self.partyA = partyA
		self.partyB= partyB
		self.isdaDate = isdaDate
		self.valueDate =valueDate  
		self.exchangeRate = exchangeRate
		self.buyQuant = buyQuant
		self.settlement1 = settlement1
		self.sellQuant = sellQuant
		self.deliveryAgent1 = deliveryAgent1
		self.intermediatery = intermediatery
		self.settlement2 = settlement2
		self.beneficiary2 = beneficiary2

	@classmethod
	def insert(cls, ourReference ,typeOfOperation ,commonReference ,contractDate , randoma ,partyA ,partyB , isdaDate,valueDate ,exchangeRate ,buyQuant ,settlement1 ,sellQuant ,deliveryAgent1 ,intermediatery,settlement2 ,beneficiary2):
		data = cpSideModel(ourReference ,typeOfOperation ,commonReference ,contractDate , randoma ,partyA ,partyB , isdaDate,valueDate ,exchangeRate ,buyQuant ,settlement1 ,sellQuant ,deliveryAgent1 ,intermediatery,settlement2 ,beneficiary2)
		return data.save()
