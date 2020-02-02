from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from cloudmesh.common.util import banner


class MathUtil:
    operErrors = []

    def add(self, n1, n2):
        HEADING()
        result = n1 + n2
        return result

    def divide(self, n1, n2):
        HEADING()
        result = 0
        try:
            result = n1 / n2
        except ZeroDivisionError as err:
            self.operErrors.append({"operation": "divide", "Error": f"Error when dividing {n1} by {n2} : {err}"})
        return result


if __name__ == '__main__':
    mathUtil = MathUtil()
    banner("Start:: Testing Math Util")
    sum = mathUtil.add(3, 5)
    print(sum)
    div = mathUtil.divide(50, 0)
    banner("End:: Testing Math Util")

    VERBOSE(mathUtil.operErrors[0])
