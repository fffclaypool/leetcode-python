class Codec:

    def serialize(self, root):
        def rserialize(root, string):

            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)

            return string

        return rserialize(root, '')

    def deserialize(self, data):

        def rdeserialize(l):

            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)

            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)

        return root
