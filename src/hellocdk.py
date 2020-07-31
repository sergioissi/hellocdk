from aws_cdk import core


class TestlibcdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        print("non funzionerà mai")
        # The code that defines your stack goes here
