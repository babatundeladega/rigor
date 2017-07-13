import enum


@enum.unique
class Status(enum.Enum):
    ACTIVE = "ACTIVE"
    SKIPPED = "SKIPPED"
    PASSED = "PASSED"
    FAILED = "FAILED"


@enum.unique
class Method(enum.Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


@enum.unique
class Comparison(enum.Enum):
    CONTAINS = "contains"
    NOT_CONTAINS = "not contains"
    GREATER_THAN = "greater than"
    EQUALS = "equals"
    IN = "in"
    NOT_IN = "not in"
    SAME = "same"

    def is_contains(self, actual, expect):
        return expect in actual

    def is_not_contains(self, actual, expect):
        return expect not in actual

    def is_equals(self, actual, expect):
        return actual == expect

    def is_in(self, actual, expect):
        return actual in expect

    def is_not_in(self, actual, expect):
        return actual not in expect

    def is_same(self, actual, expect):
        """
        Returns true if equal or if 2 lists, have the same items
        regardless of order.
        """
        same = actual == expect
        if not same and isinstance(actual, list) and isinstance(expect, list):
            same = bool(len(actual) and len(expect))
            same = same and all([item in expect for item in actual])
            same = same and all([item in actual for item in expect])
        return same

    def evaluate(self, actual, expected):
        method = getattr(self, "is_%s" % self.value.replace(" ", "_"))
        try:
            return method(actual, expected)
        except:
            return False
