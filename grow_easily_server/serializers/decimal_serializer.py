import json
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            if isinstance(o, decimal.Decimal):
                if o % 1 == 0:
                    return int(o)
                else:
                    return float(o)
            return super().default(o)
        except AttributeError:
            return super().default(o)
