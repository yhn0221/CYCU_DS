modify_count = 0 ##紀錄交換次數

class StudentNode:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score
        self.left = None
        self.right = None
        self.parent=None##記錄父節點
        self.bf = 0

class StudentTree:
    def __init__(self):
        self.root = None
        
    def height(self, node):
        """計算節點的高度"""
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        """計算節點的平衡因子"""
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return left_height - right_height
    
    def find(self, student_id,node):
        """計算節點的平衡因子"""
        if node is None:# 到底停下
            return node
        if student_id < node.student_id:
            node = self._delete_recursive(node.left, student_id)
            # print(f'if得到的node是{node.student_id}')
        elif student_id > node.student_id:
            node = self._delete_recursive(node.right, student_id)
            # print(f'elif得到的node是{node.student_id}')
        else:
            return node

    def modify(self, node):
        """檢查是RR,RL,LL,LR，並調整"""
        global modify_count
        modify_count+=1
        # print(f'交換次數:{modify_count}')
        node_bf = self.balance_factor(node)
        if node_bf>1:
            """偏左"""
            child_bf=self.balance_factor(node.left)
            if child_bf<0:
                """LR"""
                ##先記錄各點的資料
                right=node.right##1
                left_left=node.left.left##2
                left_right_left=node.left.right.left##3
                left_right_right=node.left.right.right##4
                left=node.left##B
                left_right=node.left.right##C
                ##node自己是A

                ##開始調整位置，C來當這顆子樹的根
                left_right.left=left##B
                left_right.right=node##A
                left.left=left_left##2
                left.right=left_right_left##3
                node.left=left_right_right##4
                node.right=right##1

                ##調整個點的parent
                left_right.parent=node.parent##改c的父nood
                if node.parent != None:
                    if node.parent.left==node:##讓子樹的爸爸所指更改
                        node.parent.left=left_right
                    else:
                        node.parent.right=left_right
                else:
                    self.root=left_right

                left.parent=left_right##B的父等於c
                node.parent=left_right##A的父等於c
                if left_right_left != None:
                    left_right_left.parent=left##3的父等於B
                if left_right_right != None:
                    left_right_right.parent=node##4的父等於A

            else:
                """LL"""
                ##先記錄各點的資料
                right=node.right##1
                left_right=node.left.right##2
                left_left_right=node.left.left.right##3
                left_left_left=node.left.left.left##4
                left=node.left##B
                left_left=node.left.left##C
                ##node自己是A

                ##開始調整位置，B來當這顆子樹的根
                # left.left=left##B的左=c
                left.right=node##B的右=A
                # print(f'{left.student_id}的右={left.right.student_id}')
                node.left=left_right##2
                # if node.left != None:
                #     print(f'{node.student_id}的左={node.left.student_id}')
                # else:
                #     print(f'{node.student_id}A的左=none')

                ##調整個點的parent
                left.parent=node.parent##改b的父nood
                if node.parent != None:
                    if node.parent.left==node:##讓子樹的爸爸所指更改
                        node.parent.left=left
                    else:
                        node.parent.right=left
                else:
                    self.root=left

                left_left.parent=left##c的父等於b
                # print(f'{left_left.student_id}的父={left_left.parent.student_id}')
                node.parent=left##A的父等於b
                # print(f'{node.student_id}的父={node.parent.student_id}')
                if left_right != None:
                    left_right.parent=node##2的父等於A

                

        else:
            """偏右"""
            child_bf=self.balance_factor(node.right)
            # print(f'{node.student_id}')
            if child_bf>0:
                """RL"""
                # print('經過RL')
                ##先記錄各點的資料
                left=node.left##1
                right_right=node.right.right##2
                right_left_left=node.right.left.left##3
                right_left_right=node.right.left.right##4
                right=node.right##B                
                right_left=node.right.left##C
                # print(f'{right.student_id},{right_left.student_id}')
                ##node自己是A
                
                ##開始調整位置，C來當這顆子樹的根
                right_left.right=right##B
                right_left.left=node##A
                node.right=right_left_left##3
                right.left=right_left_right##4

                ##調整個點的parent
                right_left.parent=node.parent##改c的父nood
                if node.parent != None:
                    if node.parent.left==node:##讓子樹的爸爸所指更改
                        node.parent.left=right_left
                    else:
                        node.parent.right=right_left
                else:
                    self.root=right_left
                right.parent=right_left##B的父等於c
                node.parent=right_left##A的父等於c
                if right_left_right != None:
                    right_left_right.parent=right##4的父等於B
                if right_left_right != None:
                    right_left_right.parent=node##3的父等於A
                # print(f'11111,{node.parent.right.student_id}')

            else:
                """RR"""
                ##先記錄各點的資料
                left=node.left##1
                right_left=node.right.left##2
                right_right_left=node.right.right.left##3
                right_right_right=node.right.right.right##4
                right=node.right##B
                right_right=node.right.right##C
                ##node自己是A

                ##開始調整位置，B來當這顆子樹的根
                right.right=right_right##B的右=c
                right.left=node##B的左=A
                node.right=right_left##2

                ##調整個點的parent
                right.parent=node.parent##改b的父nood
                if node.parent != None:
                    if node.parent.left==node:##讓子樹的爸爸所指更改
                        node.parent.left=right
                    else:
                        node.parent.right=right
                else:
                    self.root=right
                node.parent=right##A的父等於c
                if right_left!=None:
                    right_left.parent=node##2的父等於A

    def check_balance(self, node):
        """遞迴檢查每個節點的平衡因子，並打印出來"""
        if node is not None:
            node_bf = self.balance_factor(node)
            # print(f'現在檢查Node {node.student_id} (BF: {node_bf}) ')
            if abs(node_bf)>1:
                self.modify(node)
                # print(f'{node.parent.student_id}')
                # self.check_balance(student_tree.root)
            else:
                self.check_balance(node.parent)

    def insert(self, student_id, name, score):
        """根據學生ID插入新的學生資料"""
        new_node = StudentNode(student_id, name, score)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)
        self.check_balance(new_node)

    def _insert_recursive(self, node, new_node):
        """遞迴方式在適當的位置插入新學生節點"""
        if new_node.student_id < node.student_id:
            if node.left is None:
                node.left = new_node
                new_node.parent=node
            else:
                self._insert_recursive(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
                new_node.parent=node
            else:
                self._insert_recursive(node.right, new_node)


    def preorder(self):
        return self._preorder(self.root)
    
    def _preorder(self, node):
        if node is not None:
            return [node.student_id] + self._preorder(node.left) + self._preorder(node.right)
        else:
            return []

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            return self._inorder(node.left) + [node.student_id] + self._inorder(node.right)
        else:
            return []



    ##
    def display(self):
        """以中序遍歷的方式打印二元樹中的所有學生資料"""
        self._display_recursive(self.root)

    def _display_recursive(self, node):
        """遞迴方式打印每個學生節點的資料"""
        if node is not None:
            self._display_recursive(node.left)
            print(f'Student ID: {node.student_id}, Name: {node.name}, Score: {node.score}, BF:{node.bf}')
            self._display_recursive(node.right)
    ##

    ###

    def calculate_bf(self, node):
        """遞迴計算每個節點的bf"""
        if node is not None:
            bf = self.balance_factor(node)
            node.bf=bf
            # print(f'Student ID: {node.student_id}, BF: {bf}')
            self.calculate_bf(node.left)
            self.calculate_bf(node.right) 

    ###

    def delete(self, student_id):
        node=self._delete_recursive(self.root, student_id)
        # print(f'在delete這邊{node.right.student_id}')
        self.check_balance(node)

    def _delete_recursive(self, node, student_id):
        if node is None:# 到底停下
            return node
        if student_id < node.student_id:
            node = self._delete_recursive(node.left, student_id)
            # print(f'if得到的node是{node.student_id}')
        elif student_id > node.student_id:
            node = self._delete_recursive(node.right, student_id)
            # print(f'elif得到的node是{node.student_id}')
        else:
            """找到該點"""
            #沒孩子
            if node.left == None and node.right == None:
                # print(f'現在處理的node={node.student_id}')
                temp=node.parent
                if temp != None:
                    if temp.left == node:
                        temp.left=None
                    else:
                        temp.right=None
                        # node.parent.right=None

                else:
                    self.root = None
                node=None
                # print(f'經過這裡,{temp.student_id}')
                return temp

            # 只有一個小孩
            elif node.left == None:
                temp = node.right
                temp.parent=node.parent
                if node.parent != None:
                    if node.parent.left == node:#找node在父節點的左或右
                        node.parent.left=temp
                    else:
                        node.parent.right=temp
                else:
                    self.root=temp

                node = None
                return temp
            elif node.right == None:
                temp = node.left
                temp.parent=node.parent
                if node.parent != None:
                    if node.parent.left == node:#找node在父節點的左或右
                        node.parent.left=temp
                    else:
                        node.parent.right=temp
                else:
                    self.root=temp
                node = None
                return temp
            
            else:# 2個小孩 取右子樹最小
                temp = self._min_value_node(node.right)
                node.student_id = temp.student_id
                node.name = temp.name
                node.score = temp.score
                node.right = self._delete_recursive(node.right, temp.student_id)
                if node.right==node:
                    node.right=None
                    return node
                # print(f'node的右{node.right.student_id}')
                return node.right
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

def work(mode):
    if mode == 1:
        """insert"""
        print('進行插入任務')
        # 用戶輸入整個資訊
        print('請直接輸入ilearning上複製後的字串，例如:')
        print('Student ID: 20310')
        print('Student Name: Mary')
        print('Student Score: 90 ')
        print('')
        input_data1 = input("")
        input_data2 = input("")
        input_data3= input("")


        # 分割字符串
        parts = input_data1.split(':')
        # 提取 ID（去除前後空格）
        student_id = int(parts[1].strip())

        # 分割字符串
        parts = input_data2.split(':')
        # 提取 ID（去除前後空格）
        student_name = (parts[1].strip())

        # 分割字符串
        parts = input_data3.split(':')
        # 提取 ID（去除前後空格）
        student_score = int(parts[1].strip())


        student_tree.insert(student_id, student_name, student_score)
        print('')
        print('學生資料清單:')

        print("Pre-order traversal:", student_tree.preorder())
        print("In-order traversal:", student_tree.inorder())
        student_tree.calculate_bf(student_tree.root)
        student_tree.display()
        print('')

    elif mode == 2:
        """delete"""
        print('進行刪除任務')
        delete_id=int(input('輸入要刪除的學生的ID，即可:'))
        student_tree.delete(delete_id)
        print("Pre-order traversal:", student_tree.preorder())
        print("In-order traversal:", student_tree.inorder())
        student_tree.calculate_bf(student_tree.root)
        student_tree.display()
        print('')  
    elif mode == 3:
        """檢查清單"""
        print('進行檢查清單任務')
        print('')
        print('學生資料清單:')

        print("Pre-order traversal:", student_tree.preorder())
        print("In-order traversal:", student_tree.inorder())
        student_tree.calculate_bf(student_tree.root)
        student_tree.display()
        print('')
    elif mode == 4:
        """調整"""
        print('進行調整任務')
        mod_id=input('你要調整的ID是?')
        student_id = int(mod_id.strip())
        node=student_tree.find(student_id,student_tree.root)
        print(f'目前的id是{node.student_id},名字是{node.name},成績是{node.score}')
        input_data1=input('你要調整的名字')
        input_data2=input('你要調整的成績')
        student_name = (input_data1.strip())
        student_score = int(input_data2.strip())
        node.name=student_name
        node.score=student_score
        student_tree.calculate_bf(student_tree.root)
        student_tree.display()


    else:
        print('重新輸入')
####main
student_tree = StudentTree()
while True:
    try:
        mode = input('輸入要做的任務，插入1，刪除2，查看3，調整4，會自動平衡: ')
        mode = int(mode)  # 嘗試將輸入轉換成整數
        if mode in [1, 2, 3, 4]:  # 檢查是否是有效的選項
            work(mode)  
        else:
            print("請輸入1, 2, 3 或 4。")  
    except ValueError:
        print("無效的輸入！請輸入一個整數。")  # 處理非整數的輸入
