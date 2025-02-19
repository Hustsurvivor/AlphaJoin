import json
import re

with open('infos/imdb/single_alias_map')as f:
    table2alias = json.load(f)
    
def generate_pg_hint(seq):
    # 定义连接条件的字典映射
    join_mapping = {
        "Nested_Loop": "NestLoop",
        "Hash_Join": "HashJoin",
        "Merge_Join": "MergeJoin",
        # 可以根据需要添加更多连接类型
    }

    # 定义一个简单的树节点结构
    class JoinNode:
        def __init__(self, left, right):
            self.left = left
            # self.join_type = join_type
            self.right = right

    # 解析字符串为树结构
    def parse(tokens):
        def helper(it):
            try:
                token = next(it)
            except StopIteration:
                return None

            if token == '(':
                left = helper(it)
                # join_type = next(it)
                right = helper(it)
                closing = next(it)
                if closing != ')':
                    raise ValueError("Unmatched parentheses")
                return JoinNode(left, right)
            elif token == ')':
                # 这应该由调用者处理
                return None
            else:
                return token

        return helper(iter(tokens))

    # 生成 Leading 提示的递归函数
    def generate_leading(node):
        if isinstance(node, JoinNode):
            left = generate_leading(node.left)
            right = generate_leading(node.right)
            return f"( {left} {right} )"
            # return f"({table2alias[left][0]} {table2alias[right][0]})"
        else:
            return table2alias[node][0]

    # 遍历树并收集 join hints
    def traverse(node, hints):
        if isinstance(node, JoinNode):
            # 先遍历左子树和右子树
            traverse(node.left, hints)
            traverse(node.right, hints)
            # 添加当前节点的 join hint
            # join_type = join_mapping.get(node.join_type, node.join_type)
            # 连接类型的 hint 只需要列出所有涉及的表，不需要嵌套括号
            # 例如 HashJoin(posts postlinks)
            if isinstance(node.left, JoinNode) or isinstance(node.right, JoinNode):
                # 如果子节点是 JoinNode，则需要展平表名
                def collect_tables(n):
                    if isinstance(n, JoinNode):
                        return collect_tables(n.left) + collect_tables(n.right)
                    else:
                        return [n]

                left_tables = collect_tables(node.left)
                right_tables = collect_tables(node.right)
                all_tables = left_tables + right_tables
                # 去重并保持顺序
                seen = set()
                all_tables_unique = [x for x in all_tables if not (x in seen or seen.add(x))]
                hints.append(f"({ ' '.join(all_tables_unique) })")
            else:
                # 如果子节点是表名，直接列出
                hints.append(f"({node.left} {node.right})")

    # 预处理字符串，确保括号与其他字符用空格分开
    seq = seq.replace('(', ' ( ').replace(')', ' ) ')

    # 分词，保留括号作为独立的 token
    tokens = re.findall(r'\(|\)|\S+', seq)
    
    # 调试：打印分词结果
    # print("Tokens:", tokens)

    # 解析字符串为嵌套的 JoinNode 树结构
    try:
        tree = parse(iter(tokens))
    except Exception as e:
        raise ValueError(f"Failed to parse hint string: {e}")

    if tree is None:
        raise ValueError("Empty or invalid hint string.")

    # 收集所有的 join hints
    join_hints = []
    traverse(tree, join_hints)

    # 生成 Leading 提示
    leading = generate_leading(tree)

    hint_core = leading 

    # 构造最终的 pg_hint 字符串
    pg_hint = "/*+ " + f" Leading({leading})" + " */"
    return hint_core, pg_hint