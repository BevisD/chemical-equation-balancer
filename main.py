import numpy as np
import re


def get_equation_sides(raw_inp):
    raw_inp = raw_inp.replace(" ", "")
    return re.split(r"->|=", raw_inp)


def get_equation_terms(side):
    return re.findall(r"(?:\(?[A-Z][a-z]*\d*\)?\d*)+", side)


def get_matrix_equation(terms_1, terms_2):
    dim = len(terms_2) + len(terms_1) - 1
    matrix = np.zeros((dim, dim))
    vector = np.zeros(dim)

    elements = {}
    for col, term in enumerate(terms_1):
        segments = re.findall(r"([A-Z][a-z]*)(\d*)", term)
        for segment in segments:
            element, number = segment
            if element not in elements:
                if len(elements) == 0:
                    elements[element] = 0
                else:
                    elements[element] = max(elements.values()) + 1
            row = elements[element]

            if number == "":
                number = 1
            else:
                number = int(number)
            matrix[row][col] = number

    for col, term in enumerate(terms_2[:-1]):
        segments = re.findall(r"([A-Z][a-z]*)(\d*)", term)
        for segment in segments:
            element, number = segment
            if element not in elements:
                if len(elements) == 0:
                    elements[element] = 0
                else:
                    elements[element] = max(elements.values()) + 1
            row = elements[element]

            if number == "":
                number = -1
            else:
                number = -int(number)
            matrix[row][col + len(terms_1)] = number

    term = terms_2[-1]
    segments = re.findall(r"([A-Z][a-z]*)(\d*)", term)
    for segment in segments:
        element, number = segment
        if element not in elements:
            if len(elements) == 0:
                elements[element] = 0
            else:
                elements[element] = max(elements.values()) + 1
        row = elements[element]

        if number == "":
            number = 1
        else:
            number = int(number)
        vector[row] = number
    return matrix, vector


def solve_matrix_equation(matrix, vector):
    try:
        inverse = np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        print("Equation Can not be Balanced")
        return
    coefficients = np.matmul(inverse, vector.transpose())
    coefficients = np.append(coefficients, 1)
    return coefficients


def simplify_coefficients(coefficients):
    if 0 not in coefficients:
        coefficients /= np.min(coefficients)
        coefficients = np.round(coefficients).astype(int)
    else:
        return

    return coefficients


def display_balanced_equation(coefficients, l_terms, r_terms):
    new_l_terms = []
    new_r_terms = []
    for i, term in enumerate(l_terms):
        c = coefficients[i]
        str_c = str(abs(c)) if abs(c) != 1 else ""

        if c > 0:
            new_l_terms.append((str_c, term))
        else:
            new_r_terms.append((str_c, term))

    for i, term in enumerate(r_terms):
        c = coefficients[i + len(l_terms)]
        str_c = str(abs(c)) if abs(c) not in [0, 1] else ""
        if c > 0:
            new_r_terms.append((str_c, term))
        else:
            new_l_terms.append((str_c, term))

    output = ' + '.join([''.join(term) for term in new_l_terms]) + \
             " -> " + \
             ' + '.join([''.join(term) for term in new_r_terms])
    return output


def main():
    # inp = input("Enter a Chemical Equation to Balance (Separate Sides With '=' or '->'): \n")
    inp = "He + O2->2He2O"
    l_side, r_side = get_equation_sides(inp)
    l_terms = get_equation_terms(l_side)
    r_terms = get_equation_terms(r_side)

    matrix, vector = get_matrix_equation(l_terms, r_terms)
    coefficients = solve_matrix_equation(matrix, vector)
    if coefficients is None:
        return

    coefficients = simplify_coefficients(coefficients)
    if coefficients is not None:
        print(display_balanced_equation(coefficients, l_terms, r_terms))
    else:
        print("Equation Can not be Balanced")
        return


if __name__ == "__main__":
    main()
