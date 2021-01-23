from sqlalchemy import Column, Integer, Float, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from Database.base import Base

#Class for satellite records
class LOC(Base):
    __tablename__ = "LOC"
    loc_id = Column(Integer, primary_key=True, nullable=False)
    sat_id = Column(Integer, ForeignKey("SAT.catalog_number"), nullable=False)
    sat = relationship("SAT", backref="SAT.catalog_number")
    date = Column(Text)
    first_deriv_mean = Column(Float)
    second_deriv_mean = Column(Float)
    drag_term = Column(Float)
    elem_set_number = Column(Integer)
    inclination = Column(Float)
    right_asc = Column(Float)
    eccentricity = Column(Float)
    arg_perigree = Column(Float)
    mean_anomaly = Column(Float)
    mean_motion = Column(Float)
    rev_number_at_epoch = Column(Integer)

    def __init__(self, catalogNumber, date, firstDerivMean, secondDerivMean, dragTerm, elemSetNumber, inclination, rightAsc, eccentricity, argPerigree, meanAnomaly, meanMotion, revNumberAtEpoch):
        self.sat_id = catalogNumber
        self.date = date
        self.first_deriv_mean = firstDerivMean
        self.second_deriv_mean = secondDerivMean
        self.drag_term = dragTerm
        self.elem_set_number = elemSetNumber
        self.inclination = inclination
        self.right_asc = rightAsc
        self.eccentricity = eccentricity
        self.arg_perigree = argPerigree
        self.mean_anomaly = meanAnomaly
        self.mean_motion = meanMotion
        self.rev_number_at_epoch = revNumberAtEpoch

    def getCatalogNumber(self):
        return self.sat_id
    
    def getDate(self):
        return self.date
        
    def getFirstDerivMean(self):
        return self.first_deriv_mean
    
    def getSecondDerivMean(self):
        return self.second_deriv_mean

    def getDragTerm(self):
        return self.drag_term

    def getElemSetNumber(self):
        return self.elem_set_number
    
    def getInclination(self):
        return self.inclination
        
    def getRightAsc(self):
        return self.right_asc
    
    def getEccentricity(self):
        return self.eccentricity

    def getArgPerigree(self):
        return self.arg_perigree

    def getMeanAnomaly(self):
        return self.mean_anomaly
    
    def getMeanMotion(self):
        return self.mean_motion
        
    def getRevNumberAtEpoch(self):
        return self.rev_number_at_epoch