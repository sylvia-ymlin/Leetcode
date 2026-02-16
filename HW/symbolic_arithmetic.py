# Output expression result
# If divisor is 0, print "ERROR"
# Result fraction must be simplified, do not output decimal
# Support +, -, *, /, and brackets ()

# Logic:
# Expression = term +|- term
# Term = factor *|/ factor
# factor = number | '(' expression ')'

# Use simplfied fractions (numerator, denominator) for all calcs

from math import gcd

class ExpressionEvaluator:
    def __init__(self):
        self.expression = ""
        self.stack = []
        self.i = 0
    
    def reduce(self, a, b):
        """Simplify fraction a/b"""
        if b == 0:
            print("ERROR")
            exit()
        if a == 0:
            return (0, 1)
        g = gcd(abs(a), abs(b))
        return (a // g, b // g)

    def add(self, frac1, frac2):
        """frac1 + frac2"""
        a1, b1 = frac1
        a2, b2 = frac2
        return self.reduce(a1 * b2 + a2 * b1, b1 * b2)

    def sub(self, frac1, frac2):
        """frac1 - frac2"""
        a1, b1 = frac1
        a2, b2 = frac2
        return self.reduce(a1 * b2 - a2 * b1, b1 * b2)
    
    def mul(self, frac1, frac2):
        """frac1 * frac2"""
        a1, b1 = frac1
        a2, b2 = frac2
        return self.reduce(a1 * a2, b1 * b2)
    
    def div(self, frac1, frac2):
        """frac1 / frac2"""
        a1, b1 = frac1
        a2, b2 = frac2
        return self.reduce(a1 * b2, b1 * a2)
    
    def format(self, f):
        """Format output, negative sign only on numerator"""
        a, b = f
        if abs(b) == 1:
            return str(a * b)
        else:
            return f"{a * (1 if b > 0 else -1)}/{abs(b)}"
    
    def express(self):
        """Parse expression: Handle + -"""
        f = self.term()
        while self.i < len(self.expression) and self.expression[self.i] in ('+', '-'):
            op = self.expression[self.i]
            self.i += 1
            next_term = self.term()
            if op == '+':
                f = self.add(f, next_term)
            else:
                f = self.sub(f, next_term)
        return f

    def term(self):
        """Parse term: Handle * /"""
        f = self.factor()
        while self.i < len(self.expression) and self.expression[self.i] in ('*', '/'):
            op = self.expression[self.i]
            self.i += 1
            next_factor = self.factor()
            if op == '*':
                f = self.mul(f, next_factor)
            else:
                f = self.div(f, next_factor)
        return f

    def factor(self):
        """Parse factor: Handle number and brackets"""
        if self.expression[self.i] == '(':
            self.i += 1 # skip '('
            f = self.express()
            self.i += 1 # skip ')'
            return f
        else:
            # Handle number (possibly multi-digit)
            # Original code only did `int(self.expression[self.i])` -> Single digit!!
            # Sample might imply multi-digit support?
            # "Factor = number". Usually implies full integer.
            # Original code: `num = int(self.expression[self.i]); self.i += 1`.
            # This is a BUG if numbers are > 9.
            # I should fix to read full number.
            start = self.i
            # Look ahead for handle negative numbers?
            # Usually expression like "-3" handled as 0-3 or unary operator.
            # Here assuming simple parsing, maybe no unary minus?
            # Or unary minus handled by `express` if term starts with it?
            # Check original code structure `express -> term -> factor`.
            # If input is "-1+2", `term` calls `factor`, `factor` reads `num`.
            # It fails on `-`.
            # But maybe input format guarantees valid expression?
            # Or maybe inputs are non-negative integers combined with operators?
            # Assuming non-negative integers for `factor`.
            # Parse digits.
            if self.expression[self.i] == '-': # Handle unary minus inside factor? Not typical.
                 pass
            
            # Read all digits
            while self.i < len(self.expression) and self.expression[self.i].isdigit():
                self.i += 1
            num = int(self.expression[start:self.i])
            return (num, 1)
    
    def evaluate(self, expr):
        self.expression = expr
        self.i = 0
        result = self.express()
        return self.format(result)
    
evaluator = ExpressionEvaluator()
expression = input().strip() # Input might contain spaces?
# Original code comment: "Expression might have spaces... need to dismantle".
# But `input().strip()` only removes ends.
# Best to remove ALL spaces for this parser.
expression = expression.replace(" ", "")
result = evaluator.evaluate(expression)
print(result)