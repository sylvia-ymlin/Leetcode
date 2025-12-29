# 输出表达式结果
# 遇到除数为0，直接 print "ERROR"
# 分数结果化为最简分数，不输出小数

# 需要利用栈结构实现表达式计算
# 支持四种运算：加法（+）、减法（-）、乘法（*）、除法（/） 和 括号
# 我们把表达式拆解为：
# 表达式 = term  +|- term 
# term = factor  *|/ factor 
# factor = number | '(' expression ')'

# 由于结果需要保留为分数，所有计算均以分数形式进行，分子和分母均为整数

# 逻辑复杂，需要使用类实现
# 表达式中可能有空格，可能没有空格，需要先进行拆解


from math import gcd # 引入求最大公约数函数

class ExpressionEvaluator:
    def __init__(self):
        self.expression = ""
        self.stack = []
    
    def reduce(self, a, b):
        """化简分数 a/b"""
        if b == 0:
            print("ERROR")
            exit()
        if a == 0:
            return (0, 1)
        g = gcd(abs(a), abs(b))
        return (a // g, b // g)

    def add(self, frac1, frac2):
        """分数加法 frac1 + frac2"""
        a1, b1 = frac1
        a2, b2 = frac2
        return self.reduce(a1 * b2 + a2 * b1, b1 * b2)

    def sub(self, frac1, frac2):
        """分数减法 frac1 - frac2"""
        a1, b1 = frac1
        a2, b2 = frac2
        return self.reduce(a1 * b2 - a2 * b1, b1 * b2)
    
    def mul(self, frac1, frac2):
        """分数乘法 frac1 * frac2"""
        a1, b1 = frac1
        a2, b2 = frac2
        return self.reduce(a1 * a2, b1 * b2)
    
    def div(self, frac1, frac2):
        """分数除法 frac1 / frac2"""
        a1, b1 = frac1
        a2, b2 = frac2
        return self.reduce(a1 * b2, b1 * a2)
    
    def format(self, f):
        """格式化输出分数，负号只出现在分子前面"""
        a, b = f
        if abs(b) == 1:
            return str(a * b)
        else:
            return f"{a * (1 if b > 0 else -1)}/{abs(b)}"
    
    def express(self):
        """解析表达式：处理加减法"""
        f = self.term() # 拿到第一个项
        # 循环处理所有加减法
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
        """解析项：处理乘除法"""
        f = self.factor()
        # 循环处理所有乘除法
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
        """解析因子：处理数字和括号"""
        if self.expression[self.i] == '(':
            self.i += 1 # 跳过 '('
            f = self.express()
            self.i += 1 # 跳过 ')'
            return f
        else:
            # 处理数字
            num = int(self.expression[self.i])
            self.i += 1
            return (num, 1) # 返回分数形式
    
    def evaluate(self, expr):
        self.expression = expr
        self.i = 0
        result = self.express()
        return self.format(result)
    
evaluator = ExpressionEvaluator()
expression = input().strip() # 读取输入表达式，去除多余空格
result = evaluator.evaluate(expression)
print(result)
    