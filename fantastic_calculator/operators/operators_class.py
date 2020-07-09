from fantastic_calculator.operators.operations import division_calculus, modulus_calculus, radical, \
    factorial_calculus, logarithm_based_ob_b, natural_logarithm, logarithm_based_on_ten, addition_calculus, \
    subtraction_calculus, multiplication_calculus, exponentiation_calculus


class Operator:
    def __init__(self, symbol, regex, description, can_be_prefix, is_binary, needs_index, calculation):
        self.symbol = symbol
        self.regex = regex
        self.description = description
        self.can_be_prefix = can_be_prefix  # for negative numbers, logarithms and radical (last two
        # also must have needs_index = True)
        self.is_binary = is_binary  # for operators requiring second number (not an index)
        self.needs_index = needs_index  # For radicals, logarithms and powers
        self.calculation = calculation


addition = Operator(symbol="+",
                    regex="\\+",
                    description="addition",
                    can_be_prefix=False,
                    is_binary=True,
                    needs_index=False,
                    calculation=lambda x, y: addition_calculus(x, y))
subtraction = Operator(symbol="-",
                       regex="-",
                       description="subtraction",
                       can_be_prefix=True,
                       is_binary=True,
                       needs_index=False,
                       calculation=lambda x, y: subtraction_calculus(x, y))
multiplication = Operator(symbol="*",
                          regex="\\*",
                          description="multiplication",
                          can_be_prefix=False,
                          is_binary=True,
                          needs_index=False,
                          calculation=lambda x, y: multiplication_calculus(x, y))
division = Operator(symbol="/",
                    regex="/",
                    description="division",
                    can_be_prefix=False,
                    is_binary=True,
                    needs_index=False,
                    calculation=lambda x, y: division_calculus(x, y))
exponentiation = Operator(symbol="^[i]",
                          regex="\\^\\[(-)?\\d+(\\.\\d+)?\\]",
                          description="exponentiation with index i",
                          can_be_prefix=False,
                          is_binary=False,
                          needs_index=True,
                          calculation=lambda x, y: exponentiation_calculus(x, y))
modulus = Operator(symbol="%",
                   regex="%",
                   description="modulus",
                   can_be_prefix=False,
                   is_binary=True,
                   needs_index=False,
                   calculation=lambda x, y: modulus_calculus(x, y))
radical_of_i_index = Operator(symbol="V[i]",
                              regex="V\\[\\d+\\]",
                              description="radical of i-index",
                              can_be_prefix=True,
                              is_binary=False,
                              needs_index=True,
                              calculation=lambda x, y: radical(x, y))
factorial = Operator(symbol="!",
                     regex="!",
                     description="factorial",
                     can_be_prefix=False,
                     is_binary=False,
                     needs_index=False,
                     calculation=lambda x, y: factorial_calculus(x))
logarithm_based_on_i = Operator(symbol="log[i]",
                                regex="log\\[\\d+\\]",
                                description="logarithm based on i",
                                can_be_prefix=True,
                                is_binary=False,
                                needs_index=True,
                                calculation=lambda x, y: logarithm_based_ob_b(x, y))
ln = Operator(symbol="ln",
              regex="ln",
              description="natural logarithm",
              can_be_prefix=True,
              is_binary=False,
              needs_index=False,
              calculation=lambda x, y: natural_logarithm(x))
lg = Operator(symbol="lg",
              regex="lg",
              description="logarithm based on 10",
              can_be_prefix=True,
              is_binary=False,
              needs_index=False,
              calculation=lambda x, y: logarithm_based_on_ten(x))
