from schemas.predict import MultipleBCancerDataInputs


def test_example_existance():
    assert len(MultipleBCancerDataInputs.Config.schema_extra['example']['inputs'][0]) == 30
