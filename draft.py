#length = 15
#expression = '123.45#1+126.53@'
expression = '1#3+1#0.4'

def calculate(expression):
    # 定义特殊字符的加法规则
    special_rules = {
        "!+!=": 0,
        "!+@": 13,
        "!+#": 4,
        "@+@": 7,
        "@+#": 20,
        "#+#": 5
    }

    # 将字符串按运算符分割为左右两部分
    left, right = expression.split("+")

    # 计算表达式结果
    if set(left) & set("!@#") or set(right) & set("!@#"):
        # 如果表达式中包含特殊字符，则使用特殊规则计算
        left_point_pos = left.find(".")
        if left_point_pos == -1:
            left_point_pos = len(left)
        right_point_pos = left.find('.')
        left_pos = []
        left_chart = []
        left = list(left)
        for i in range(len(left)):
            if left[i] == '!' or left[i] == '@' or left[i] == '#':
                left_pos.append(i)
                left_chart.append(left[i])
                left[i] = '0'
        #right_pos = []
        right_chart = []
        right = list(right)
        for i in range(len(right)):
            if right[i] == '!' or right[i] == '@' or right[i] == '#':
                #right_pos.append(i)
                right_chart.append(right[i])
                right[i] = "0"
        ans1 = float("".join(left)) + float("".join(right))
        ans2 = 0
        for i in range(len(left_pos)):
            rule1 = '+'.join([left_chart[i],right_chart[i]])
            rule2 = '+'.join([right_chart[i],left_chart[i]])
            value1 = special_rules.get(rule1,0)
            value2 = 0
            if value1 == 0:
                value2 = special_rules.get(rule2,0)
            weigth = left_point_pos-left_pos[i]
            if weigth > 0:
                weigth -= 1
            ans2+=(value1+value2)*(pow(10,weigth))
        return ans1 + ans2
    else:
        # 否则将字符串转换为浮点数并相加
        return float(left) + float(right)


result = calculate(expression)
if result.is_integer():
    # 如果结果是整数，则去掉小数部分
    print(int(result))
else:
    print(result)

