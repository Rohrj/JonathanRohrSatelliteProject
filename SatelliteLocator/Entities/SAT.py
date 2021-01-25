from sqlalchemy import Column, Integer, String
from SatelliteLocator.Database.base import Base

#Class for satellite
class SAT(Base):
    __tablename__ = "SAT"
    catalog_number = Column(Integer, primary_key=True, nullable=False)
    classification = Column(String)
    launch_year = Column(Integer)
    launch_num_and_designator = Column(String(20))

    def __init__(self, catalogNumber, classification, launchYear, launchNumAndDesignator):
        self.catalog_number = catalogNumber
        self.classification = classification
        self.launch_year = launchYear
        self.launch_num_and_designator = launchNumAndDesignator

    def getCatalogNumber(self):
        return self.catalog_number
    
    def getClassification(self):
        return self.classification
        
    def getLaunchYear(self):
        return self.launch_year
    
    def getLaunchNumAndDesignator(self):
        return self.launch_num_and_designator