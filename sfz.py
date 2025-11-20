class MotorPair:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # special case: run_angle called with different signs
    def run_angle(self, speed, angle, wait=True):
        self.left.run_angle(speed, angle, wait=wait)
        self.right.run_angle(-speed, angle, wait=wait)

    # fallback for all other cases
    def __getattr__(self, name):
        attr_left = getattr(self.left, name)
        attr_right = getattr(self.right, name)

        def wrapper(*args, **kwargs):
            r1 = attr_left(*args, **kwargs)
            r2 = attr_right(*args, **kwargs)
            # Wenn du Rückgabewerte brauchst:
            return r1, r2

        return wrapper
