from typing import List, Optional

from pydantic import BaseModel, Field


class PredictionResults(BaseModel):
    version: str
    predictions: Optional[List[float]]


class BCancerDataInputSchema(BaseModel):
    meanradius: Optional[float] = Field(alias="mean radius")
    meantexture: Optional[float] = Field(alias="mean texture")
    meanperimeter: Optional[float] = Field(alias="mean perimeter")
    meanarea: Optional[float] = Field(alias="mean area")
    meansmoothness: Optional[float] = Field(alias="mean smoothness")
    meancompactness: Optional[float] = Field(alias="mean compactness")
    meanconcavity: Optional[float] = Field(alias="mean concavity")
    meanconcavepoints: Optional[float] = Field(alias="mean concave points")
    meansymmetry: Optional[float] = Field(alias="mean symmetry")
    meanfractaldimension: Optional[float] = Field(alias="mean fractal dimension")
    radiuserror: Optional[float] = Field(alias="radius error")
    textureerror: Optional[float] = Field(alias="texture error")
    perimetererror: Optional[float] = Field(alias="perimeter error")
    areaerror: Optional[float] = Field(alias="area error")
    smoothnesserror: Optional[float] = Field(alias="smoothness error")
    compactnesserror: Optional[float] = Field(alias="compactness error")
    concavityerror: Optional[float] = Field(alias="concavity error")
    concavepointserror: Optional[float] = Field(alias="concave points error")
    symmetryerror: Optional[float] = Field(alias="symmetry error")
    fractaldimensionerror: Optional[float] = Field(alias="fractal dimension error")
    worstradius: Optional[float] = Field(alias="worst radius")
    worsttexture: Optional[float] = Field(alias="worst texture")
    worstperimeter: Optional[float] = Field(alias="worst perimeter")
    worstarea: Optional[float] = Field(alias="worst area")
    worstsmoothness: Optional[float] = Field(alias="worst smoothness")
    worstcompactness: Optional[float] = Field(alias="worst compactness")
    worstconcavity: Optional[float] = Field(alias="worst concavity")
    worstconcavepoints: Optional[float] = Field(alias="worst concave points")
    worstsymmetry: Optional[float] = Field(alias="worst symmetry")
    worstfractaldimension: Optional[float] = Field(alias="worst fractal dimension")


class MultipleBCancerDataInputs(BaseModel):
    inputs: List[BCancerDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "mean radius": 17.27,
                        "mean texture": 25.42,
                        "mean perimeter": 112.4,
                        "mean area": 928.8,
                        "mean smoothness": 0.08331,
                        "mean compactness": 0.1109,
                        "mean concavity": 0.1204,
                        "mean concave points": 0.05736,
                        "mean symmetry": 0.1467,
                        "mean fractal dimension": 0.05407,
                        "radius error": 0.51,
                        "texture error": 1.679,
                        "perimeter error": 3.283,
                        "area error": 58.38,
                        "smoothness error": 0.008109,
                        "compactness error": 0.04308,
                        "concavity error": 0.04942,
                        "concave points error": 0.01742,
                        "symmetry error": 0.01594,
                        "fractal dimension error": 0.003739,
                        "worst radius": 20.38,
                        "worst texture": 35.46,
                        "worst perimeter": 132.8,
                        "worst area": 1284.0,
                        "worst smoothness": 0.1436,
                        "worst compactness": 0.4122,
                        "worst concavity": 0.5036,
                        "worst concave points": 0.1739,
                        "worst symmetry": 0.25,
                        "worst fractal dimension": 0.07944,
                    }
                ]
            }
        }
