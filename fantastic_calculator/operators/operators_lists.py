from fantastic_calculator.operators.operators_class import addition, subtraction, multiplication, division, \
    exponentiation, modulus, radical_of_i_index, factorial, logarithm_based_on_i, ln, lg


operators_list = {
    addition.symbol: addition,
    subtraction.symbol: subtraction,
    multiplication.symbol: multiplication,
    division.symbol: division,
    exponentiation.symbol: exponentiation,
    modulus.symbol: modulus,
    radical_of_i_index.symbol: radical_of_i_index,
    factorial.symbol: factorial,
    logarithm_based_on_i.symbol: logarithm_based_on_i,
    ln.symbol: ln,
    lg.symbol: lg
}

operators_regex_list = {
    addition.regex: addition,
    subtraction.regex: subtraction,
    multiplication.regex: multiplication,
    division.regex: division,
    exponentiation.regex: exponentiation,
    modulus.regex: modulus,
    radical_of_i_index.regex: radical_of_i_index,
    factorial.regex: factorial,
    logarithm_based_on_i.regex: logarithm_based_on_i,
    ln.regex: ln,
    lg.regex: lg
}
