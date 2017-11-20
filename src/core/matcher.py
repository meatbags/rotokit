
class Matcher:
    def __init__(self):
        pass

    def matchGroups(self, a, b):
        if len(a) != len(b):
            print('Warning: Group size mismatch.')

        # update path profiles
        for path in a + b:
            path.updateProfile()

        # update path groups
        for path in a:
            path.updateGroup(a)
        for path in b:
            path.updateGroup(b)

        # match !
        pass
