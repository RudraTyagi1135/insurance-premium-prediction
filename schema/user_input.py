#imports
from pydantic import BaseModel , computed_field ,Field ,field_validator
from typing import Optional, Literal, Annotated


#import cities
from config.city_tier import tier_1_cities,tier_2_cities


#user_input_pydantic_model
class UserInput(BaseModel):
    """do value and data validation of input"""
    age: Annotated[int, Field(...,gt=0,lt=120,description = "age of the user")]
    weight: Annotated[float, Field(...,description = "weight of the user in KG")]
    height: Annotated[float, Field(...,description = "height of the user in meter")]
    income_lpa: Annotated[float, Field(...,gt=0,description = "height of the user in meter")]
    smoker: Annotated[bool, Field(...,description = "is user a smoker")]
    city: Annotated[str, Field(...,description = "where user lives")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    
    #make field validator w.r.t city 
    @field_validator('city')
    @classmethod
    def strip(cls,i):
        i = i.strip().title()
        return i


    #compute bmi
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    

    #compute lifestyle_risk
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        

    #compute age group of user    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    


    #compute tier if city where user lives in
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
